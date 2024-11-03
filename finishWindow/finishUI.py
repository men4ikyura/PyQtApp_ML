from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal


class FinishImageWindow(QWidget):
    
    come_back_download_menu = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Завершение обработки изображения")
        main_layout = QVBoxLayout()    
        title_label = QLabel("Обработка завершена")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(200, 200) 
        pixmap.fill(Qt.GlobalColor.lightGray) 
        self.image_label.setPixmap(pixmap)
        self.info_label = QLabel("Ваше изображение успешно обработано!")
        self.info_label.setStyleSheet("font-size: 16px; text-align: center;")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.come_back_to_download_menu_btn = QPushButton("Назад в меню загрузки")
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_download_menu)
        self.come_back_to_download_menu_btn.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")
        main_layout.addWidget(title_label)
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.info_label)
        main_layout.addWidget(self.come_back_to_download_menu_btn)
        self.setLayout(main_layout)  


    def emit_come_back_download_menu(self):
        self.come_back_download_menu.emit()
