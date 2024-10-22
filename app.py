from PyQt6.QtWidgets import QApplication
from mainWindow.main_wnd import MainWindow
import sys 


if __name__=="__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show() 
    app.exec()
