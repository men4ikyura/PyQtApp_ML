from PyQt6.QtWidgets import QApplication
from appController.appCntl import AppHandler
import sys 


if __name__=="__main__":
    app = QApplication(sys.argv)
    main_window = AppHandler()
    main_window.show() 
    app.exec()

