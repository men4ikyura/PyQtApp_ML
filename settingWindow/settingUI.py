from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QMainWindow
import json

class SettingsUI(QMainWindow):


    def __init__(self):
        super().__init__()
        self.add_btn = QPushButton("+")
        self.minus_btn = QPushButton("-")
        self.come_back_main_menu_btn = QPushButton("Назад")
        self.save_settings_data = QPushButton("Сохранить")


    def setup_settings_ui(self):
        self.digit = self.load_data()
        self.previous_digit = self.digit
        self.digit_label = QLabel(f"Текущий счетчик: {self.digit}")
        layout = QVBoxLayout()
        title = QLabel("Это настройки")
        layout.addWidget(title)
        layout.addWidget(self.come_back_main_menu_btn)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.minus_btn)
        layout.addWidget(self.digit_label) 
        layout.addWidget(self.save_settings_data) 
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        try:
            with open("settings.json", "r") as file:
                data = json.load(file)
                return data.get("digit", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
        