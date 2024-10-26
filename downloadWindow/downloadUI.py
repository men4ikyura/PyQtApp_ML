from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtWidgets import QMainWindow

class DownloadWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.come_back_main_menu_btn = QPushButton("Назад")
        self.open_file_button = QPushButton("Выбрать файл", self)
        self.open_file_button.setGeometry(150, 80, 100, 30)

        self.file_label = QLabel(self)
        self.file_label.setGeometry(50, 120, 500, 30)
    

    def setup_settings_ui(self):

        layout = QVBoxLayout()
        title = QLabel("Загрузить фотографию")
        layout.addWidget(title)
        layout.addWidget(self.come_back_main_menu_btn)
        layout.addWidget(self.come_back_main_menu_btn)
        layout.addWidget(title) 
        layout.addWidget(self.open_file_button) 
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)