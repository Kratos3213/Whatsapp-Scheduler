import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QLineEdit, QTextEdit, QPushButton, QLabel)
from PyQt6.QtCore import Qt
import pywhatkit as kit
from datetime import datetime

class WhatsAppScheduler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Scheduler")
        self.setStyleSheet("background-color: white;")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("WhatsApp Scheduler")
        title.setStyleSheet("font-size: 24px; color: #075e54; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Phone number input
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone Number (e.g., +1234567890)")
        self.phone_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #128C7E;
                border-radius: 5px;
                font-size: 16px;
            }
        """)
        layout.addWidget(self.phone_input)

        # Message input
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Message")
        self.message_input.setStyleSheet("""
            QTextEdit {
                padding: 10px;
                border: 1px solid #128C7E;
                border-radius: 5px;
                font-size: 16px;
            }
        """)
        self.message_input.setFixedHeight(100)
        layout.addWidget(self.message_input)

        # Time input
        self.time_input = QLineEdit()
        self.time_input.setPlaceholderText("Time (HH:MM in 24-hour format)")
        self.time_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #128C7E;
                border-radius: 5px;
                font-size: 16px;
            }
        """)
        layout.addWidget(self.time_input)

        # Schedule button
        self.schedule_btn = QPushButton("Schedule Message")
        self.schedule_btn.setStyleSheet("""
            QPushButton {
                background-color: #128C7E;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:pressed {
                background-color: #075e54;
            }
        """)
        self.schedule_btn.clicked.connect(self.schedule_message)
        layout.addWidget(self.schedule_btn)

        # Status label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: #128C7E; font-size: 16px;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        # Set window size
        self.setFixedSize(400, 500)

    def schedule_message(self):
        phone_number = self.phone_input.text()
        message = self.message_input.toPlainText()
        time_str = self.time_input.text()

        if not phone_number or not message or not time_str:
            self.status_label.setText("Please fill in all fields")
            return

        try:
            hour, minute = map(int, time_str.split(":"))
            now = datetime.now()

            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                self.status_label.setText("Invalid time format")
                return

            if hour < now.hour or (hour == now.hour and minute <= now.minute):
                self.status_label.setText("Scheduled time must be in the future")
                return

            try:
                kit.sendwhatmsg(phone_number, message, hour, minute)
                self.status_label.setText(f"Message scheduled for {hour:02d}:{minute:02d}")
            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")

        except ValueError:
            self.status_label.setText("Invalid time format. Use HH:MM")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WhatsAppScheduler()
    window.show()
    sys.exit(app.exec())
