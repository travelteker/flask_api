from unittest import TestCase, mock

from pymongo.errors import BulkWriteError

from app.models.words import Words
from app.utils.responses.structures.internal_process import InternalProcess


class TestWords(TestCase):

    @mock.patch('app.models.words.Transactions')
    @mock.patch('app.models.words.BaseLogger')
    @mock.patch('app.models.words.mongo_db.cx')
    @mock.patch('app.models.words.mongo_db.db')
    def setUp(self, mock_mongo_db, mock_mongo_cx, mock_transactions, mock_logger) -> None:
        self.words = Words()

    def tearDown(self) -> None:
        del self.words

    def test_get_words(self):
        collection = self.words.collection
        item = {'word': 'fake', 'position': 1}
        collection.find.return_value.sort.return_value = [item]
        output = self.words.get_words()
        expected = [item.get('word')]
        self.assertListEqual(expected, output)

    @mock.patch('app.models.words.Anagrams.remove_item_in_list')
    def test_get_anagrams(self, mock_remove):
        collection = self.words.collection
        item = {'word': 'fake', 'position': 1}
        collection.find.return_value.sort.return_value = [item]
        anagram = 'fake'
        self.words.get_anagrams(anagram)
        self.assertTrue(mock_remove.called)

    @mock.patch('app.models.words.InternalProcess')
    @mock.patch('app.models.words.UpdateOne')
    @mock.patch('app.models.words.InsertOne')
    @mock.patch('app.models.words.BaseQueries.find_one')
    def test_add_word(self, mock_find_one, mock_insert_one, mock_update_one, mock_internal):
        mock_find_one.return_value = [{'word': 'fake', 'position': 0}]
        collection = self.words.collection
        item = {'word': 'dummy', 'position': 111}
        collection.find.return_value.sort.return_value = [item]
        word = 'example'
        position = 1
        self.words.add_word(word, position)
        self.assertTrue(mock_update_one.called)
        self.assertTrue(mock_insert_one.called_once)
        self.assertTrue(mock_internal.called_once)

    @mock.patch('app.models.words.BaseQueries.find_one')
    def test_update_word_not_found_word(self, mock_find_one):
        mock_find_one.return_value = None
        word = 'dummy'
        position = 1
        output = self.words.update_word(word, position)
        self.assertTrue(mock_find_one.called)
        self.assertIsInstance(output, InternalProcess)

    @mock.patch('app.models.words.InternalProcess')
    @mock.patch('app.models.words.UpdateOne')
    @mock.patch('app.models.words.InsertOne')
    @mock.patch('app.models.words.BaseQueries.find_one')
    def test_update_word(self, mock_find_one, mock_insert_one, mock_update_one, mock_internal):
        mock_find_one.return_value = {'_id': 1000, 'word': 'fake', 'position': 0}
        collection = self.words.collection
        item = {'word': 'dummy', 'position': 111}
        collection.find.return_value.sort.return_value = [item]
        word = 'example'
        position = 1
        self.words.update_word(word, position)
        self.assertTrue(mock_update_one.called)
        self.assertTrue(mock_insert_one.called_once)
        self.assertTrue(mock_internal.called_once)

    def test_reset_collection(self):
        collection = self.words.collection
        collection.remove = mock.Mock()
        total_expected = 0
        collection.remove.return_value.get.return_value = total_expected
        output = self.words.reset_collection_data()
        self.assertEqual(output, total_expected)

    @mock.patch('app.models.words.BaseQueries.delete_one')
    @mock.patch('app.models.words.BaseQueries.find_one')
    def test_delete_word_failure(self, mock_fine_one, mock_delete_one):
        mock_fine_one.return_value = None
        word = 'dummy'
        output = self.words.delete_word(word)
        self.assertIsInstance(output, InternalProcess)
        self.assertFalse(output.operation)

    @mock.patch('app.models.words.BaseQueries.delete_one')
    @mock.patch('app.models.words.BaseQueries.find_one')
    def test_delete_word_success(self, mock_fine_one, mock_delete_one):
        word = 'dummy'
        mock_fine_one.return_value = {'_id': 1111, 'word': word, 'position':1}
        output = self.words.delete_word(word)
        self.assertIsInstance(output, InternalProcess)
        self.assertTrue(output.operation)

