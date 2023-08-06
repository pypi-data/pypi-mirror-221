# promptz

A lightweight library, built on top of pandas and pydantic, that lets you interact and control language models and store the output as queryable embeddings.

## Getting starting

To follow along and run the examples interactively using [./basic-usage.ipynb]().

```python
pip install promptz
```

Setup

```python
import os
import promptz
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

llm = promptz.ChatGPT(
    api_key=os.environ['OPENAI_API_KEY'],
    org_id=os.environ['OPENAI_ORGANIZATION_ID'],
)

ef = OpenAIEmbeddingFunction(
    api_key=os.environ['OPENAI_API_KEY'],
    model_name="text-embedding-ada-002",
)

promptz.init(llm=llm, ef=ef)
```

The `init` accepts configuration options and activates a session, which allows you to interact with generative models, store results, and query collections. 

```python
from promptz import prompt

character = 'Batman'
prompt(f'Write a character profile for {character}')
```

Output will vary depending on the model, but using ChatGPT we get something like:

```
Name: Bruce Wayne (Batman)                                                      
                                                                                
Age: 35                                                                         
                                                                                
Occupation: Vigilante, CEO of Wayne Enterprises                                 
                                                                                
Physical Appearance: Tall and muscular build, with a dark and brooding presence.
Wears a black batsuit with a cape, utility belt, and a bat symbol on his chest.
His face is covered by a mask, leaving only his piercing blue eyes visible.
                                                                                
Personality: Intense, determined, and highly disciplined. Bruce Wayne is known
for his relentless pursuit of justice and his unwavering commitment to
protecting Gotham City. He is intensely focused, often seen as aloof and...
```

The response is a raw string of the response from the model. This is what you want if you're writing an email or asking a question, but other times you'll need to convert the response into structured data.

To do that, you can pass a `pydantic.BaseModel` as `output=` when calling `prompt`. This will add format instructions, based on the pydantic schema and field annotations, and return an instance of the output model using the generated data.

```python
from typing import List
from pydantic import BaseModel, Field
from promptz import prompt

class Character(BaseModel):
    name: str = Field(..., unique=True, embed=False),
    description: str = Field(
        ..., description='Describe the character in a few sentences')
    age: int = Field(..., min=1, max=120)

characters = prompt(
    'Generate some characters from the Batman universe',
    output=List[Character],
)
```
```
        type      name                                        description  age
0  character    Batman  Batman, also known as Bruce Wayne, is a billio...   35
1  character     Joker  The Joker, also known as Arthur Fleck, is the ...   40
2  character  Catwoman  Catwoman, also known as Selina Kyle, is a skil...   30
```

This example defines the output as `List[Character]` so a `pd.Dataframe` will be returned with multiple characters. If we used `output=Character` a single `Character` object would be returned instead.

```python
batman = prompt('Generate a character profile for Batman', ouput=Character)
```
```
{"age": 35, "type": "character", "name": "Batman", "id": "ee49c4e5-4c7d-4790-ba1b-80ebff4c43d7", "description": "Batman, also known as Bruce Wayne, is a wealthy philanthropist and vigilant crime-fighter who operates in Gotham City. Driven by the tragic murder of his parents, Batman uses his intelligence, strength, and gadgets to protect his city from chaos and corruption."}
```

You can further guide the model output by providing few shot examples. This is especially useful for controlling the style or specific language used in text. Here's an example the uses a more wordy description, which should prompt the model to return more expressive results.

```python

character = prompt(
    'Generate a character from the Batman universe',
    examples=[
        (
            None, 
            Character(
                name='Batman', 
                description="Immersed in the oppressive cloak of nightfall, a figure emerges, solitary and resolute - the Batman. Like an apparition carved from the darkest fears of the human heart, he is a chilling silhouette against the city's venomous glow, embodying a vow birthed from the ashes of personal tragedy. His is the eternal dance with Gotham's nightmarish symphony, a spectral waltz of justice and retribution, his soul as scarred and formidable as the armored veil that encases him.",
                age=32,
            ),
        ),
    ],
    output=Character,
)
```
```
{"name": "Joker", "description": "In a city fueled by corruption and madness,
there exists a maniacal criminal mastermind known as the Joker. With his
clownish appearance and signature eerie grin, he wreaks havoc on Gotham City,
plunging it into chaos and anarchy. The Joker is unpredictable, his twisted
sense of humor matched only by his sadistic pleasure in causing mayhem. Behind
his painted facade lies a deranged and dangerous mind, making him the perfect
foil for the Dark Knight.", "age": 45}
```

TODO: improve this - needs to introduce collections properly.
You can store any output from prompts in a `Collection`, which extends `pd.Dataframe`.

```python
from promptz import store

store(characters)
```
```
        type      name                                        description  age
0  character    Batman  Batman, also known as Bruce Wayne, is a billio...   35
1  character     Joker  The Joker, also known as Arthur Fleck, is the ...   40
2  character  Catwoman  Catwoman, also known as Selina Kyle, is a skil...   30
```

When items are stored embeddings are computed for each field. For example, `[{name: 'Batman'}, {description: 'Batman, also known as...'}, {age: 35}]` would be converted into 3 embeddings for the first item. You can then query collections using those field embeddings.

```python
from promptz import query

villains = query('they are a villain').first
```
```
```

Data can be updated using standard panda transforms and passing the result to `store`.

```python
villains['evil'] = True
store(villains)
```
```
```

Now lets try creating a few more characters. A unique constraint is set on the character name field, which prevents duplicates from being stored, but we need to modify the prompt slightly to avoid generating existing characters. 

```python
from promptz import Prompt

sample = query(where={'type': 'character'}).sample(3)
examples = [
    { 'existing_characters': [name for name in sample[:2]['name']] },
    sample[2:],
]

p = Prompt(
    '''
    Generate a list of new random characters from the Batman universe.
    Don't use any of the existing characters.
    ''',
    examples=examples,
    output=List[Character],
)
```

This is then called in a loop and the existing characters are fetched from the store on each iteration. Further guidence is provided by the examples by selecting 3 random characters and using them to construct the expected input/output.

```python
examples = query(where={'type': 'character'}).sample(3)
for _ in range(5):
    existing = query(where={'type': 'character'})
    cs = p({ 'existing_characters': [name for name in existing['name']] })
    store(cs)
```

Running this for 5 iterations on ChatGPT generates something like this.

```
```

Now lets do the same for locations and items and then pull them together to generate some story ideas.

```python
class StoryIdea(BaseModel):
    title: str
    description: str = None
    characters: List[str] = []

villains = query('they are a villain').sample(3)

ideas = prompt(
    'Generate some story ideas',
    input={
        'characters': [batman] + villains.objects,
    },
    output=List[StoryIdea],
)
```
```
```

Finally, let's store those ideas, but instead of using the default collection we'll add them to a new `story_ideas` collection.

```python
store(*ideas, collection='story_ideas')
collection('story_ideas')
```
```
```