# mimic
personal module to bootstrap markov projects

## basic usage
``` python
from mimic.mimic import Mimic

markov_model = Mimic().create_from_file('corpus.txt')

markov_model.create_sentence()
```

this relies on `nltk` so you will need to download the sources for that.
