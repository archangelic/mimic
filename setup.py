from setuptools import setup

setup(
    name = 'mimic',
    py_modules = ['mimic'],
    install_requires = [
        'nltk',
        'markovify'
    ]
)
