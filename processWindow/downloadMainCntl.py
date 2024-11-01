from processWindow.downloadMainUI import DownloadMainWindowUI
from PyQt6.QtWidgets import QFileDialog, QStackedWidget
from PyQt6.QtWidgets import QMainWindow
from stackCntrl.stackCntrl import StackCntrl

class DownloadMainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.come_back_main_menu_btn = 0
        self.stack = QStackedWidget()
        self.setup_start_downaload_ui()
        self.setCentralWidget(self.stack)
        self.resize(600, 600)

    
    def setup_start_downaload_ui(self):
        self.add_item_to_stack(DownloadMainWindowUI)
        

    
    def add_item_to_stack(self,  class_name):
        """Добавляет новый виджет в QStackedWidget и устанавливает его как текущий."""

        StackCntrl.clear_stacked_widget(self.stack)  # Очищаем стек перед добавлением нового виджета

        # Создаем экземпляр переданного класса
        widget_instance = class_name()  
        self.stack.addWidget(widget_instance)
        self.stack.setCurrentWidget(widget_instance)

        if class_name.__name__  == "DownloadMainWindowUI":
            self.come_back_main_menu_btn = widget_instance.come_back_main_menu_btn

        



        
