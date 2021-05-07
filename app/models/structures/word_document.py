from dataclasses import dataclass

from bson import ObjectId


@dataclass
class WordDocument:

    """Interface DAO to manipulate structure data"""

    id: ObjectId
    word: str
    position: int

