# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(581, 530)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.verticalLayout_4 = QVBoxLayout(self.setting)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.setting)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(516, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.toolButton_7 = QToolButton(self.frame_4)
        self.toolButton_7.setObjectName(u"toolButton_7")
        icon = QIcon()
        icon.addFile(u":/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.toolButton_7)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.frame_5 = QFrame(self.setting)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinBox = QSpinBox(self.frame_6)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000000000)

        self.horizontalLayout_5.addWidget(self.spinBox)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox_2 = QSpinBox(self.frame_7)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(1000000000)

        self.horizontalLayout_4.addWidget(self.spinBox_2)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.setting)
        self.readBook = QWidget()
        self.readBook.setObjectName(u"readBook")
        self.verticalLayout_2 = QVBoxLayout(self.readBook)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.readBook)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 22))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.toolButton_3 = QToolButton(self.frame_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon/paly.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 0))
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/icon/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QSize(35, 35))
        self.toolButton.setAutoRaise(False)

        self.horizontalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon3)
        self.toolButton_2.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.toolButton_6 = QToolButton(self.frame_2)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.toolButton_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.readBook)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(26)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget.addWidget(self.readBook)
        self.mainMenu = QWidget()
        self.mainMenu.setObjectName(u"mainMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainMenu.sizePolicy().hasHeightForWidth())
        self.mainMenu.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.mainMenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.toolButton_4 = QToolButton(self.frame_3)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icon/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.toolButton_4, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(523, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.toolButton_5 = QToolButton(self.frame_3)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icon/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon5)
        self.toolButton_5.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.toolButton_5)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.mainMenu)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432 \u0432 \u043c\u0438\u043d\u0443\u0442\u0443", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"sdasd", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

