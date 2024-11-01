from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from test import modificated_image

class FinishImageWindow(QWidget):
    
    come_back = pyqtSignal()
      # Измените здесь на QWidget
    def __init__(self, file_path):
        super().__init__()  # Добавьте вызов родительского конструктора
        self.file_label = QLabel(self)
        self.come_back_to_download_menu_btn = QPushButton("Выбрать другой файл") # Подключаем кнопку "Назад"
        self.set_finish_ui(file_path)
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_signal)

    def set_finish_ui(self, file_path):
        if file_path:
            layout2 = QVBoxLayout()
            self.file_label.setText(f"Выбранный файл: {file_path}")
            pixmap = QPixmap(file_path)
            width, height = 300, 300 
            scaled_pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            image_label = QLabel(self)
            image_label.setPixmap(scaled_pixmap)
            layout2.addWidget(self.file_label)
            layout2.addWidget(image_label)
            layout2.addWidget(self.come_back_to_download_menu_btn)

            self.setLayout(layout2)  # Устанавливаем layout для текущего виджета
            self.resize(400, 400)  # Устанавливаем размер окна

    def emit_come_back_signal(self):
        self.come_back.emit() 
