from collections import Counter
from typing import List, Optional
from pymongo.cursor import Cursor


class Anagrams:

    @staticmethod
    def get_coincidences(word: str, data: list) -> list:
        """Method to get all coincidences for anagrams using a word reference and searching into a container
        :params reference: (str) It is a word used to detect anagramas
        :params data: (list) Container with words that will be used to detect anagrams
        """
        return data if not data else list(filter(lambda x: (Counter(word) == Counter(x)), data))

    @staticmethod
    def unique_list_same_order(data: list) -> list:
        """Find unique elements in list creating a new list with the same order that original list without duplicates
        :params data: (list) Container with elements that it's necessary filter
        :return: (list) Container with all unique elements
        """
        unique = []
        for word in data:
            if word in unique:
                continue
            else:
                unique.append(word)
        return unique

    @staticmethod
    def remove_item_in_list(item: str, container: Optional[Cursor]) -> List[str]:
        """Compare items from Cursor and save in a list"""
        output = []
        for register in container:
            word = register.get('word')
            if word != item:
                output.append(word)
        return output
