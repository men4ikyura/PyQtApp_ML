from mainWindow.mainUI import MainUI
from PyQt6.QtWidgets import QMainWindow


# class MainController(QMainWindow, MainUI):
#     def __init__(self):
#         super().__init__()
#         self.setup_main_ui()

class MainController(QMainWindow, MainUI):
    def __init__(self):
        QMainWindow.__init__(self)  # Явный вызов инициализатора QMainWindow
        MainUI.__init__(self)  # Явный вызов инициализатора MainUI

        # Устанавливаем центральный виджет
        self.setCentralWidget(self.setup_main_ui())
        self.setWindowTitle("Главное окно")
        self.resize(600, 400)