import json

class SettingsModel:
    def __init__(self):
        self.digit = self.load_data()
        self.previous_digit = self.digit

    def load_data(self):
            try:
                with open("settings.json", "r") as file:
                    data = json.load(file)
                    return data.get("digit", 0)
            except (FileNotFoundError, json.JSONDecodeError):
                return 0
        