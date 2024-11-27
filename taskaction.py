# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskaction.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_actionWithTask(object):
    def setupUi(self, actionWithTask):
        if not actionWithTask.objectName():
            actionWithTask.setObjectName(u"actionWithTask")
        actionWithTask.resize(400, 250)
        actionWithTask.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        self.completeButton = QPushButton(actionWithTask)
        self.completeButton.setObjectName(u"completeButton")
        self.completeButton.setGeometry(QRect(10, 10, 381, 71))
        self.completeButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 81 8pt \"Inter ExtraBold\";\n"
"    background-color: rgb(220, 205, 194);\n"
"    border: 2px solid rgb(220, 205, 194);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 180, 170); \n"
"    border: 2px solid rgb(200, 180, 170);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 160, 150); \n"
"    border: 2px solid rgb(180, 160, 150);\n"
"}")
        self.changeTaskButton = QPushButton(actionWithTask)
        self.changeTaskButton.setObjectName(u"changeTaskButton")
        self.changeTaskButton.setGeometry(QRect(10, 90, 381, 71))
        self.changeTaskButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 81 8pt \"Inter ExtraBold\";\n"
"    background-color: rgb(220, 205, 194);\n"
"    border: 2px solid rgb(220, 205, 194);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 180, 170); \n"
"    border: 2px solid rgb(200, 180, 170);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 160, 150); \n"
"    border: 2px solid rgb(180, 160, 150);\n"
"}")
        self.deleteButton = QPushButton(actionWithTask)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(10, 170, 381, 71))
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 81 8pt \"Inter ExtraBold\";\n"
"    background-color: rgb(220, 205, 194);\n"
"    border: 2px solid rgb(220, 205, 194);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 180, 170); \n"
"    border: 2px solid rgb(200, 180, 170);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 160, 150); \n"
"    border: 2px solid rgb(180, 160, 150);\n"
"}")

        self.retranslateUi(actionWithTask)

        QMetaObject.connectSlotsByName(actionWithTask)
    # setupUi

    def retranslateUi(self, actionWithTask):
        actionWithTask.setWindowTitle(QCoreApplication.translate("actionWithTask", u"Task Action", None))
        self.completeButton.setText(QCoreApplication.translate("actionWithTask", u"COMPLETED", None))
        self.changeTaskButton.setText(QCoreApplication.translate("actionWithTask", u"CHANGE TASK", None))
        self.deleteButton.setText(QCoreApplication.translate("actionWithTask", u"DELETE", None))
    # retranslateUi

