from os import getenv

from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import abort

from app.models.words import Words
from app.schemas.word import WordSchema
from app.utils.conditions.word_repeated import WordRepeated
from app.utils.filters.anagrams import Anagrams
from app.utils.responses.structures.success import Success


tags = Blueprint('tags', __name__, url_prefix='/words')


@tags.route('/', methods=['GET'])
def index():
    try:
        model = Words()
        words = model.get_words()
        return Success.response(words)
    except Exception as err:
        message = f'Endpoint </words/> method <GET> failure|description: {err}'
        abort(500, message)


@tags.route('/', methods=['POST'])
def insert():
    try:
        body = request.get_json(force=True)
        schema = WordSchema()
        data = schema.load(body)
        word = data.word
        position = data.position
        model = Words()
        WordRepeated.exit(model, data.word)
        model.add_word(word, position)
        return Success.response({'word': data.word, 'position': data.position}, 201)
    except ValidationError as err:
        abort(400, str(err))
    except Exception as err:
        status, message, *extra = str(err).split(':')
        status, *others = status.split(' ')
        abort(int(status), message)


@tags.route('/<word>', methods=['PATCH'])
def update(word: str):
    try:
        body = request.get_json(force=True)
        body.update({'word': word})
        schema = WordSchema()
        data = schema.load(body)
        model = Words()
        internal_process = model.update_word(data.word, data.position)
        if not internal_process.operation:
            abort(400, internal_process.message)
        return Success.response({'word': data.word, 'position': data.position})
    except ValidationError as err:
        abort(400, str(err))


@tags.route('/<tag>', methods=['DELETE'])
def delete(tag: str):
    Words().delete_word(tag)
    return Success.response(code=204)


@tags.route('/reset', methods=['DELETE'])
def reset():
    registers = Words().reset_collection_data()
    if registers is None:
        registers = 0
    return Success.response(['Operation reset successfully', registers], 205)


@tags.route('<word>/anagrams', methods=['GET'])
def anagram(word: str):
    try:
        container = Words().get_anagrams(word)
        if not container:
            return Success.response(container)
        anagrams = Anagrams.get_coincidences(word, container)
        if bool(int(getenv('WILL_HAVE_WORDS_REPETEAD', 0))):
            anagrams = Anagrams.unique_list_same_order(anagrams)
        return Success.response(data=anagrams)
    except Exception as err:
        message = f'Endpoint </word/anagrams> method <GET> failure|description: {err}'
        abort(500, message)
