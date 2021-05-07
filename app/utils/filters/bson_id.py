from bson.objectid import ObjectId


class BsonId:

    """Method to casting fields of data received from mongodb and show in a readable format"""

    def __init__(self):
        self.__module = type(self).__module__

    @staticmethod
    def casting_fields(container: list) -> list:
        result = []
        for element in container:
            oid = ObjectId(element.get('_id'))
            created_at = element.get('created_at')
            modify_at = element.get('modify_at')
            if created_at:
                element.update({'created_at': str(created_at)})
            if modify_at:
                element.update({'modify_at': str(modify_at)})
            element.update({'_id': str(oid)})
            result.append(element)
        return result

