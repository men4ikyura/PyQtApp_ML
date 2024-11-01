from settingWindow.settingUI import SettingsUI
from PyQt6.QtWidgets import QMessageBox
import json
from PyQt6.QtCore import pyqtSignal


class SettingController(SettingsUI):

    come_back = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setup_settings_ui()
        self.connect_signals()
         

    def connect_signals(self):
        self.add_btn.clicked.connect(self.increment_digit)
        self.minus_btn.clicked.connect(self.decrement_digit)
        self.save_settings_data.clicked.connect(self.save_data)
        self.come_back_main_menu_btn.clicked.connect(self.emit_come_back_signal)

    def increment_digit(self):
        self.digit += 1
        self.update_digit_display()  

    def decrement_digit(self):
        self.digit -= 1
        self.update_digit_display()  

    def update_digit_display(self):
        self.digit_label.setText(f"Текущий счетчик: {self.digit}")
    
    def save_data(self):
        if self.digit == self.previous_digit:
            QMessageBox.information(self, "Информация", "Значение не изменилось.")
        else:
            try:
                with open("settings.json", "r") as file:
                    existing_data = json.load(file)  
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = {}  

            existing_data["digit"] = self.digit 
            
            self.previous_digit = self.digit
            QMessageBox.information(self, "Информация", "Значение поменялось.")
            with open("settings.json", "w") as file:
                json.dump(existing_data, file)

    
    def emit_come_back_signal(self):
        self.come_back.emit() 