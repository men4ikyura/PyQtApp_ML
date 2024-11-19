from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal, QSize


class ShowImageWindow(QWidget):
    
    come_back = pyqtSignal()
    go_to_processing = pyqtSignal(str)
    file_path_signal = pyqtSignal(str)


    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.file_label = QLabel(self)
        self.come_back_to_download_menu_btn = QPushButton("Выбрать другой файл") 
        self.start_process_image_btn = QPushButton("Начать обработку изображения")
        self.setup_before_process_image_ui(self.file_path)
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_signal)
        self.start_process_image_btn.clicked.connect(self.emit_go_to_processing)



    def setup_before_process_image_ui(self, file_path):
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
            layout2.addWidget(self.start_process_image_btn)

            self.setLayout(layout2) 
            self.resize(600, 600) 

    def sizeHint(self):
        # Возвращает размер, основываясь на содержимом (в данном случае - 800x800)
        return QSize(self.width(), self.height())
    
    def emit_file_path_signal(self):
        self.file_path_signal.emit(self.file_path)


    def emit_come_back_signal(self):
        self.come_back.emit() 


    def emit_go_to_processing(self):
        self.go_to_processing.emit(self.file_path) 
