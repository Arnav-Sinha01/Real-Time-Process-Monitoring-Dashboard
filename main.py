# main.py
import sys
from PyQt6.QtWidgets import QApplication
from ui import SystemMonitor

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            background-color: #121212;
            color: #e0e0e0;
            font-size: 14px;
        }
        
        QPushButton:hover {
            background-color: #2a8cbd;
        }
        QLineEdit {
            border: 1px solid #666;
            background-color: #1e1e1e;
            color: white;
        }
    """)
    window = SystemMonitor()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
