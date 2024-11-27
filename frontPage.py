from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QColor
from user_interface import Ui_MainWindow
from date_management import DateManagement
import datetime

class MyToDoList(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo List App")

        self.date_management = DateManagement(self)
        self.calendarWidget.clicked.connect(self.set_day)

        date_now = datetime.date.today()
        self.update_labels_and_table(date_now)

        self.todayButton.clicked.connect(self.set_today)
        
    def set_today(self):
        date_now = datetime.date.today()
        qdate = QDate(date_now.year, date_now.month, date_now.day)
        self.update_labels_and_table(date_now)
        self.date_management.set_date_label(qdate)
        self.calendarWidget.setSelectedDate(qdate)
    
    def set_day(self, date):
        selected_date = date.toPython()
        self.update_labels_and_table(selected_date)
        self.date_management.set_date_label(date)

    def update_labels_and_table(self, date_now):

        self.tableWidget.clearContents()

        for i in range(7):

            offset = i - date_now.weekday()
            date = date_now + datetime.timedelta(days=offset)
            day_text = self.if_day_less_than_10(date.day)

            item = QTableWidgetItem(day_text)
            item.setTextAlignment(Qt.AlignCenter)

            today = datetime.date.today()
            if date == today:
                item.setBackground(QColor("#ADD8E6"))  
            else:
                item.setBackground(QColor("#FFC0CB")) 

            self.tableWidget.setItem(0, i, item)

    def if_day_less_than_10(self, day):
        return f'0{day}' if day < 10 else str(day)
