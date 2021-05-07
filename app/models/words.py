from datetime import datetime
from typing import Optional
from pymongo import UpdateOne, InsertOne

from app.models import mongo_db
from app.models.base_queries import BaseQueries
from app.models.queries.search_by_word import SearchByWord
from app.models.queries.update_word import UpdateWord
from app.models.structures.word_document import WordDocument
from app.models.transactions import Transactions
from app.utils.filters.anagrams import Anagrams
from app.utils.logger.base_logger import BaseLogger
from app.models.queries.search_words import SearchWords
from app.models.queries.search_by_position import SearchByPosition
from app.utils.responses.structures.internal_process import InternalProcess


class Words(BaseQueries):

    """Model to manage <words> for blueprint <tags>"""

    DEFAULT_FIELD_ORDER = 'position'
    DEFAULT_ORDER = 1

    def __init__(self):
        self.__module = type(self).__name__
        self.collection = mongo_db.db.tags
        self.__client = mongo_db.cx
        self.__logger = BaseLogger().create_logger(self.__module, 'words.log')
        self.__transaction = Transactions()
        super().__init__(self.collection)

    def get_words(self, query: dict = None, order_field: str = 'position', order: int = 1) -> list:
        """Action to recieved <words> from mongo databse
        :params query: (dict) Conditions to execute query
        :params oder_field: (str) Field used to order results
        :params order: (int) Value to indicate ASC or DESC ordenation
        :return: (list) Container with words found
        """
        extract_words = []
        if query is None:
            query = {}
        container = self.collection.find(query).sort(order_field, order)
        for item in container:
            word = item.get('word')
            extract_words.append(word)
        self.__logger.info(f'{self.__module}|get_words()|extract_words: {extract_words}')
        return extract_words

    def get_anagrams(self, anagram: str) -> list:
        """Action to recieved <words> which have the same characters that word of reference. It will be excluded
        of this container the word used like reference.
        :params anagram: (str) Word used like reference to matching the same characters
        :return: (list) Container with words found matching with word reference
        """
        query = {'word': {'$exists': True}, '$expr': {'$eq': [{'$strLenCP': '$word'}, len(anagram)]}}
        position = type(self).DEFAULT_FIELD_ORDER
        order = type(self).DEFAULT_ORDER
        container = self.collection.find(query).sort(position, order)
        output = Anagrams.remove_item_in_list(anagram, container)
        return output

    def add_word(self, word: str, position: int) -> InternalProcess:
        """Action to insert <word> in database.
        :params word: (str) Word to insert in database
        :params position: (int) Position used for word
        :return: (InternalProcess) Dataclass to indicate if action was successfully or not
        """
        query, options = SearchWords.seeker(SearchByPosition(position))
        bulk_api = []
        if self.find_one(query, options):
            # Get all words by position greater or equal than position detected
            # for conditions in self.__get_positions_range(position):
            for conditions in self.__get_words_by('position', {'$gte': position}):
                oid, new_value = conditions
                bulk_api.append(UpdateOne(oid, new_value))
        register_time = datetime.now()
        iterable = {
            'word': word,
            'position': position,
            'created_at': register_time,
            'modify_at': register_time
        }
        bulk_api.append(InsertOne(iterable))
        return self.__transaction.execute_transaction(self.collection, bulk_api)

    def __get_words_by(self, field: str, criteria: dict, order: int = 1):
        """Method to obtain all <words> in collection with a criteria and order
        :params field: (str) Name field used in query to search by that field
        :params criteria: (dict) Extra information used in query to search words
        :params order: (int) Flag to indicate ordenation criteria, ASC or DESC
        :return: (list) Data founds stored in a list structure
        """
        query = {field: criteria}
        options = {'_id': 1, 'position': 1}
        container = self.find(query, options)
        container_order = container.sort(field, order)
        new_positions = []
        for item in container_order:
            oid = {'_id': item.get('_id')}
            new_value = {'$set': {
                'position': item.get('position') + 1,
                'modify_at': datetime.now()
            }}
            new_positions.append((oid, new_value))
        return new_positions

    def update_word(self, word: str, new_position: int) -> InternalProcess:
        """Action to update <word>. It is mandatory that word exists.
        :params word: (str) Word that will be updated in database
        :params new_positon: (int) New value for position
        :return: (InternalProcess) Dataclass to indicate if action was successfully or not
        """
        query_word, options_word = SearchWords.seeker(SearchByWord(word))
        data_word = self.find_one(query_word, options_word)
        if data_word is None:
            return InternalProcess(False, str(f'word <{word}> not found, update aborted'))
        oid_word = data_word.get('_id')
        current_position = data_word.get('position')
        doc = WordDocument(oid_word, word, new_position)

        # Checking if the new position it's not occupied. POSITION not exists in database
        query_position, options_position = SearchWords.seeker(SearchByPosition(new_position))
        availability = self.find_one(query_position, options_position)
        if availability is None:
            # Update word with new position
            oid = {'_id': oid_word}
            new_value = {'$set': {'position': new_position, 'modify_at': datetime.now()}}
            self.collection.update_one(oid, new_value)
            return InternalProcess(True)
        if new_position == current_position:
            return InternalProcess(False, f'Update failure, current position and new position '
                                          f'are equal <{current_position}>')
        query, options = SearchWords.seeker(UpdateWord(current_position, new_position))
        words_permutation = self.find(query, options)
        # Checking permutations ASCENDENT or DESCENDENT
        counter = -1 if new_position > current_position else 1
        request_api = []
        for word in words_permutation:
            request_api.append(UpdateOne({'_id': word.get('_id')}, {'$inc': {'position': counter}}))
        oid_update_word = {'_id': doc.id}
        new_value_update_word = {'$set': {'position': doc.position, 'modify_at': datetime.now()}}
        request_api.append(UpdateOne(oid_update_word, new_value_update_word))
        return self.__transaction.execute_transaction(self.collection, request_api)

    def delete_word(self, word: str) -> InternalProcess:
        """Action to delete an specific document in the collection if exists
        :params word: (str) Word will be deleted
        :return: (InternalProcess) Data structure containing information about operation
        """
        query = {'word': word}
        options = {'_id': 1}
        check = self.find_one(query, options)
        if check is None:
            return InternalProcess(False, f'Word <{word}> not found, aborting action delete')
        output = self.delete_one({'_id': check.get('_id')})
        total_register_delete = output.deleted_count
        return InternalProcess(True, f'Word <{word}> delete succesfully: {total_register_delete}')

    def reset_collection_data(self) -> Optional[int]:
        """Action to reset all documents in the collection
        :return: Optional[int] Total collectiones droped
        """
        query = {}
        operation = self.collection.remove(query)
        registers_delete = operation.get('n')
        return registers_delete

