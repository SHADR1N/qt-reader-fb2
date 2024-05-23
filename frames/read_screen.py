from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider, QSpinBox, QSpacerItem, \
    QSizePolicy


class ReadScreen(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setting = self.parent().parent().setting
        self.data_book: dict = {}
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.__update_row)

    def pause(self):
        self.__timer.stop()

    def play(self):
        self.__timer.start()

    def stop(self):
        self.setting.setValue(self.data_book["title"], 0)
        self.__timer.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:

            if self.__timer.isActive():
                self.pause()
            else:
                if self.data_book:
                    self.play()

        super().keyPressEvent(event)

    def update(self):
        super().update()
        self.__timer.stop()
        if self.data_book:
            delay, timeout = self.get_timings()

            self.__timer.setInterval(timeout * 1000)
            self.setting.setValue("timeout", timeout)

            vertical = QVBoxLayout()

            tools_button = QHBoxLayout()

            play = QPushButton("Начать")
            play.setAutoDefault(False)
            play.clicked.connect(self.play)

            pause = QPushButton("Пауза")
            pause.setAutoDefault(False)
            pause.clicked.connect(self.pause)

            stop = QPushButton("Стоп")
            stop.setAutoDefault(False)
            stop.clicked.connect(self.stop)

            label = QLabel("Слов в минуту")
            self.spin_box = QSpinBox()
            self.spin_box.setRange(1, 1000)
            self.spin_box.valueChanged.connect(self.change_speed)

            tools_button.addWidget(play, alignment=Qt.AlignmentFlag.AlignLeft)
            tools_button.addWidget(pause, alignment=Qt.AlignmentFlag.AlignLeft)
            tools_button.addWidget(stop, alignment=Qt.AlignmentFlag.AlignLeft)

            tools_button.addSpacerItem(QSpacerItem(
                40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
            ))

            tools_button.addWidget(label, alignment=Qt.AlignmentFlag.AlignRight)
            tools_button.addWidget(self.spin_box, alignment=Qt.AlignmentFlag.AlignRight)

            self.word_label = QLabel("...")
            font = QFont()
            font_size = self.setting.value("font_size", str(24))
            font.setPointSize(int(font_size))

            self.word_label.setFont(font)
            self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.duration_read = QLabel(f"Примерное время чтения: {int(delay)} мин.")
            self.duration_read.setAlignment(Qt.AlignmentFlag.AlignCenter)

            word_peer_minutes = self.setting.value("word_peer_minutes", str(300))
            self.slider = QSlider()
            self.slider.setOrientation(Qt.Orientation.Horizontal)
            self.slider.setValue(int(word_peer_minutes))
            self.slider.setRange(0, len(self.data_book["tokenize_book"]))

            self.slider.valueChanged.connect(self.hand_changer)

            vertical.addLayout(tools_button)
            vertical.addWidget(self.word_label, stretch=1)
            vertical.addWidget(self.duration_read, alignment=Qt.AlignmentFlag.AlignBottom)
            vertical.addWidget(self.slider, alignment=Qt.AlignmentFlag.AlignBottom)

            self.setLayout(vertical)

            play.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            pause.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            stop.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            self.spin_box.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            self.slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def get_timings(self):
        word_peer_minutes = self.setting.value("word_peer_minutes", str(300))
        timeout = 60 / int(word_peer_minutes)

        total_words = len(self.data_book["tokenize_book"])
        has_read = int(self.setting.value(self.data_book["title"], 0))
        delay = (total_words - has_read) / int(word_peer_minutes)
        return delay, timeout

    def change_speed(self, value: int):
        self.setting.setValue("word_peer_minutes", str(value))
        delay, timeout = self.get_timings()
        self.__timer.setInterval(timeout * 1000)

    def hand_changer(self, value: int):
        self.__timer.stop()

        key = self.data_book["title"]
        self.setting.setValue(key, str(int(value)))
        self.word_label.setText(self.data_book["tokenize_book"][int(value)])

        QTimer.singleShot(300, self.play)

    def __update_row(self):
        delay, _ = self.get_timings()

        key = self.data_book["title"]
        step = self.setting.value(key, 0)
        self.setting.setValue(key, str(int(step) + 1))

        self.slider.blockSignals(True)
        self.slider.setValue(int(step) + 1)
        self.slider.blockSignals(False)

        self.word_label.setText(self.data_book["tokenize_book"][int(step) + 1])
        self.duration_read.setText(f"Примерное время чтения: {int(delay)} мин.")
