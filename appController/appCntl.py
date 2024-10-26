from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget
from mainWindow.mainCntl import MainController
from settingWindow.settingCntl import SettingController
from downloadWindow.downloadCntl import DownloadController


class AppHandler(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.mainWnd = MainController()
        self.settingsWnd = SettingController()
        self.downloadMenu = DownloadController()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.mainWnd)
        self.stack.addWidget(self.settingsWnd)
        self.stack.addWidget(self.downloadMenu)
        self.setCentralWidget(self.stack)

        self.mainWnd.setting_btn.clicked.connect(self.show_settings_window)
        self.mainWnd.download_btn.clicked.connect(self.show_download_window)
        self.settingsWnd.come_back_main_menu_btn.clicked.connect(self.show_main_window)
        self.downloadMenu.come_back_main_menu_btn.clicked.connect(self.show_main_window)
        self.resize(600,600)

        self.show_main_window()

    def show_download_window(self):
        self.setWindowTitle("Загрузочное меню")
        self.stack.setCurrentWidget(self.downloadMenu)
        
    def show_main_window(self):
        self.setWindowTitle("Главное меню")
        self.stack.setCurrentWidget(self.mainWnd)

    def show_settings_window(self):
        self.setWindowTitle("Настройки меню")
        self.stack.setCurrentWidget(self.settingsWnd)
