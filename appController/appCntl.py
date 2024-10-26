from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget
from mainWindow.mainCntl import MainController
from settingWindow.settingCntl import SettingController
from downloadWindow.downloadCntl import DownloadController


class AppHandler(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.show_main_window()
        self.setCentralWidget(self.stack)
        self.resize(600,600)
        # self.mainWnd = MainController()
        # self.settingsWnd = SettingController()
        # self.downloadMenu = DownloadController()

        # self.stack = QStackedWidget()
        # self.stack.addWidget(self.mainWnd)
        # self.stack.addWidget(self.settingsWnd)
        # self.stack.addWidget(self.downloadMenu)
        # self.setCentralWidget(self.stack)
    def clear_stacked_widget(self):
    # Удаление всех виджетов из QStackedWidget
        while self.stack.count():
            widget = self.stack.widget(0)
            self.stack.removeWidget(widget)
            widget.deleteLater()  # Удаление самого виджета из памяти

    def show_main_window(self):
        self.clear_stacked_widget()
        main_window = MainController()  # Создание нового экземпляра
        self.stack.addWidget(main_window)
        self.stack.setCurrentWidget(main_window)
        main_window.setting_btn.clicked.connect(self.show_settings_window)
        # self.mainWnd.download_btn.clicked.connect(self.show_download_window)
        # self.settingsWnd.come_back_main_menu_btn.clicked.connect(self.show_main_window)
        # self.downloadMenu.come_back_main_menu_btn.clicked.connect(self.show_main_window)
        # self.resize(600,600)

    def show_settings_window(self):
        self.clear_stacked_widget()
        settings_window = SettingController()  # Создание нового экземпляра
        self.stack.addWidget(settings_window)
        self.stack.setCurrentWidget(settings_window)
        settings_window.come_back_main_menu_btn.clicked.connect(self.show_main_window)
    # def show_download_window(self):
    #     self.setWindowTitle("Загрузочное меню")
    #     self.stack.setCurrentWidget(self.downloadMenu)

    # def show_main_window(self):
    #     self.setWindowTitle("Главное меню")
    #     self.stack.setCurrentWidget(self.mainWnd)

    # def show_settings_window(self):
    #     self.setWindowTitle("Настройки меню")
    #     self.stack.setCurrentWidget(self.settingsWnd)
