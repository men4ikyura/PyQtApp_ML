from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class DownloadMainWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.come_back_main_menu_btn = QPushButton("Назад")
        self.open_file_button = QPushButton("Выбрать файл", self)
        self.open_file_button.setGeometry(150, 80, 100, 30)
        self.file_label = QLabel(self)
        self.file_label.setGeometry(50, 120, 500, 30)
        self.come_back_to_download_menu_btn = QPushButton("Назад")
        self.central_widget = QWidget()
        self.setup_start_downaload_ui()
        self.connect_signals()
    

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
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*.*)")
        self.setup_before_process_image_ui(file_path)


    def setup_before_process_image_ui(self, file_path):
        if file_path:
            layout2 =  QVBoxLayout()
            self.file_label.setText(f"Выбранный файл: {file_path}")
            pixmap = QPixmap(file_path)
            width, height = 300, 300  # Укажите желаемые размеры
            scaled_pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            label = QLabel()
            label.setPixmap(scaled_pixmap)
            layout2.addWidget(label)
            layout2.addWidget(self.come_back_to_download_menu_btn)
            central_widget = QWidget()
            central_widget.setLayout(layout2)
            self.setCentralWidget(central_widget)

        else:
            self.file_label.setText("Файл не выбран")
        
        

    # Настройка размеров окна под изображение
       
        # self.resize(pixmap.width(), pixmap.height())



