

class SearchByWord:

    """Generate query to search by word"""

    def __init__(self, word: str):
        self.__word = word

    def search_field(self):
        query = {'word': self.__word}
        options = {'_id': 1, 'position': 1}
        return query, options
