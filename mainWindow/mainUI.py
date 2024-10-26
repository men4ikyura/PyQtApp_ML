from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt


# class MainUI:
#     def __init__(self):
#         # super().__init__()
#         self.download_btn = QPushButton("Загрузить изображение")
#         self.show_hst_btn = QPushButton("Показать историю результатов")
#         self.setting_btn = QPushButton("Настройки приложения")
#         self.layout_main = QVBoxLayout()

        
#     def setup_main_ui(self):
#         self.resize(600, 600)
#         self.setWindowTitle("Главная страница")
#         title = QLabel("здарова это приложение команды восход загружаете")
#         self.download_btn.setFixedSize(300, 30)
#         self.setting_btn.setFixedSize(300, 30)
#         self.show_hst_btn.setFixedSize(300, 30)

#         self.layout_main.addWidget(self.download_btn, alignment=Qt.AlignmentFlag.AlignCenter)
#         self.layout_main.addWidget(self.show_hst_btn, alignment=Qt.AlignmentFlag.AlignCenter)
#         self.layout_main.addWidget(self.setting_btn, alignment=Qt.AlignmentFlag.AlignCenter)
#         self.layout_main.addSpacing(40)
#         self.layout_main.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
#         self.layout_main.addStretch()
  
#         central_widget = QWidget()
#         central_widget.setLayout(self.layout_main)
#         self.setCentralWidget(central_widget)


class MainUI:
    def __init__(self):
        self.download_btn = QPushButton("Загрузить изображение")
        self.show_hst_btn = QPushButton("Показать историю результатов")
        self.setting_btn = QPushButton("Настройки приложения")

        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.download_btn)
        self.layout_main.addWidget(self.show_hst_btn)
        self.layout_main.addWidget(self.setting_btn)

    def setup_main_ui(self):
        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        return central_widget 
