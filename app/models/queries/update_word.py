

class UpdateWord:

    """Generate query to search by position with filters"""

    def __init__(self, current_position: int, new_position: int):
        self.__current = current_position
        self.__new = new_position

    def search_field(self):
        query = {'position': {'$gte': self.__new, '$lt': self.__current}}
        if self.__new > self.__current:
            query = {'position': {'$gt': self.__current, '$lte': self.__new}}
        options = {'_id': 1, 'position': 1, 'word': 1}
        return query, options
