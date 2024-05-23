from functools import partial

from PySide6.QtCore import QSize, Qt, QSettings
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from controls import LoaderBooks, ControlsBook
from widgets import FlowScrollArea


class LibraryScreen(QFrame):
    flow_area: FlowScrollArea

    def __init__(self, parent=None):
        super().__init__(parent)
        self.render_widget()
        self.setting = self.parent().parent().setting
        self.fetcher_books = ControlsBook(self)

        self.loader = LoaderBooks(self)
        self.loader.fetching_books()

    def render_widget(self):
        vertical = QVBoxLayout()

        tools_layout = QHBoxLayout()

        add_book = QPushButton()
        add_book.setObjectName("AddBook")
        add_book.setText("Добавить книгу")

        tools_layout.addWidget(add_book, alignment=Qt.AlignmentFlag.AlignLeft)

        self.flow_area = FlowScrollArea(self)

        vertical.addLayout(tools_layout)
        vertical.addWidget(self.flow_area)
        self.setLayout(vertical)

    @staticmethod
    def __get_image(image):

        image_book = QLabel()
        image_book.setObjectName(u"label_4")
        if image:
            image_book.setScaledContents(True)
            image_book.setAlignment(Qt.AlignCenter)
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            image_book.setPixmap(pixmap)
            image_book.setScaledContents(True)
        else:
            image_book.setStyleSheet("background: gray;")

        return image_book

    def add_book(self, data_book: dict):
        card_book = QFrame()
        card_book.setObjectName(u"card_book")
        card_book.setFixedSize(QSize(150, 250))

        vertical_layout = QVBoxLayout()
        image_book = self.__get_image(data_book["image"])

        progress_book = QLabel()
        total_words = len(data_book["tokenize_book"])
        has_read = int(self.setting.value(data_book["title"], 0))
        percent_progress = (has_read / total_words) * 100 if total_words > 0 else 0
        progress_book.setText(f"{int(percent_progress)}%")

        open_book = QPushButton(card_book)
        open_book.setObjectName(u"openBook")
        open_book.clicked.connect(partial(self.parent().read, data_book))
        open_book.setText("Читать")
        open_book.setCursor(QCursor(Qt.PointingHandCursor))

        vertical_layout.addWidget(image_book)
        vertical_layout.addWidget(progress_book)
        vertical_layout.addWidget(open_book)
        card_book.setLayout(vertical_layout)

        self.flow_area.addWidget(card_book)

