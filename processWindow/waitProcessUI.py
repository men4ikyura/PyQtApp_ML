from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from scripts_yolo.methods_new import main
from PyQt5.QtCore import QObject, pyqtSignal, QSize
from PIL import Image
import tempfile
import os
import uuid

class ProcessingWindow(QWidget):
    result_ready = pyqtSignal(list, str)
    come_back_show_image = pyqtSignal(str, float, float, bool, int, float)
    # forcdly_finished = pyqtSignal()

    def __init__(self, file_path, *args):
        super().__init__()
        self.file_path = file_path
        self.args = args
        self.setWindowTitle("Обработка изображения")
        self.main_layout = QVBoxLayout()
        self.title_label = QLabel(
            "Идёт обработка изображения, пожалуйста, подождите...")
        self.title_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; text-align: center;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)
        self.resize(600, 400)
        self.setLayout(self.main_layout)
        self.thread_procces = None
        self.worker_procces = None

    def sizeHint(self):
        return QSize(self.width(), self.height())

    def showEvent(self, event):
        super().showEvent(event)
        self.setup_thread()

    def setup_thread(self):
        self.thread_procces = QThread()
        self.worker_procces = WorkerProcces(self.file_path, self.args)
        self.worker_procces.moveToThread(self.thread_procces)
        self.worker_procces.error_call.connect(self.show_mistake)
        self.thread_procces.started.connect(self.worker_procces.run)
        self.worker_procces.result_ready.connect(self.result_ready)
        self.worker_procces.finished.connect(self.thread_procces.quit)
        self.worker_procces.finished.connect(self.worker_procces.deleteLater)
        self.thread_procces.finished.connect(self.thread_procces.deleteLater)
        self.thread_procces.start()

    def show_mistake(self, info_error):
        self.come_back_show_image.emit(self.file_path, *self.args)
        QMessageBox.information(self, "Erorr", f"{
                                info_error}\nОшибка обработки, попробуй-те поменять параметры")


class WorkerProcces(QObject):
    result_ready = pyqtSignal(list, str)
    finished = pyqtSignal()
    error_call = pyqtSignal(str)

    def __init__(self, file_path, args):
        super().__init__()
        self.file_path = file_path
        self.args = args

    def run(self):
        try:
            path_formate_image = self.find_filled_areas(self.file_path)
            result = main(path_formate_image, *self.args)
            self.result_ready.emit(result, path_formate_image)
        except Exception as e:
            self.error_call.emit(f"{e}")
        finally:
            self.finished.emit()

    def find_filled_areas(self, file_path):
        with Image.open(file_path) as img:
            gray_image = img.convert("L")
            threshold = 30
            bw_image = gray_image.point(lambda p: p > threshold and 255)
            bbox = bw_image.getbbox()

            if bbox:
                gray_image = img.crop(bbox)


            if not os.path.exists("./tmp"):
                os.makedirs("./tmp")

            filename = f"{uuid.uuid4()}.jpg"
            temp_file_path = f"./tmp/{filename}"
            gray_image.save(temp_file_path)
            return temp_file_path
