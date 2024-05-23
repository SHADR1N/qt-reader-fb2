from PySide6.QtWidgets import QTabWidget

from frames.labrary_screen import LibraryScreen
from frames.read_screen import ReadScreen


class RootScreen(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.core = parent
        self.build()

    def build(self):
        self.currentChanged.connect(self.pause_read)
        self.addTab(
            ReadScreen(self), "Reader"
        )
        self.addTab(
            LibraryScreen(self), "Library"
        )

    def pause_read(self):
        reader = self.findChild(ReadScreen)
        reader.pause()

    def read(self, data_book: dict):
        reader = self.findChild(ReadScreen)
        reader.data_book = data_book
        reader.update()
        self.setCurrentWidget(reader)



