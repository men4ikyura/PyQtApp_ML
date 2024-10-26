from mainWindow.mainUI import MainUI
from PyQt6.QtWidgets import QMainWindow

class MainController(MainUI):
    def __init__(self):
        super().__init__()
        self.setup_main_ui()