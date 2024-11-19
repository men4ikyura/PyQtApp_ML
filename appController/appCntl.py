from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from mainWindow.mainCntl import MainController
from settingWindow.settingCntl import SettingController
from prepareProcessWindow.downloadMainUI import DownloadMainWindowUI
from prepareProcessWindow.showImageWnd import ShowImageWindow
from processWindow.waitProcessUI import ProcessingWindow
from finishWindow.finishUI import FinishImageWindow
from stackCntrl.stackCntrl import StackCntrl


class AppHandler(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.resize(600, 600)

        # Показываем главное окно при инициализации приложения
        self.show_main_window()

    
    def show_main_window(self):
        """Показывает главное окно приложения."""
        widget_instance = self.add_item_to_stack("Главное меню", MainController)
        widget_instance.setting_btn.clicked.connect(self.show_settings_window)
        widget_instance.download_btn.clicked.connect(self.show_download_window)


    def show_settings_window(self):
        """Показывает окно настроек приложения."""
        widget_instance = self.add_item_to_stack("Настройки", SettingController)
        widget_instance.come_back.connect(self.show_main_window)
        
        
    def show_download_window(self):
        """Показывает окно загрузки."""
        widget_instance = DownloadMainWindowUI()  
        self.resize(widget_instance.sizeHint())
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        widget_instance.come_back.connect(self.show_main_window)
        widget_instance.file_selected.connect(self.show_image_window)


    def show_processing_window(self, file_path):
        widget_instance = ProcessingWindow(file_path)  
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        widget_instance.result_ready.connect(self.stop_process_image)


    def stop_process_image(self, info_drops, file_path):
        widget_instance = FinishImageWindow(info_drops, file_path)  
        self.resize(widget_instance.sizeHint())
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        widget_instance.come_back_download_menu.connect(self.show_download_window)


    def show_image_window(self, file_path):
        self.setWindowTitle("Обработка изображения")
        StackCntrl.clear_stacked_widget(self.stack)

        widget_instance = ShowImageWindow(file_path)
         
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)
        widget_instance.come_back.connect(self.show_download_window)
        widget_instance.go_to_processing.connect(self.show_processing_window)
        
       
    def add_item_to_stack(self, title, class_name):
        """Добавляет новый виджет в QStackedWidget и устанавливает его как текущий."""
        self.setWindowTitle(title)
        StackCntrl.clear_stacked_widget(self.stack)  # Очищаем стек перед добавлением нового виджета

        widget_instance = class_name()  
         
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)

        return widget_instance


    
      