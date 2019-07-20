from setuptools import setup

setup(
    name = 'mimic',
    py_modules = ['mimic'],
    version='0.1.0',
    install_requires = [
        'nltk',
        'markovify'
    ]
)
