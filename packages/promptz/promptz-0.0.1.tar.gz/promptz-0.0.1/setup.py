from setuptools import setup

setup(
    name='promptz',
    version='0.0.1',
    description='A Python package for interactive prompts',
    packages=['promptz'],
    entry_points={
        'console_scripts': [
            'promptz=promptz.main:main'
        ]
    },
)