import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600, 600)
        self.setWindowTitle("Главная страница")

        download_btn = QPushButton("Загрузить изображение")
        show_hst_btn = QPushButton("Показать историю результатов")
        download_btn.setFixedSize(300, 30)
        show_hst_btn.setFixedSize(300, 30)

        layout = QVBoxLayout()
        layout.addWidget(download_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(show_hst_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(10)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

