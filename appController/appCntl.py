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
       

    def clear_stacked_widget(self):
        while self.stack.count():
            widget = self.stack.widget(0)
            self.stack.removeWidget(widget)
            widget.deleteLater() 


    def show_main_window(self):
        self.setWindowTitle("Главное мемню")
        self.clear_stacked_widget()
        main_window = MainController()  
        self.stack.addWidget(main_window)
        self.stack.setCurrentWidget(main_window)
        main_window.setting_btn.clicked.connect(self.show_settings_window)
        main_window.download_btn.clicked.connect(self.show_download_window)
       

    def show_settings_window(self):
        self.setWindowTitle("Настройки")
        self.clear_stacked_widget()
        settings_window = SettingController()  
        self.stack.addWidget(settings_window)
        self.stack.setCurrentWidget(settings_window)
        settings_window.come_back_main_menu_btn.clicked.connect(self.show_main_window)


    def show_download_window(self):
        self.setWindowTitle("Загрузочное меню")
        self.clear_stacked_widget()
        download_window = DownloadController()  
        self.stack.addWidget(download_window)
        self.stack.setCurrentWidget(download_window)
        download_window.come_back_main_menu_btn.clicked.connect(self.show_main_window)
