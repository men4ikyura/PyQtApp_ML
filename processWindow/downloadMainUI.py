from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal
from processWindow.showImageWnd import ShowImageWindow



class DownloadMainWindowUI(QMainWindow):

    come_back = pyqtSignal()
    file_selected = pyqtSignal(str) 

    def __init__(self):
        super().__init__()
       
        self.come_back_main_menu_btn = QPushButton("Назад")
        self.open_file_button = QPushButton("Выбрать файл", self)
        self.open_file_button.setGeometry(150, 80, 100, 30)
        self.come_back_main_menu_btn.clicked.connect(self.emit_come_back_signal)
        self.central_widget = QWidget()
        self.setup_start_downaload_ui()
        self.connect_signals()
        self.file_path = None
        
    

    def connect_signals(self):
        self.open_file_button.clicked.connect(self.open_file)
        

    def setup_start_downaload_ui(self):
        
        title = QLabel("Загрузить фотографию")
        layout1 =  QVBoxLayout()
        layout1.addWidget(title)
        layout1.addWidget(self.come_back_main_menu_btn)               
        layout1.addWidget(self.open_file_button) 

        central_widget = QWidget()
        central_widget.setLayout(layout1)
        self.setCentralWidget(central_widget)


    def open_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*.*)")
        if self.file_path:  # Проверяем, был ли выбран файл
            self.file_selected.emit(self.file_path)


    def emit_come_back_signal(self):
        self.come_back.emit() 

        
        

    # Настройка размеров окна под изображение
       
        # self.resize(pixmap.width(), pixmap.height())



