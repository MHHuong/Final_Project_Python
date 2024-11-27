from PySide6.QtWidgets import QTableWidgetItem, QDialog, QLabel, QVBoxLayout, QMenuBar, QFormLayout, QMessageBox
from PySide6.QtCore import QDate, QTime, Qt
from PySide6.QtGui import QColor, QBrush, QAction, QFont
from frontPage import MyToDoList
from taskDialog import TaskDialog
from taskaction import Ui_actionWithTask
import numpy as np
import json
import datetime

class MainApp(MyToDoList):
    def __init__(self):
        super().__init__()
        self.tasks = [] 
        self.current_week = None  
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        view_menu = self.menu_bar.addMenu("View")
        task_summary_action = QAction("Task Summary", self)
        task_summary_action.triggered.connect(self.open_task_summary_dialog)
        view_menu.addAction(task_summary_action)

        # Các kết nối khác
        self.addButton.clicked.connect(self.open_task_dialog)
        self.calendarWidget.clicked.connect(self.on_date_clicked)
        self.todayButton.clicked.connect(self.today_clicked)
        self.tableWidget.cellClicked.connect(self.task_clicked)
        self.load_tasks_from_json()

   
    def open_task_summary_dialog(self):
        """Hiển thị hộp thoại thống kê công việc."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Task Summary")
        dialog.setFixedSize(200, 100)  

        dialog.setStyleSheet("""
            QDialog {
                background-color: #FFD1B3;  
                border-radius: 15px;       
            }
            QLabel {
                color: #333333;           
                font-size: 12pt;
                font-family: Arial;
            }
        """)

        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.get("completed", False)])
        remaining_tasks = total_tasks - completed_tasks

        form_layout = QFormLayout()
        form_layout.setHorizontalSpacing(20)
        form_layout.setVerticalSpacing(15)

        total_label = QLabel("Total Tasks:")
        total_value = QLabel(str(total_tasks))
        completed_label = QLabel("Completed Tasks:")
        completed_value = QLabel(str(completed_tasks))
        remaining_label = QLabel("Remaining Tasks:")
        remaining_value = QLabel(str(remaining_tasks))

        bold_font = QFont("Arial", 12, QFont.Weight.Bold)
        total_label.setFont(bold_font)
        completed_label.setFont(bold_font)
        remaining_label.setFont(bold_font)

        form_layout.addRow(total_label, total_value)
        form_layout.addRow(completed_label, completed_value)
        form_layout.addRow(remaining_label, remaining_value)

        dialog.setLayout(form_layout)
        dialog.exec()
    
    def task_clicked(self, row, column):
        item = self.tableWidget.item(row, column)
        if item is None or item.text().strip() == "":
            return
        dialog = QDialog(self)
        task_ui = Ui_actionWithTask()
        task_ui.setupUi(dialog)
        task_ui.completeButton.clicked.connect(lambda: self.complete_action(row, column))
        task_ui.changeTaskButton.clicked.connect(lambda: self.change_task_action(row, column))
        task_ui.deleteButton.clicked.connect(lambda: self.delete_task_action(row, column))
        dialog.exec()

    def delete_task_action(self, row, column):
        """Xóa tất cả các nhiệm vụ giao nhau hoặc có thời gian trùng khớp với nhiệm vụ được chọn."""
        item = self.tableWidget.item(row, column)
        if not item or item.text().strip() == "":
            return

        # Lấy thông tin thời gian và ngày từ ô được chọn
        task_time = item.text().split("\n")[0]
        task_time_start, task_time_end = task_time.split(" - ")
        task_date = self.get_date_from_column(column)

        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(":"))
            return hours * 60 + minutes

        # Convert thời gian bắt đầu và kết thúc sang phút
        task_start_minutes = time_to_minutes(task_time_start)
        task_end_minutes = time_to_minutes(task_time_end)

        # Nếu thời gian bắt đầu và kết thúc bằng nhau (ví dụ: 23:00 - 23:00), xử lý đặc biệt
        if task_start_minutes == task_end_minutes:
            self.tasks = [
                task for task in self.tasks
                if not (
                    task["date"] == task_date and
                    time_to_minutes(task["time_range"].split(" - ")[0]) == task_start_minutes and
                    time_to_minutes(task["time_range"].split(" - ")[1]) == task_end_minutes
                )
            ]
        else:
            # Xóa các nhiệm vụ giao nhau với khoảng thời gian của nhiệm vụ được chọn
            self.tasks = [
                task for task in self.tasks
                if not (
                    task["date"] == task_date and
                    time_to_minutes(task["time_range"].split(" - ")[0]) < task_end_minutes and
                    time_to_minutes(task["time_range"].split(" - ")[1]) > task_start_minutes
                )
            ]

        # Lưu lại nhiệm vụ sau khi xóa và cập nhật giao diện
        self.save_task_to_json()
        self.reset_table_for_week()
        self.load_tasks_from_json()

    def delete_task_action(self, row, column):
        """Xóa nhiệm vụ dựa trên hàng và cột được chọn."""
        item = self.tableWidget.item(row, column)
        if not item or item.text().strip() == "":
            return

        # Lấy thời gian và ngày từ ô được chọn
        task_time = item.text().split("\n")[0]
        task_date = self.get_date_from_column(column)

        # Lọc danh sách nhiệm vụ để loại bỏ nhiệm vụ khớp với thời gian và ngày được chọn
        self.tasks = [
            task for task in self.tasks
            if not (task["time_range"] == task_time and task["date"] == task_date)
        ]

        # Cập nhật lại JSON và giao diện
        self.save_task_to_json()
        self.reset_table_for_week()
        self.load_tasks_from_json()
    
    def change_task_action(self, row, column):
        item = self.tableWidget.item(row, column)
        if item:
            original_task_time = item.text().split("\n")[0]
            original_task_date = self.get_date_from_column(column)
            original_task = None

            # Tìm nhiệm vụ ban đầu trong danh sách
            for task in self.tasks:
                if task["time_range"] == original_task_time and task["date"] == original_task_date:
                    original_task = task
                    break
            if original_task:
                dialog = TaskDialog(self)  # Mở hộp thoại thay đổi nhiệm vụ
                if dialog.exec():  # Nếu người dùng nhấn nút Save
                    new_task_info = dialog.get_task_info()

                    new_task_date = new_task_info["date"]
                    new_task_time_range = new_task_info["time_range"]
                    new_task_start, new_task_end = new_task_time_range.split(" - ")

                    def time_to_minutes(time_str):
                        hours, minutes = map(int, time_str.split(":"))
                        return hours * 60 + minutes

                    new_start_minutes = time_to_minutes(new_task_start)
                    new_end_minutes = time_to_minutes(new_task_end)

                    # Kiểm tra
                    for task in self.tasks:
                        if task["date"] == new_task_date and task != original_task:
                            task_start, task_end = task["time_range"].split(" - ")
                            task_start_minutes = time_to_minutes(task_start)
                            task_end_minutes = time_to_minutes(task_end)
                            print(new_end_minutes, " ", task_end_minutes)
                            print(new_start_minutes," ", task_start_minutes)
                            if not (new_end_minutes < task_end_minutes or new_start_minutes > task_start_minutes):
                                self.show_error_message("The new task time overlaps with an existing task.")
                                return 
                            
                    self.tasks = [
                        task for task in self.tasks
                        if not (
                            task["time_range"] == original_task_time and
                            task["date"] == original_task_date
                        )
                    ]
                    self.tasks.append(new_task_info)

                     # Ghi dữ liệu và cập nhật giao diện
                    self.save_task_to_json()
                    self.reset_table_for_week()
                    self.load_tasks_from_json()


    def complete_action(self, row, column):
        item = self.tableWidget.item(row, column)
        if not item:
            return
        item.setBackground(QColor("#E63F31"))
        font = item.font()
        font.setStrikeOut(True)  # Thêm gạch ngang
        item.setFont(font)
        item.setForeground(QColor("#A9A9A9"))  # Màu chữ nhạt hơn

        task_time = item.text().split("\n")[0]
        task_date = self.get_date_from_column(column)

        for task in self.tasks:
            if task["time_range"] == task_time and task["date"] == task_date:
                task["completed"] = True
        self.save_task_to_json()
        

    def save_task_to_json(self, task_info=None):
        """Lưu danh sách các nhiệm vụ vào file JSON."""
        filename = "tasks.json"
        if task_info:
            # Loại bỏ các nhiệm vụ trùng lặp trước khi thêm
            self.tasks = [
                task for task in self.tasks
                if not (task["date"] == task_info["date"] and task["time_range"] == task_info["time_range"])
            ]
            self.tasks.append(task_info)  
              
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def get_date_from_column(self, column):
        start_of_week = self.calendarWidget.selectedDate().addDays(-(self.calendarWidget.selectedDate().dayOfWeek() - 1))
        return start_of_week.addDays(column).toString("yyyy-MM-dd")

    def today_clicked(self):
        date_now = datetime.date.today()
        qdate = QDate(date_now.year, date_now.month, date_now.day)
        self.on_date_clicked(qdate)

    def load_tasks_from_json(self):
        filename = "tasks.json"
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

        current_date = QDate.currentDate()
        self.display_tasks_for_week(current_date)

    def reset_table_for_week(self):
        for row in range(1, self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                self.tableWidget.setSpan(row, col, 1, 1)
                self.tableWidget.setItem(row, col, None)

    def on_date_clicked(self, date):
        selected_week = date.weekNumber()[0]
        if self.current_week != selected_week:
            self.current_week = selected_week
            self.reset_table_for_week()
        self.display_tasks_for_week(date)

    def display_tasks_for_week(self, selected_date):
        start_of_week, end_of_week = self.get_week_range(selected_date)
        for task in self.tasks:
            task_date = QDate.fromString(task["date"], "yyyy-MM-dd")
            if start_of_week <= task_date <= end_of_week:
                self.add_task_to_timeline(task)

    def open_task_dialog(self):
        """Mở hộp thoại tạo nhiệm vụ mới."""
        dialog = TaskDialog(self)
        if dialog.exec():
            task_info = dialog.get_task_info()
            task_date = QDate.fromString(task_info["date"], "yyyy-MM-dd")
            task_time_start, task_time_end = task_info["time_range"].split(" - ")

            def time_to_minutes(time_str):
                hours, minutes = map(int, time_str.split(":"))
                return hours * 60 + minutes

            new_task_start = time_to_minutes(task_time_start)
            new_task_end = time_to_minutes(task_time_end)

            # Loại bỏ tất cả các nhiệm vụ bị "đè" bởi nhiệm vụ mới
            self.tasks = [
                task for task in self.tasks
                if not (
                    task["date"] == task_info["date"] and
                    time_to_minutes(task["time_range"].split(" - ")[0]) < new_task_end and
                    time_to_minutes(task["time_range"].split(" - ")[1]) > new_task_start
                )
            ]

            # Lưu nhiệm vụ mới và cập nhật giao diện
            self.save_task_to_json(task_info)
            start_of_week, end_of_week = self.get_week_range(QDate.currentDate())
            if start_of_week <= task_date <= end_of_week:
                self.add_task_to_timeline(task_info)


    def get_week_range(self, date):
        start_of_week = date.addDays(-(date.dayOfWeek() - 1))
        end_of_week = start_of_week.addDays(6)
        return start_of_week, end_of_week

    def add_task_to_timeline(self, task_info):
        task_date = task_info["date"]
        time_range = task_info["time_range"]
        task_name = time_range + "\n" + task_info["name"]
        task_date_obj = QDate.fromString(task_date, "yyyy-MM-dd")
        start_time_str, end_time_str = time_range.split(" - ")
        start_time = QTime.fromString(start_time_str, "HH:mm")
        end_time = QTime.fromString(end_time_str, "HH:mm")
        day_index = task_date_obj.dayOfWeek() - 1
        start_hour = start_time.hour()
        end_hour = end_time.hour()
        if start_hour == 23 and end_hour == 0:
            end_hour = 24

        for hour in range(start_hour, end_hour + 1):
            table_row = hour + 1
            if hour == start_hour:
                item = QTableWidgetItem(task_name)
                self.tableWidget.setItem(table_row, day_index, item)
                span_rows = end_hour - start_hour
                self.tableWidget.setSpan(table_row, day_index, span_rows, 1)

                if task_info.get("completed", False):
                    font = item.font()
                    font.setStrikeOut(True)
                    item.setFont(font)
                    item.setForeground(QColor("#A9A9A9"))

                def generate_light_color():
                    r = np.random.randint(200, 255)
                    g = np.random.randint(200, 255)
                    b = np.random.randint(200, 255)
                    return QColor(r, g, b)

                light_color = generate_light_color()
                item.setBackground(light_color)
                item.setTextAlignment(Qt.AlignCenter)
    def show_error_message(self, message):
        QMessageBox.warning(self, "Input Error", message)
