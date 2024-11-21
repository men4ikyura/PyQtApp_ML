from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal, QThread, QTimer
from methods import main
from PyQt6.QtCore import QObject, pyqtSignal, QSize


class ProcessingWindow(QWidget):
    result_ready = pyqtSignal(list, str)
    come_back_show_image = pyqtSignal(str)

    def __init__(self, file_path):
        super().__init__()

        self.file_path = file_path
        self.setWindowTitle("Обработка изображения")
        self.main_layout = QVBoxLayout()
        self.title_label = QLabel("Идёт обработка изображения, пожалуйста, подождите...")
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)
        self.resize(600, 400)

        self.setLayout(self.main_layout)

        self.thread = None
        self.worker = None

    def sizeHint(self):
        # Возвращает размер, основываясь на содержимом (в данном случае - 800x800)
        return QSize(self.width(), self.height())
    
    def showEvent(self, event):
        super().showEvent(event)
        self.setup_thread()

    def setup_thread(self):
        self.thread = QThread()
        self.worker = Worker(self.file_path)  
        self.worker.moveToThread(self.thread)
        self.worker.error_call.connect(self.show_mistake)
        self.thread.started.connect(self.worker.run)
        self.worker.result_ready.connect(self.result_ready)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
       
    def show_mistake(self):
        self.come_back_show_image.emit(self.file_path)
        QMessageBox.information(self, "Erorr", "Ошибка обработки, попробуй-те поменять параметры")
        


class Worker(QObject):
    result_ready = pyqtSignal(list, str)
    finished = pyqtSignal()
    error_call = pyqtSignal()


    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        
        try: 
            result = main(self.file_path)
            self.result_ready.emit(result, self.file_path)   
        except:
            self.error_call.emit()
        finally:
            self.finished.emit()


        