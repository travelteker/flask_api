from unittest import TestCase
from unittest.mock import Mock

from app.models.queries.search_words import SearchWords


class TestSearchWords(TestCase):

    def test_seeker(self):
        query = Mock()
        SearchWords.seeker(query)
        self.assertTrue(query.search_field.called)
