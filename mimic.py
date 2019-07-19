import json
import re

import markovify
import nltk

class Mimic:
    model = None

    def __init__(self, from_file=None, from_string=None, from_json=None, newline=False, **kwargs):
        if from_file:
            _from_file(from_file, newline=newline, **kwargs)
        elif from_string:
            _from_string(from_string, newline=newline, **kwargs)
        elif from_json:
            _from_json(from_json)

    class Text(markovify.Text):
        def word_split(self, sentence):
            words = re.split(self.word_split_pattern, sentence)
            words = [w for w in words if len(w) > 0]
            words = [":-:".join(tag) for tag in nltk.pos_tag(words)]
            return words

        def word_join(self, words):
            sentence = " ".join(word.split(":-:")[0] for word in words)
            return sentence

    class NewlineText(markovify.NewlineText):
        def word_split(self, sentence):
            words = re.split(self.word_split_pattern, sentence)
            words = [w for w in words if len(w) > 0]
            words = [":-:".join(tag) for tag in nltk.pos_tag(words)]
            return words

        def word_join(self, words):
            sentence = " ".join(word.split(":-:")[0] for word in words)
            return sentence

    def _create_model(self, corpus, newline=False, **kwargs):
        if newline:
            self.model = self.NewlineText(corpus, **kwargs)
        else:
            self.model = self.Text(corpus, **kwargs)

    @classmethod
    def create_from_file(cls, corpus, newline=False, **kwargs):
        return cls(from_file=corpus, newline=newline, **kwargs)

    def _from_file(self, corpus, newline=False, **kwargs):
        with open(corpus) as c:
            text = c.read()
        self._create_model(text, newline, **kwargs)

    @classmethod
    def create_from_string(cls, corpus, newline=False, **kwargs):
        return cls(from_string=corpus, newline=newline, **kwargs)

    def _from_string(self, corpus, newline=False, **kwargs):
        self._create_model(corpus, newline, **kwargs)

    @classmethod
    def from_json(cls, _json):
        return cls(from_json=_json)

    def _from_json(self, _json):
        self.model = self.Text.from_json(_json)

    @classmethod
    def from_json_file(cls, _json_file):
        with open(_json_file) as j:
            jdict = json.load(j)
        return cls(from_json=jdict)

    def to_json_file(self, _json_file):
        with open(_json_file) as j:
            json.dump(self.model.to_json(), j)

    def make_sentence(self):
        return self.model.make_sentence()

    def make_short_sentence(self, length):
        return self.model.make_short_sentence(length)
