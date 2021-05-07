from typing import Any


class SearchWords:

    """Class to apply conditions to generate queries"""

    @staticmethod
    def seeker(query: Any):
        return query.search_field()

