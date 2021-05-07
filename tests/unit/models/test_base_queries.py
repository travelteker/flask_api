from unittest import TestCase
from unittest.mock import Mock

from app.models.base_queries import BaseQueries


class TestBaseQueries(TestCase):

    def setUp(self) -> None:
        self.mock_collection = Mock()
        self.base = BaseQueries(self.mock_collection)

    def tearDown(self) -> None:
        del self.mock_collection
        del self.base

    def test_find_one(self):
        query_expected = {}
        options_expected = {}
        self.base.find_one(query_expected)
        self.assertTrue(self.mock_collection.find_one.called_with(query_expected, options_expected))

    def test_find(self):
        query_expected = {}
        options_expected = {}
        self.base.find(query_expected)
        self.assertTrue(self.mock_collection.find_one.called_with(query_expected, options_expected))

    def test_delete_one(self):
        query_expected = {}
        options_expected = {}
        self.base.delete_one(query_expected)
        self.assertTrue(self.mock_collection.find_one.called_with(query_expected, options_expected))



