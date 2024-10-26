from downloadWindow.downloadUI import DownloadWindowUI
from PyQt6.QtWidgets import QFileDialog

class DownloadController(DownloadWindowUI):
    def __init__(self):
        super().__init__()
        self.setup_settings_ui()
        self.open_file_button.clicked.connect(self.open_file)
        
    def open_file(self):
        # Открытие диалога выбора файла
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*.*)")
        
        # Проверка, что файл выбран
        if file_path:
            self.file_label.setText(f"Выбранный файл: {file_path}")
        else:
            self.file_label.setText("Файл не выбран")



        
