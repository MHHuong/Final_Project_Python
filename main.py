from PySide6.QtWidgets import QApplication
from button import MainApp
from PySide6.QtCore import QLoggingCategory #import module de xoa
import sys

if __name__ == "__main__":
    QLoggingCategory.setFilterRules("*=false")  # Xoa log
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())