from os import environ
from unittest import TestCase, mock

from app.utils.filters.anagrams import Anagrams


class TestAnagrams(TestCase):

    def test_unique_list_same_order(self):
        data = ['aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'd', 'ef', 'fe']
        expected = ['aa', 'bb', 'cc', 'd', 'ef', 'fe']

        output = Anagrams.unique_list_same_order(data)
        self.assertListEqual(expected, output)

        data = []
        output = Anagrams.unique_list_same_order(data)
        self.assertListEqual(data, output)

    def test_get_coincidences(self):
        container = ['pesa', 'sepa', 'agua', 'otro', 'pasa', 'sapa', 'coto']

        word = 'pasa'
        expected = ['pasa', 'sapa']
        output = Anagrams.get_coincidences(word, container)
        self.assertListEqual(expected, output)

        word = 'hola'
        expected = []
        output = Anagrams.get_coincidences(word, container)
        self.assertListEqual(expected, output)

    def test_get_coincidences_empty_container(self):
        word = 'fake'
        container = []
        expected = []
        output = Anagrams.get_coincidences(word, container)
        self.assertListEqual(expected, output)

    @mock.patch.dict(environ, {'WILL_HAVE_WORDS_REPETEAD': '1'})
    def test_get_coincidences_container_with_repetitions(self):
        word = 'casa'
        container = ['saca', 'saca', 'csaa', 'aasc', 'repo', 'hola', 'cosa']
        expected = ['saca', 'saca', 'csaa', 'aasc']
        output = Anagrams.get_coincidences(word, container)
        self.assertListEqual(expected, output)

    def test_removee_item_in_list(self):
        word = 'cosa'
        container = [
            {'word': 'cosa'},
            {'word': 'cosa'},
            {'word': 'cosa'},
            {'word': 'casa'},
            {'word': 'sosa'},
        ]
        expected = ['casa', 'sosa']
        output = Anagrams.remove_item_in_list(word, container)
        self.assertListEqual(expected, output)