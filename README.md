# mimic
personal module to bootstrap markov projects. really just a wrapper over the *really damn good* [markovify](https://github.com/jsvine/markovify).

## basic usage
``` python
from mimic import Mimic

markov_model = Mimic.create_from_file('corpus.txt')

markov_model.make_sentence()
```

also can be created using `Mimic.create_from_string` and can do sentences based on newlines by passing `newline=True`.

this relies on `nltk` so you will need to download the sources for that.
