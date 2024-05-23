from PySide6.QtWidgets import QLayout, QSizePolicy
from PySide6.QtCore import Qt, QSize, QRect, QPoint


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super().__init__()
        self.core_parent = parent

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if 0 <= index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        space_x = 0
        spacing = self.spacing()
        line_items = []  # List to hold items for each line

        for item in self.itemList:
            style = item.widget().style()
            layout_spacing_x = style.layoutSpacing(
                QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal
            )
            layout_spacing_y = style.layoutSpacing(
                QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical
            )
            space_x = spacing + layout_spacing_x
            space_y = spacing + layout_spacing_y
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                # Center the items in the current line
                line_width = x - rect.x() - space_x  # Subtract the last spacing
                line_x = rect.x() + (rect.width() - line_width) // 2
                for line_item in line_items:
                    line_item_width = line_item.sizeHint().width()
                    line_item.setGeometry(QRect(QPoint(line_x, y), line_item.sizeHint()))
                    line_x += line_item_width + space_x
                line_items.clear()
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                line_items.append(item)

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        # Center the remaining items in the last line
        if line_items:
            line_width = x - rect.x() - space_x  # Subtract the last spacing
            line_x = rect.x() + (rect.width() - line_width) // 2
            for line_item in line_items:
                line_item_width = line_item.sizeHint().width()
                line_item.setGeometry(QRect(QPoint(line_x, y), line_item.sizeHint()))
                line_x += line_item_width + space_x

        return y + line_height - rect.y()

