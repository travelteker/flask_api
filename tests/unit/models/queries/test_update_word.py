from unittest import TestCase

from app.models.queries.update_word import UpdateWord


class TestUpdateWord(TestCase):

    def test_search_field_new_greater_than(self):
        current = 1
        new = 5
        update_word = UpdateWord(current, new)
        query, position = update_word.search_field()
        query_expected = {'position': {'$gt': current, '$lte': new}}
        position_expected = {'_id': 1, 'position': 1, 'word': 1}
        self.assertDictEqual(query, query_expected)
        self.assertDictEqual(position, position_expected)

    def test_search_field_new_less_than(self):
        current = 5
        new = 1
        update_word = UpdateWord(current, new)
        query, position = update_word.search_field()
        query_expected = {'position': {'$gte': new, '$lt': current}}
        position_expected = {'_id': 1, 'position': 1, 'word': 1}
        self.assertDictEqual(query, query_expected)
        self.assertDictEqual(position, position_expected)

    def test_search_field_equals(self):
        current = 3
        new = 3
        update_word = UpdateWord(current, new)
        query, position = update_word.search_field()
        query_expected = {'position': {'$gte': new, '$lt': current}}
        position_expected = {'_id': 1, 'position': 1, 'word': 1}
        self.assertDictEqual(query, query_expected)
        self.assertDictEqual(position, position_expected)
