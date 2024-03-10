import os
import shutil
import sys
import time
import icon_rc

from functools import partial
from typing import Union

from mainUI import Ui_MainWindow
from read_book import ReaderBook, ReaderBookTXT

from PySide6.QtWidgets import (
    QMainWindow, QLabel, QApplication, QVBoxLayout, QPushButton, QGridLayout, QWidget, QScrollArea, QFileDialog
)
from PySide6.QtCore import Signal, QThread, QSize, Qt, QSettings, QTimer
from PySide6.QtGui import QPixmap, QCursor, QFont


class TileWidget(QWidget):
    def __init__(self, parent=None, callback_resize=None):
        super().__init__(parent=parent)
        self.setObjectName(u"gridLayout")
        self.callback_resize = callback_resize

        self.lay = QVBoxLayout()

        self.setContentsMargins(0, -1, -1, -1)

        self.scroll_area = QScrollArea()
        self.scroll_area.setObjectName(u"cardsMap")
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.grid = QGridLayout()
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.grid)

        self.scroll_area.setWidget(self.scroll_widget)
        self.lay.addWidget(self.scroll_area, 1)
        self.setLayout(self.lay)

    def resizeEvent(self, event):
        self.callback_resize()


class QtBookReader(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.current_book = None
        self.books = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initReader()
        self.setStyleSheet("""
            * {
                background: black;
                color: white;
            }
            QToolButton {
                background: #dbdbdb;
                border: 1px solid white;
                border-radius: 3px;
                color: background;
                width: 100px;
            }
            #label, #label_2, #label_3, #label_4 {
                color: white;    
            }
            
            #toolButton, #toolButton_2, #toolButton_3, #toolButton_4, #toolButton_5, #toolButton_6, #toolButton_7 {
                background: none;
                border: 0px solid #fff;
                width: 30px;
                height: 30px;
            }
        
            #toolButton:hover, #toolButton_2:hover, #toolButton_3 :hover, #toolButton_4 :hover, #toolButton_5 :hover, 
            #toolButton_6:hover, #toolButton_7:hover {
                width: 30px;
                height: 30px;
            }
            
            QPushButton#openBook {
                border: 1px solid #464C55;
                border-radius: 6px;
                padding: 3px;
                background: #DFF0FE;
                }
            
            QPushButton#openBook:hover {
                border: 1px solid #464C55;
                background: #98CCFD;
            }
            
            #cardsMap {
                border: 0px solid #fff;
                background: none;
            }
            
            QScrollBar:vertical {
                border-right: 1px solid white;
                
                background: black;
                width: 5px;
                margin: 0px;
                padding-right: 1px;
            }
            
            QScrollBar::handle:vertical {
                background: white;
                padding: 0px;
                border: 1px solid #fff;
                border-radius: 2px;
            }
            
            QScrollBar::add-line:vertical {
                height: 0px;
            }
            
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
                width: 26px;
                height: 26px;
                background: none;
            }
            
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        QTimer.singleShot(0, self.initBook)

    def reset_book(self):
        self.thr.stop()
        self.setting.setValue(self.current_book["title"], 0)
        self.open_book(self.current_book)

    def bindButton(self):
        self.ui.toolButton.clicked.connect(self.thr.stop)  # Pause
        self.ui.toolButton_2.clicked.connect(self.reset_book)  # Stop
        self.ui.toolButton_3.clicked.connect(self.thr.start)  # Run
        self.ui.toolButton_4.clicked.connect(self.copy_book_to_dir)
        self.ui.toolButton_5.clicked.connect(self.open_setting)
        self.ui.pushButton.clicked.connect(self.save_setting)

    def open_setting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.setting)
        word_peer_minutes = self.setting.value("word_peer_minutes", str(300))
        font_size = self.setting.value("font_size", str(24))
        self.ui.spinBox.setValue(int(word_peer_minutes))
        self.ui.spinBox_2.setValue(int(font_size))

    def save_setting(self):
        wpm = self.ui.spinBox.text()
        self.setting.setValue("word_peer_minutes", str(wpm))

        fs = self.ui.spinBox_2.text()
        self.setting.setValue("font_size", str(fs))

        font_size = self.setting.value("font_size", str(24))

        font = QFont()
        font.setPointSize(int(font_size))

        self.ui.label_2.setFont(font)

    def change_content(self):
        key = self.current_book["title"]
        step = self.setting.value(key, 0)
        self.setting.setValue(key, str(int(step) + 1))

        self.ui.label_2.setText(self.current_book["tokenize_book"][int(step) + 1])
        self.ui.label_3.setText(str(int(step) + 1) + "/" + str(len(self.current_book["tokenize_book"])))

    def resizeEventGrid(self, *args):
        if not self.books:
            return

        width = self.width()
        button_width = 150
        columns = width // (button_width + 10)  # 10 is for spacing

        self.delete_book()

        for i, button in enumerate(self.books):
            if columns == 0:
                self.gridLayout.grid.addWidget(button, 0, i)
                continue

            row = i // columns
            col = i % columns
            self.gridLayout.grid.addWidget(button, row, col)

    def open_book(self, data_book: dict):
        self.current_book = data_book
        self.ui.stackedWidget.setCurrentWidget(self.ui.readBook)
        self.change_book_data(data_book)
        word_peer_minutes = self.setting.value("word_peer_minutes", str(300))
        timeout = 60 / int(word_peer_minutes)

        self.thr.setInterval(timeout * 1000)
        self.setting.setValue("timeout", timeout)

        all_words = len(data_book["tokenize_book"])
        readed_book = int(self.setting.value(data_book["title"], 0))
        delay = (all_words - readed_book) / int(word_peer_minutes)

        self.ui.label_4.setText(f"Примерное время чтения: {int(delay)} мин.")

    def change_book_data(self, data_book):
        start_word = self.setting.value(data_book["title"], 0)

        self.ui.label.setText(data_book["title"])
        self.ui.label_2.setText(data_book["tokenize_book"][0])
        self.ui.label_3.setText(str(start_word) + "/" + str(len(data_book["tokenize_book"])))

    def copy_book_to_dir(self):
        file_path = QFileDialog.getOpenFileName(self, caption="Выберите книгу .fb2", filter="FB2 (*.fb2, *.txt)")
        if file_path[0]:

            extension = ".fb2" if file_path[0].endswith(".fb2") else ".txt"
            file_dir = os.path.join(
                    "books",
                    os.path.splitext(
                        os.path.basename(file_path[0])
                    )[0] + extension
                )
            if os.path.exists(file_dir):
                return

            shutil.copy(
                file_path[0],
                file_dir
            )
            self.update_books()

    def update_books(self):
        self.initBook()
        self.resizeEventGrid()

    def delete_book(self, book=None, clear=True):
        if not book:
            for button in self.books:
                self.gridLayout.grid.removeWidget(button)
                del button

            if not clear:
                self.books = []
        else:
            self.gridLayout.grid.removeWidget(book)
            self.books.remove(book)
            del book

    def add_book(self, title, image, index, data_book):
        card_book = QWidget(self.ui.mainMenu)
        card_book.setObjectName(u"card_book")
        card_book.setFixedSize(QSize(150, 250))

        self.ui.verticalLayout_5 = QVBoxLayout(card_book)
        self.ui.verticalLayout_5.setObjectName(u"verticalLayout_5")

        label_4 = QLabel(card_book)
        label_4.setObjectName(u"label_4")
        if image:
            label_4.setScaledContents(True)
            label_4.setAlignment(Qt.AlignCenter)
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            label_4.setPixmap(pixmap)
            label_4.setScaledContents(True)
        else:
            label_4.setStyleSheet("background: gray;")

        self.ui.verticalLayout_5.addWidget(label_4)

        pushButton = QPushButton(card_book)
        pushButton.setObjectName(u"openBook")
        pushButton.setText("Читать")
        pushButton.clicked.connect(partial(self.open_book, data_book))
        pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.ui.verticalLayout_5.addWidget(pushButton)

        self.gridLayout.grid.addWidget(card_book, index // 3, index % 3)
        self.resizeEventGrid(None)
        self.books.append(card_book)

        card_book.show()
        self.gridLayout.update()

    def initReader(self):
        self.gridLayout = TileWidget(self.ui.mainMenu, self.resizeEventGrid)
        self.ui.verticalLayout_6.addWidget(self.gridLayout)
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainMenu)
        self.ui.toolButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mainMenu))
        self.ui.toolButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mainMenu))

        self.setting = QSettings("Reader", "App")
        font_size = self.setting.value("font_size", str(24))

        font = QFont()
        font.setPointSize(int(font_size))

        self.ui.label_2.setFont(font)

        self.thr = QTimer(self)
        self.thr.timeout.connect(self.change_content)
        self.bindButton()

    def initBook(self):
        self.books = []
        if not os.path.exists("books"):
            os.mkdir("books")

        book = [b for b in os.listdir("books") if b.endswith(".fb2") or b.endswith(".txt")]
        for index, book_path in enumerate(book):
            if book_path.endswith(".fb2"):
                book = ReaderBook("books/" + book_path).read_and_tokenize()
            else:
                book = ReaderBookTXT("books/" + book_path).read_and_tokenize()

            if not book:
                continue

            book["path_book"] = "books/" + book_path
            self.add_book(book["title"], book["image"], index, book)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap(u":/icon/icon.png"))

    main = QtBookReader()

    # Properties window
    main.setWindowTitle("QtBookReader by SHADRIN")
    main.setMinimumSize(QSize(400, 300))

    main.show()

    sys.exit(app.exec())
