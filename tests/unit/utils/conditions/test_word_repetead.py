from os import environ
from unittest import TestCase, mock

from app.utils.conditions.word_repeated import WordRepeated


class TestWordRepeated(TestCase):

    @mock.patch.dict(environ, {'WILL_HAVE_WORDS_REPETEAD': '0'})
    @mock.patch('app.utils.conditions.word_repeated.abort')
    def test_exit(self, mock_abort):
        model = mock.Mock()
        model.find_one.return_value = ['found']
        word = 'fake'
        WordRepeated.exit(model, word)
        self.assertTrue(model.find_one.called)
        code = 400
        message = f'Already exists word <{word}>, aborting process'
        self.assertTrue(mock_abort.called_with_once(code, message))
