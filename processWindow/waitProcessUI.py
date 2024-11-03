from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal, QTimer, QThread
from test import get_process_result
import time

class ProcessingWindow(QWidget):
    
    come_back_download_menu = pyqtSignal()
    result_ready = pyqtSignal(dict)

    def __init__(self, file_path):
        super().__init__()

        self.file_path = file_path
        self.setWindowTitle("Обработка изображения")
        self.main_layout = QVBoxLayout()
        self.title_label = QLabel()
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)
        self.setLayout(self.main_layout)

        self.dot_count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        
        # Настройка потока
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.result_ready.connect(self.handle_result)
        self.thread.started.connect(self.run)

        # Запуск таймера и потока
        self.timer.start(1000)
        self.thread.start()

    def update_text(self):
        # Обновляем текст метки с добавлением точек
        text = f"Обработка изображения{'.' * self.dot_count}"
        self.title_label.setText(text)
        
        # Увеличиваем количество точек или сбрасываем
        self.dot_count = (self.dot_count + 1) % 4

    def run(self):
        result = get_process_result(self.file_path)
        self.result_ready.emit(result)

    def handle_result(self, result):
        print("Результат готов:", result)
        
        # Остановка таймера и завершение потока
        self.timer.stop()
        self.thread.quit()
        self.thread.wait()