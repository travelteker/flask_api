

class SearchByPosition:

    """Generate query to search by position"""

    def __init__(self, position: int):
        self.__position = position

    def search_field(self):
        query = {'position': self.__position}
        options = {'_id': 1}
        return query, options
