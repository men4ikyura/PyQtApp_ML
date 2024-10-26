from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class SettingsUI:
    def __init__(self):

        self.download_btn = QPushButton("Назад")

    def setup_settings_ui(self):

        layout = QVBoxLayout()
        title = QLabel("Это настройки")
        layout.addWidget(title)
        layout.addWidget(self.download_btn)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        