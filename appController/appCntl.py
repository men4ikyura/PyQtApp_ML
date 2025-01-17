from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from mainWindow.mainCntl import MainController
from settingWindow.settingUI import SettingsUI
from prepareProcessWindow.downloadMainUI import DownloadMainWindowUI
from prepareProcessWindow.showImageWnd import ShowImageWindow
from processWindow.waitProcessUI import ProcessingWindow
from finishWindow.finishUI import FinishImageWindow
from finishWindow.finishGraphic import GraphicsDraw
from stackCntrl.stackCntrl import StackCntrl
from historyWindow.historyUI import HistoryUI
from documentationWindow.documWnd import DocumentationUI
from PyQt5.QtGui import QIcon
from settingWindow.settingUI import SettingsUI
import os


class AppHandler(QMainWindow):

    def __init__(self):
        if not os.path.exists("./settings.json"):
            SettingsUI.create_settings_file()
        super().__init__()
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.show_main_window()
        self.setWindowIcon(QIcon('icon.ico'))
        self.show_main_window()

    def show_main_window(self):
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = MainController()
        self.setWindowTitle("Главное меню")
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        self.resize(600, 400)
        self.center()
        widget_instance.setting_btn.clicked.connect(self.show_settings_window)
        widget_instance.download_btn.clicked.connect(self.show_download_window)
        widget_instance.show_hst_btn.clicked.connect(self.show_history_window)
        widget_instance.documentation_btn.clicked.connect(
            self.show_documentation_wnd)

    def show_documentation_wnd(self):
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = DocumentationUI()
        self.setWindowTitle("Параметры модели")
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        self.center()
        widget_instance.come_back_main_menu.connect(self.show_main_window)

    def show_finish_graphics(self, info_drops):
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = GraphicsDraw(info_drops)
        self.setWindowTitle("График")
        self.center()
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        widget_instance.come_back_download_menu.connect(
            self.show_download_window)

    def show_history_window(self):
        widget_instance = self.add_item_to_stack(
            "История обработок", HistoryUI)
        widget_instance.come_back.connect(self.show_main_window)
        self.center()

    def show_settings_window(self):
        widget_instance = self.add_item_to_stack(
            "Настройки", SettingsUI)
        widget_instance.come_back.connect(self.show_main_window)

    def show_download_window(self):
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = DownloadMainWindowUI()
        self.setWindowTitle("Загрузочное меню")
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        self.resize(600, 400)
        self.center()
        widget_instance.come_back.connect(self.show_main_window)
        widget_instance.file_selected.connect(self.show_image_window)

    def show_processing_window(self, file_path, *args):
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = ProcessingWindow(file_path, *args)
        self.setWindowTitle("Обработка изображения")
        self.resize(widget_instance.sizeHint())
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        widget_instance.result_ready.connect(self.stop_process_image)
        widget_instance.come_back_show_image.connect(self.show_image_window)

    def stop_process_image(self, info_drops, file_path):
        widget_instance = FinishImageWindow(info_drops, file_path)
        self.setWindowTitle("Результаты обработки")
        self.resize(widget_instance.sizeHint())
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        self.center()
        widget_instance.come_back_download_menu.connect(
            self.show_download_window)
        widget_instance.get_data_to_graphics.connect(self.show_finish_graphics)

    def show_image_window(self, file_path, *args):
        self.setWindowTitle("Загрузочное меню")
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = ShowImageWindow(file_path, *args)
        self.resize(widget_instance.sizeHint())
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        self.center()
        widget_instance.come_back.connect(self.show_download_window)
        widget_instance.go_to_processing.connect(self.show_processing_window)

    def add_item_to_stack(self, title, class_name):
        self.setWindowTitle(title)
        StackCntrl.clear_stacked_widget(self.stack)
        widget_instance = class_name()
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)

        return widget_instance

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
