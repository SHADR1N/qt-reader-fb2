from PySide6.QtCore import QSettings

import icon_rc

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from frames import RootScreen


class Reader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setting = QSettings("Reader", "App")
        self.setCentralWidget(RootScreen(self))


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QPixmap(u":/icon/icon.png"))

    reader = Reader()
    reader.setWindowTitle("BookReader by SHADRIN")
    reader.setMinimumSize(400, 300)
    reader.show()

    app.exec()
