from typing import Any, Optional, Union

from pymongo.cursor import Cursor


class BaseQueries:

    """Class to centralize commons method to manipulate database mongo"""

    def __init__(self, collection: Any):
        self.__collection = collection

    def find_one(self, query: dict, options: Optional[dict] = None) -> Union[None, dict, Cursor]:
        if options is None:
            options = {}
        return self.__collection.find_one(query, options)

    def find(self, query: dict, options: Optional[dict] = None) -> Union[None, dict, Cursor]:
        if options is None:
            options = {}
        return self.__collection.find(query, options)

    def delete_one(self, query: dict, options: Optional[dict] = None):
        if options is None:
            options = {}
        return self.__collection.delete_one(query, options)

