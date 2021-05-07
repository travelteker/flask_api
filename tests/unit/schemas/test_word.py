from unittest import TestCase
from unittest.mock import Mock

from app.schemas.word import WordSchema


class TestWordSchema(TestCase):

    def test_create_word_success(self):
        data = {'word': 'dummy', 'position': 0}
        schema = WordSchema()
        validate_word = schema.load(data)
        result_word = validate_word.word
        result_position = validate_word.position
        self.assertEqual(data.get('word'), result_word)
        self.assertEqual(data.get('position'), result_position)

    def test_create_word_failure(self):
        pass