import sys
import time
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from test import get_process_result


class ScriptController(QObject):
    # Сигнал для уведомления, что результат готов
    result_ready = pyqtSignal(dict)

    def __init__(self, file_path):
        super().__init__()
        

    def run(self):
        result = get_process_result(self.file_path)
        self.result_ready.emit(result)

    def handle_result(self, result):
        print("Результат готов:", result)
        
        # Завершаем поток
        self.thread.quit()
        self.thread.wait()


