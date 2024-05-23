import os

from readers import FBReader, TXTReader


class LoaderBooks:

    def __init__(self, parent):
        self.books = []
        self.parent = parent

    def fetching_books(self):
        if not os.path.exists("books"):
            os.mkdir("books")

        book = [b for b in os.listdir("books") if b.endswith(".fb2") or b.endswith(".txt")]
        for index, book_path in enumerate(book):
            if book_path.endswith(".fb2"):
                book = FBReader("books/" + book_path).read_and_tokenize()
            else:
                book = TXTReader("books/" + book_path).read_and_tokenize()

            if not book:
                continue

            book["path_book"] = "books/" + book_path
            for _ in range(10):
                self.parent.add_book(book)


