from settingWindow.settingUI import SettingsUI
from PyQt6.QtWidgets import QMainWindow

class SettingController(QMainWindow, SettingsUI):
    def __init__(self):
        super().__init__()
        self.setup_settings_ui()

        
