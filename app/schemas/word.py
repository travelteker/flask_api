from marshmallow import Schema, fields, post_load


class Word:

    """Class to parameterize structure data received by HTTP"""

    def __init__(self, word: str, position: int):
        self.word = word
        self.position = position


class WordSchema(Schema):

    """Validation class"""

    word = fields.String(required=True)
    position = fields.Integer(required=True)

    @post_load
    def create_word(self, data, **kwargs):
        return Word(**data)

