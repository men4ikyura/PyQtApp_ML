from PyQt5.QtWidgets import QApplication
from appController.appCntl import AppHandler
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AppHandler()
    main_window.show()
    app.exec()

# pyinstaller -w --icon=icon.ico --name=Voshod app.py
# pyinstaller -w  --icon=icon.ico --add-data "./icon.ico:resources" --add-data "./best.pt:resources" --name=Voshod app.py

# helllo
