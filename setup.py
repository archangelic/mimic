from setuptools import setup

setup(
    name = 'mimic',
    py_modules = ['mimic'],
    version='0.1.1',
    install_requires = [
        'nltk',
        'markovify'
    ]
)
