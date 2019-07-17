from setuptools import setup

setup(
    name = 'mimic',
    packages = ['mimic'],
    install_requires = [
        'nltk',
        'markovify'
    ]
)
