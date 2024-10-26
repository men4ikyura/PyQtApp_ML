from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SettingsUI:
    def __init__(self):
        self.a = 5

    def setup_settings_ui(self):
        self.resize(600, 600)
        self.setWindowTitle("Настройки")

        # Создаем компоновку
        layout = QVBoxLayout()
        title = QLabel("Это настройки")
        layout.addWidget(title)

        # Устанавливаем компоновку на центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
