from readers.abctract_reader import Reader
import os
import os.path
import base64
import nltk
import ssl
import xml.etree.ElementTree as ET

from utils import BookNotFound

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')


class FBReader(Reader):

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
            try:
                tree = ET.parse(self.path_book)
            except:
                print(f"Не смог загрузить: {self.path_book}")
                return

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


