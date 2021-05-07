from unittest import TestCase

from app.models.queries.search_by_position import SearchByPosition


class TestSearchByPosition(TestCase):

    POSITION = 10

    def setUp(self) -> None:
        self.search = SearchByPosition(type(self).POSITION)

    def tearDown(self) -> None:
        del self.search

    def test_search_field(self):
        query, option = self.search.search_field()
        expected = {'position': type(self).POSITION}
        self.assertDictEqual(query, expected)
        expected = {'_id': 1}
        self.assertDictEqual(option, expected)

