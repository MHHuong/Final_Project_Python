from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QDateEdit, QVBoxLayout, QPushButton, QFrame, QMessageBox, QTimeEdit
from PySide6.QtCore import QDate, QTime, Signal
from PySide6.QtGui import QFont
import json

class TaskDialog(QDialog):
    # Define a signal to emit when a task is created
    task_created = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Task")
        self.setFixedSize(320, 450)
        self.setStyleSheet("background-color: #FFD1B3;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        header_frame = QFrame(self)
        header_frame.setFixedHeight(100)
        header_frame.setStyleSheet("""
            background-color: #FFD1B3; 
            border-top-left-radius: 15px; 
            border-top-right-radius: 15px;
        """)
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(15, 15, 15, 0)

        title_label = QLabel("Create New Task", self)
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #333333;")
        header_layout.addWidget(title_label)

        self.task_name = QLineEdit()
        self.task_name.setPlaceholderText("Enter task name")
        self.task_name.setFixedHeight(40)
        self.task_name.setStyleSheet("""
            padding: 5px; font-size: 15pt; color: #333333;
            background-color: #FFD1B3; border: none;
        """)
        header_layout.addWidget(self.task_name)

        main_layout.addWidget(header_frame)

        input_container = QFrame()
        input_container.setFixedHeight(250)
        input_container.setStyleSheet("""
            background-color: #FFFFFF;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        """)

        input_layout = QVBoxLayout()
        input_layout.setContentsMargins(20, 5, 20, 5)
        input_layout.setSpacing(10)

        # Date Edit
        task_date_label = QLabel("Date")
        task_date_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        task_date_label.setStyleSheet("color: #555555; margin-bottom: 0px;")
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("dddd, dd MMMM")
        self.date_edit.setFixedHeight(30)
        self.date_edit.setStyleSheet("""
            padding: 5px; font-size: 12pt; color: #333333;
            border: 1px solid #AAAAAA; border-radius: 5px;
            background-color: #F5F5F5;
        """)
        input_layout.addWidget(task_date_label)
        input_layout.addWidget(self.date_edit)

        # Time Edits
        time_layout = QVBoxLayout()
        time_layout.setSpacing(10)

        task_time_label = QLabel("Time Range")
        task_time_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        task_time_label.setStyleSheet("color: #555555; margin-bottom: 0px;")
        time_layout.addWidget(task_time_label)

        self.start_time_edit = QTimeEdit()
        self.start_time_edit.setTime(QTime.currentTime())
        self.start_time_edit.setDisplayFormat("HH:00")
        self.start_time_edit.setFixedHeight(30)
        self.start_time_edit.setStyleSheet("""
            padding: 5px; font-size: 12pt; color: #333333;
            border: 1px solid #AAAAAA; border-radius: 5px;
            background-color: #F5F5F5;
        """)

        self.end_time_edit = QTimeEdit()
        self.end_time_edit.setTime(QTime.currentTime().addSecs(3600))
        self.end_time_edit.setDisplayFormat("HH:00")
        self.end_time_edit.setFixedHeight(30)
        self.end_time_edit.setStyleSheet("""
            padding: 5px; font-size: 12pt; color: #333333;
            border: 1px solid #AAAAAA; border-radius: 5px;
            background-color: #F5F5F5;
        """)

        time_layout.addWidget(QLabel("Start Time"))
        time_layout.addWidget(self.start_time_edit)
        time_layout.addWidget(QLabel("End Time"))
        time_layout.addWidget(self.end_time_edit)

        input_layout.addLayout(time_layout)

        input_container.setLayout(input_layout)
        main_layout.addWidget(input_container)

        # Save Button
        self.save_button = QPushButton("Save Task")
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font: bold 10pt Arial;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
        """)
        self.save_button.setFixedHeight(50)
        main_layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.on_save_clicked)

    def on_save_clicked(self):
        if self.validate_time_input():
            # Get task info
            task_info = self.get_task_info()
            # Emit signal with task i nfo
            if hasattr(self.parent(), "save_task_to_json"):
                self.parent().save_task_to_json(task_info)

            self.task_created.emit(task_info)
            self.accept()
  

    def validate_time_input(self):
        start_time = self.start_time_edit.time()
        end_time = self.end_time_edit.time()
        if start_time.hour() == 23 and end_time.hour() == 0:
            return True
        if end_time <= start_time:
            self.show_error("End time must be after start time.")
            return False

        return True

    def get_task_info(self):
        start_time_str = self.start_time_edit.time().toString("HH:00")
        end_time_str = self.end_time_edit.time().toString("HH:00")
        time_range = f"{start_time_str} - {end_time_str}"
        return {
            "name": self.task_name.text(),
            "date": self.date_edit.date().toString("yyyy-MM-dd"),
            "time_range": time_range,
        }

    def show_error(self, message):
        QMessageBox.warning(self, "Input Error", message)
        
   
