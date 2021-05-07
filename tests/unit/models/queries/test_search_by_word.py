from unittest import TestCase

from app.models.queries.search_by_word import SearchByWord


class TestSearchByWord(TestCase):

    WORD = 'dummy'

    def setUp(self) -> None:
        self.search = SearchByWord(type(self).WORD)

    def tearDown(self) -> None:
        del self.search

    def test_search_field(self):
        query, option = self.search.search_field()
        expected = {'word': type(self).WORD}
        self.assertDictEqual(query, expected)
        expected = {'_id': 1, 'position': 1}
        self.assertDictEqual(option, expected)
