from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal, QThread
from methods_new import main
from PyQt6.QtCore import QObject, pyqtSignal, QSize
from PIL import Image
import tempfile


class ProcessingWindow(QWidget):
    result_ready = pyqtSignal(list, str)
    come_back_show_image = pyqtSignal(str, float, float, bool, int, float)

    def __init__(self, file_path, *args):
        super().__init__()
        self.file_path = file_path
        self.args = args
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
        return QSize(self.width(), self.height())
    
    def showEvent(self, event):
        super().showEvent(event)
        self.setup_thread()

    def setup_thread(self):
        self.thread = QThread()
        self.worker = Worker(self.file_path, self.args)  
        self.worker.moveToThread(self.thread)
        self.worker.error_call.connect(self.show_mistake)
        self.thread.started.connect(self.worker.run)
        self.worker.result_ready.connect(self.result_ready)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
       
    def show_mistake(self):
        self.come_back_show_image.emit(self.file_path, *self.args)
        QMessageBox.information(self, "Erorr", "Ошибка обработки, попробуй-те поменять параметры")
        


class Worker(QObject):
    result_ready = pyqtSignal(list, str)
    finished = pyqtSignal()
    error_call = pyqtSignal()


    def __init__(self, file_path, args):
        super().__init__()
        self.file_path = file_path
        self.args = args
      

    def run(self):
        try: 
            path_formate_image = self.find_filled_areas(self.file_path)
            result = main(path_formate_image, *self.args)
            self.result_ready.emit(result, path_formate_image)   
        except:
            self.error_call.emit()
        finally:
            self.finished.emit()


    def find_filled_areas(self, file_path):
        with Image.open(file_path) as img:
            # Преобразуем изображение в оттенки серого
            gray_image = img.convert("L")

            # Применяем пороговую фильтрацию, чтобы отделить заполненные области (например, значимые пиксели)
            # Порог для выделения "заполненных" областей (чем выше, тем светлее пиксели)
            threshold = 30 # константу сам подобрал на ориг фотках
            bw_image = gray_image.point(lambda p: p > threshold and 255)

            # Используем getbbox(), чтобы найти ограничивающую рамку заполненных областей
            bbox = bw_image.getbbox()  # Возвращает кортеж (left, upper, right, lower)

            if bbox:
                # Обрезаем изображение по найденной рамке
                gray_image = img.crop(bbox)

            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                temp_file_path = temp_file.name  

                # Сохраняем изображение во временный файл
        
                gray_image.save(temp_file_path)
            return temp_file_path
        