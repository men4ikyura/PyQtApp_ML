from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget
from mainWindow.mainCntl import MainController
from settingWindow.settingCntl import SettingController


class AppHandler(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.mainWnd = MainController()
        self.settingsWnd = SettingController()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.mainWnd)
        self.stack.addWidget(self.settingsWnd)
        self.setCentralWidget(self.stack)

        self.mainWnd.setting_btn.clicked.connect(self.show_settings_window)
        self.settingsWnd.download_btn.clicked.connect(self.show_main_window)
        self.resize(600,600)

        self.show_main_window()

    def show_main_window(self):
        self.setWindowTitle("Главное меню")
        self.stack.setCurrentWidget(self.mainWnd)

    def show_settings_window(self):
        self.setWindowTitle("Настройки меню")
        self.stack.setCurrentWidget(self.settingsWnd)
