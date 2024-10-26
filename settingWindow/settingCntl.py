from settingWindow.settingUI import SettingsUI
from PyQt6.QtWidgets import QMessageBox
import json


class SettingController(SettingsUI):
    def __init__(self):
        super().__init__()
        self.setup_settings_ui()
        self.connect_signals()

    def connect_signals(self):
        self.add_btn.clicked.connect(self.increment_digit)
        self.minus_btn.clicked.connect(self.decrement_digit)
        self.save_settings_data.clicked.connect(self.save_data)

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
                    existing_data = json.load(file)  # Чтение текущих данных из файла
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = {}  # Инициализация пустого словаря, если файл не найден или пуст

            existing_data["digit"] = self.digit  # Обновление значения по ключу "digit"
            
            self.previous_digit = self.digit
            
            with open("settings.json", "w") as file:
                json.dump(existing_data, file)

            QMessageBox.information(self, "Информация", "Сохранилось")  # Запись обновленных данных обратно в файл

        # self.close()



        
