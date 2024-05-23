from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QScrollArea

from widgets import FlowLayout


class FlowScrollArea(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.disableAutoscroll = False
        self.initWidget()

    def addWidget(self, widget: QFrame):
        self.layerAreaMessage.addWidget(widget)

    def initWidget(self):
        self.layer = QVBoxLayout()
        self.layer.setContentsMargins(0, 0, 0, 0)
        self.layer.setSpacing(0)
        self.setLayout(self.layer)
        self.setContentsMargins(0, 0, 0, 0)

        self.areaMessage = QScrollArea(self)
        self.areaMessage.horizontalScrollBar().setVisible(False)
        self.areaMessage.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.areaMessage.setWidgetResizable(True)

        widget = QFrame(parent=self)
        self.layerAreaMessage = FlowLayout(self)
        widget.setLayout(self.layerAreaMessage)
        self.areaMessage.setWidget(widget)

        self.layer.addWidget(self.areaMessage)


