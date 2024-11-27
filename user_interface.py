# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1304, 655)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.action_widget = QWidget(self.centralwidget)
        self.action_widget.setObjectName(u"action_widget")
        self.action_widget.setGeometry(QRect(350, 0, 931, 101))
        self.action_widget.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        self.month_year_label = QLabel(self.action_widget)
        self.month_year_label.setObjectName(u"month_year_label")
        self.month_year_label.setGeometry(QRect(50, 40, 241, 51))
        font = QFont()
        font.setFamilies([u"Inter"])
        self.month_year_label.setFont(font)
        self.month_year_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.todayButton = QPushButton(self.action_widget)
        self.todayButton.setObjectName(u"todayButton")
        self.todayButton.setGeometry(QRect(420, 50, 75, 31))
        font1 = QFont()
        font1.setFamilies([u"Inter ExtraBold"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.todayButton.setFont(font1)
        self.todayButton.setFocusPolicy(Qt.StrongFocus)
        self.todayButton.setStyleSheet(u"QPushButton {\n"
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
        self.addButton = QPushButton(self.action_widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(530, 50, 75, 31))
        font2 = QFont()
        font2.setFamilies([u"Inter Display ExtraBold"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.addButton.setFont(font2)
        self.addButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 81 8pt \"Inter Display ExtraBold\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50); \n"
"    border: 2px solid rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(80, 80, 80); \n"
"    border: 2px solid rgb(80, 80, 80);\n"
"}")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 351, 651))
        self.widget_2.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        self.calendarWidget = QCalendarWidget(self.widget_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 80, 321, 301))
        self.calendarWidget.setStyleSheet(u"\n"
"QCalendarWidget QWidget {\n"
"	 alternate-background-color: #B8E2FF;\n"
"}\n"
"\n"
"/* style for top navigation area*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"   background-color: #fff;\n"
"	color: #000;\n"
"	border-bottom: 0px;\n"
"}\n"
"\n"
"/* style for month change buttons*/\n"
"\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"    border: none;  \n"
"	qproperty-icon: none; \n"
"	\n"
"    min-width: 13px;\n"
"    max-width: 13px;\n"
"    min-height: 13px;\n"
"    max-height: 13px;\n"
"\n"
"    border-radius: 5px; \n"
"    background-color: transparent; \n"
"	padding: 5px;\n"
"}\n"
"\n"
"/* style for pre month button*/\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	margin-left:5px;\n"
"	image: url(./icon/arrow-119-48.ico);\n"
"}\n"
"\n"
"/* style for next month button*/\n"
"#qt_calendar_nextmonth {\n"
"	margin-right:5px;\n"
"	image: url(./icon/arrow-19-48.ico);\n"
"}\n"
"#qt_calendar_prevmonth:hover, \n"
"#qt_calendar_nextmonth:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calen"
                        "dar_prevmonth:pressed, \n"
"#qt_calendar_nextmonth:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"\n"
"/* Style for month and yeat buttons*/\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	font-size: 13px;\n"
"	padding:0px 10px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 135px;\n"
"    color: #000;\n"
"	font-size: 13px;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	padding:0px 2px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_monthbutton:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit*/\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 70px;\n"
"    color: #000;\n"
"    background: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"/* Style for year change buttons*/\n"
"\n"
"#qt_calendar_yearedit::up-butt"
                        "on { \n"
"	image: url(./icon/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image: url(./icon/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"	background-color: #55aaff;\n"
"}\n"
"\n"
"/* Style for month select menu*/\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"	color: #000;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	padding: 10px;\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* "
                        "Style for calendar table*/\n"
"#qt_calendar_calendarview {\n"
"    outline: 0px;\n"
"	color: #000;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"   border-radius:5px;\n"
"	background-color:#aaffff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #55aa7f; \n"
"	border-radius:5px;\n"
"}")
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 25):
            self.tableWidget.setRowCount(25)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, __qtablewidgetitem31)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.NoBrush)
        font3 = QFont()
        font3.setPointSize(14)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font3);
        __qtablewidgetitem32.setBackground(brush);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font3);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font3);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font3);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font3);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem37.setFont(font3);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem38.setFont(font3);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignLeading|Qt.AlignTop);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem39)
        font4 = QFont()
        font4.setUnderline(True)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font4);
        self.tableWidget.setItem(3, 3, __qtablewidgetitem40)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(350, 100, 951, 551))
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setStyleSheet(u"background-color: rgb(251, 247, 244);\n"
"color: rgb(0, 0, 0);\n"
"font: 81 8pt \"Inter ExtraBold\";")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.month_year_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">November 2024</span></p></body></html>", None))
        self.todayButton.setText(QCoreApplication.translate("MainWindow", u"TODAY", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Mon", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tue", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Wed", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Thu", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fri", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sat", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Sun", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Hour/Day", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"0 AM", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1 AM", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"2 AM", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"3 AM", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"4 AM", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"5 AM", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"6 AM", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"7 AM", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"8 AM", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"9 AM", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"10 AM", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"11 AM", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"12 PM", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1 PM", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"2 PM", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"3 PM", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"4 PM", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"5 PM", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"6 PM", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"7 PM", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(21)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"8 PM", None));
        ___qtablewidgetitem29 = self.tableWidget.verticalHeaderItem(22)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"9 PM", None));
        ___qtablewidgetitem30 = self.tableWidget.verticalHeaderItem(23)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"10 PM", None));
        ___qtablewidgetitem31 = self.tableWidget.verticalHeaderItem(24)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"11 PM", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem32 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem33 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem34 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem35 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem36 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem37 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem38 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

