# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zeekify.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_Converted = QTextEdit(self.centralwidget)
        self.text_Converted.setObjectName(u"text_Converted")
        self.text_Converted.setReadOnly(True)

        self.gridLayout.addWidget(self.text_Converted, 3, 0, 1, 1)

        self.button_Copy = QPushButton(self.centralwidget)
        self.button_Copy.setObjectName(u"button_Copy")

        self.gridLayout.addWidget(self.button_Copy, 4, 0, 1, 1)

        self.button_Zeekify = QPushButton(self.centralwidget)
        self.button_Zeekify.setObjectName(u"button_Zeekify")

        self.gridLayout.addWidget(self.button_Zeekify, 2, 0, 1, 1)

        self.text_Source = QTextEdit(self.centralwidget)
        self.text_Source.setObjectName(u"text_Source")

        self.gridLayout.addWidget(self.text_Source, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_Copy.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.button_Zeekify.setText(QCoreApplication.translate("MainWindow", u"Zeekify", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter your text here:", None))
    # retranslateUi

