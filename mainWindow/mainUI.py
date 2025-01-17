from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.download_btn = QPushButton("Загрузить изображение")
        self.documentation_btn = QPushButton("Документация")
        self.show_hst_btn = QPushButton("Показать историю результатов")
        self.setting_btn = QPushButton("Настройки приложения")
        self.layout_main = QVBoxLayout()
        self.resize(600, 300)

    def setup_main_ui(self):
        self.setWindowTitle("Главная страница")
        title = QLabel("Приложение \"Voshod\"для подсчета капель на изображении\nс помощью технологии YOLOv11.\nЗагрузите изображение и начните обработку.\nДалее после обработки вам будет доступна такая информация как,\nколичество капель, график распределения площадей.\nТакже будет возможность сохранить результаты в csv файл.")
        self.download_btn.setFixedSize(300, 30)
        self.setting_btn.setFixedSize(300, 30)
        self.show_hst_btn.setFixedSize(300, 30)
        self.documentation_btn.setFixedSize(300, 30)

        self.layout_main.addWidget(
            self.download_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addWidget(
            self.documentation_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addWidget(
            self.show_hst_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addWidget(
            self.setting_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addSpacing(40)
        self.layout_main.addWidget(
            title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        self.setCentralWidget(central_widget)
