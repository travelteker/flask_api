from os import getenv
from typing import Any

from werkzeug.exceptions import abort

from app.models.queries.search_words import SearchWords
from app.models.queries.search_by_word import SearchByWord


class WordRepeated:

    """Condition to manage operation flow working with words
    It's a criteria to decide if insert or not into collection mongo
    """

    @staticmethod
    def exit(model: Any, word: str):
        query, options = SearchWords.seeker(SearchByWord(word))
        data = model.find_one(query, options)
        if not bool(int(getenv('WILL_HAVE_WORDS_REPETEAD', 0))) and data:
            abort(400, f'Already exists word <{word}>, aborting process')
