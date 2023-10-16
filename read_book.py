import os
import os.path
import time
import xml.etree.ElementTree as ET
import base64
import string
import nltk

from nltk.tokenize import word_tokenize

nltk.download('punkt')  # Download the necessary data for NLTK (only needs to be done once)


class BookNotFound(Exception):
    def __init__(self):
        super().__init__()


class ReaderBook:
    def __init__(self, path_book: str):
        self.path_book = path_book

    def get_image(self, root):
        # Extract image
        coverpage = root.findall(".//{http://www.gribuser.ru/xml/fictionbook/2.0}binary")
        if coverpage:
            coverpage = coverpage[-1].text
        else:
            return None

        # Your Base64-encoded image data as a string
        base64_image_data = coverpage

        # Decode the Base64 string
        image_data = base64.b64decode(base64_image_data)
        return image_data

    def read(self):
        if os.path.exists(self.path_book):
            tree = ET.parse(self.path_book)
            root = tree.getroot()

            # Extract book title
            book_title = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}book-title").text

            # Extract author's first name
            author = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}first-name").text
            author += root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}last-name").text

            image = self.get_image(root)

            # Extract book content (assuming it's within the <section> element)
            content = []
            for section in root.findall(".//{http://www.gribuser.ru/xml/fictionbook/2.0}section"):
                for paragraph in section.findall(".//{http://www.gribuser.ru/xml/fictionbook/2.0}p"):
                    if paragraph.text:
                        content.append(paragraph.text)

            # Join the content paragraphs into a single string
            book_content = "\n".join(content)

            return {"title": book_title, "author": author, "content": book_content, "image": image}
        else:
            raise BookNotFound()

    def tokenaize(self, content: str):
        # Remove punctuation using str.translate()
        translator = str.maketrans('', '', string.punctuation)
        text_no_punct = content.translate(translator)

        # Tokenize the text into words using NLTK
        words = word_tokenize(text_no_punct)

        # Print the list of words
        return words

    def read_and_tokenize(self):
        data = self.read()
        tokenize_book = self.tokenaize(data["content"])
        data["tokenize_book"] = tokenize_book
        return data


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    book = ReaderBook("books/StrageLife.fb2").read_and_tokenize()

    word_peer_min = 300
    timeout = 60 / word_peer_min

    print(len(book["tokenize_book"]) / word_peer_min)
    for w in book["tokenize_book"]:
        print(w)
        time.sleep(timeout)
        clear()
