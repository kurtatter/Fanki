import string
import validators
from lxml.builder import unicode


class TextCruncher:
    def __init__(self, text: str):
        self.text = text

    def taran(self, words: list) -> list:
        clear_words = []
        for word in words:
            result = set(word) - set(string.ascii_letters)
            if not result:
                clear_words.append(word)
        return clear_words

    def crunch_to_words(self) -> list:
        nt_words = self._not_punctuation(self._space_crunch())
        nn_words = self._not_digits(nt_words)
        nr_words = self._not_repeat(nn_words)
        nu_words = self._not_urls(nr_words)
        ne_words = self._not_empty(nu_words)
        cl_words = self.taran(ne_words)
        return cl_words

    def _space_crunch(self) -> list:
        clear_text = None
        for space_symbol in string.whitespace:
            clear_text = self.text.strip(space_symbol)
        return clear_text.split()

    def _not_punctuation(self, words: list) -> list:
        for puntuation in string.punctuation:
            words = list(map(lambda word: word.strip(puntuation), words))
        for space_symbol in string.whitespace:
            words = list(map(lambda word: word.strip(space_symbol), words))
        return words

    def _not_digits(self, words: list) -> list:
        words = list(filter(lambda word: not word.replace('.', '').isdigit(), words))
        return words

    def _not_urls(self, words: list) -> list:
        words = list(filter(lambda word: not validators.url(word), words))
        return words

    def _not_empty(self, words: list) -> list:
        words = list(filter(lambda word: word, words))
        return words

    def _clear_words(self, words: list) -> list:
        for_clear_symbols = r'()"/\¶“_'
        clear_words = []
        for word in words:
            for symbol in for_clear_symbols:
                word = word.replace(symbol, '')
            if r'\u' in word or '–' in word or not word.isprintable():
                continue
            else:
                clear_words.append(word)

        return clear_words

    def _not_repeat(self, words: list) -> list:
        words = list(set(words))
        return words
