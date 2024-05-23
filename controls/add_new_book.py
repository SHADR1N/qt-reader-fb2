import os
import shutil

from PySide6.QtWidgets import QFileDialog, QFrame, QPushButton, QTabWidget


class ControlsBook:

    def __init__(self, parent):
        self.parent: QFrame = parent

        for button in self.parent.findChildren(QPushButton, "AddBook"):
            button.clicked.connect(self.open)

    def open(self):
        file_path = QFileDialog.getOpenFileName(
            self.parent,
            caption="Выберите книгу",
            filter="Book (*.fb2 *.txt)"
        )
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
        self.parent.loader.fetching_books()
