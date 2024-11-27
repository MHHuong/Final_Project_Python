# date_management.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from user_interface import Ui_MainWindow
import datetime 

class DateManagement:
    def __init__(self, main_window):
        self.main_window = main_window
        
        day_font = QFont()
        day_font.setFamilies(["Inter"])
        day_font.setPointSize(16)
        day_font.setBold(True)
        
        style = "color: rgb(220, 205, 194);"
        
        month_font = QFont()
        month_font.setFamilies(["Inter"])
        month_font.setPointSize(18)
        month_font.setBold(True)
        
        self.main_window.month_year_label.setFont(month_font)
        self.main_window.month_year_label.setStyleSheet("color: rgb(0, 0, 0);")
    
    def if_day_less_than_10(self, day):
        if day < 10:
            return '0' + str(day)
        return str(day)
            
    def set_date_label(self, date):
        date_changed = datetime.date(date.year(), date.month(), date.day())
        day_current = date_changed.day 
            
        month_dictionary = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                            7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"} 
        self.main_window.month_year_label.setText(month_dictionary[date_changed.month] + " " + str(date_changed.year))