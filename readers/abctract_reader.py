import string

from abc import ABC, abstractmethod
from nltk.tokenize import word_tokenize


class Reader(ABC):

    @abstractmethod
    def get_image(self, path_book: str):
        ...

    @abstractmethod
    def read(self) -> dict:
        ...

    def tokenize(self, content: str) -> list:
        # Remove punctuation using str.translate()
        translator = str.maketrans('', '', string.punctuation)
        text_no_punct = content.translate(translator)

        # Tokenize the text into words using NLTK
        words = word_tokenize(text_no_punct)

        # Print the list of words
        return words

    def read_and_tokenize(self) -> dict:
        data = self.read()
        if not data:
            return None

        tokenize_book = self.tokenize(data["content"])
        data["tokenize_book"] = tokenize_book
        return data



