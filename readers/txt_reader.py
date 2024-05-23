import os
import os.path
import nltk
import ssl

from utils import BookNotFound
from readers.abctract_reader import Reader

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')


class TXTReader(Reader):
    def __init__(self, path_book: str):
        self.path_book = path_book

    def get_image(self, root):
        return None

    def read(self):
        if os.path.exists(self.path_book):
            with open(self.path_book, "r", encoding="utf-8") as fl:
                book_content = fl.read()

            return {"title": "Unknown", "author": "Unknown", "content": book_content, "image": None}
        else:
            raise BookNotFound()


