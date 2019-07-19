import json
import re

import markovify
import nltk

class Mimic:
    model = None

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

    def create_from_file(self, corpus, newline=False, **kwargs):
        with open(corpus) as c:
            text = c.read()
        self._create_model(text, newline, **kwargs)

    def create_from_string(self, corpus, newline=False, **kwargs):
        self._create_model(corpus, newline, **kwargs)

    def from_json(self, _json):
        self.model = self.Text.from_json(_json)

    def from_json_file(self, _json_file):
        with open(_json_file) as j:
            self.model = self.Text.from_json(json.load(j))

    def to_json_file(self, _json_file):
        with open(_json_file) as j:
            json.dump(self.model.to_json(), j)

    def make_sentence(self):
        return self.model.make_sentence()

    def make_short_sentence(self, length):
        return self.model.make_short_sentence(length)
