from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QInputDialog
from PyQt6.QtGui import QPixmap, QPainter, QPolygon, QPen, QColor, QGuiApplication
from PyQt6.QtCore import Qt, pyqtSignal, QPoint, QSize
from PIL import Image
from datetime import datetime
import csv
import os

class FinishImageWindow(QWidget):
    
    come_back_download_menu = pyqtSignal()
    file_name_entered = pyqtSignal(str)

    def __init__(self, info_drops, file_path):
        super().__init__()
        self.info_drops = info_drops
        self.file_path = file_path
        main_layout = QVBoxLayout() 
        count_drops = QLabel(self)
        count_drops.setText(f"Количество капель: {self.info_drops[0]}")
        self.saving_btn = QPushButton("Сохранить в файл")
        self.saving_btn.clicked.connect(self.show_input_dialog)
        self.file_name_entered.connect(self.save_info_in_file)
        self.come_back_to_download_menu_btn = QPushButton("Назад в меню загрузки")
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_download_menu)
        self.come_back_to_download_menu_btn.setFixedSize(300, 30)
        self.saving_btn.setFixedSize(300, 30)
        main_layout.addWidget(count_drops, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.come_back_to_download_menu_btn,  alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.saving_btn,  alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)  
        self.width_file, self.height_file, self.koef = self.count_sizes()
        self.width_window, self.height_window = self.width_file, self.height_file
        

    def sizeHint(self):
        # Возвращает размер, основываясь на содержимом (в данном случае - 800x800)
        return QSize(self.width_window, self.height_window)


    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.file_path)
        scaled_pixmap = pixmap.scaled(self.width_file, self.height_file, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        painter.drawPixmap(0, 0, scaled_pixmap)
        

        pen_line = QPen()
        pen_line.setWidth(3)
        pen_line.setColor(QColor(0, 128, 255))  # Синий цвет для полилинии
        painter.setPen(pen_line)

        # Рисуем полилинию
        if self.info_drops[0] != 0:
            for info in self.info_drops[1]:
                masks = []

                for coordinate in info[0]:
                    masks.append(QPoint(int(coordinate[0] * self.koef), int(coordinate[1] * self.koef)))
                masks.append(QPoint(int(info[0][0][0] * self.koef), int(info[0][0][1] * self.koef)))
                center = QPoint(int(info[2][0] * self.koef), int(info[2][1] * self.koef))
                painter.drawEllipse(center, 2, 2)
                # Рисуем полилинию
                polygon = QPolygon(masks)
                painter.drawPolyline(polygon)

        painter.end()


    def count_sizes(self):
        screen = QGuiApplication.primaryScreen()

        # Получение размеров экрана
        screen_size = screen.geometry()
        width_screen = screen_size.width() - 500
        height_screen = screen_size.height() - 300

        with Image.open(self.file_path) as img:
            width_file, height_file = img.size 

        less_width = width_file <= width_screen 
        less_height = height_file <= height_screen

        if less_width and less_height:
            # Изображение умещается на экране
            koef = 1
        else:
            # Рассчитываем коэффициенты уменьшения
            koef_width =  width_screen / width_file
            koef_height =   height_screen / height_file
            koef = min(koef_width, koef_height)  # Берем минимальный коэффициент для сохранения пропорций

        # Вычисляем новые размеры
        new_width_file = int(width_file * koef)
        new_height_file = int(height_file * koef)

        return new_width_file, new_height_file, koef


    def save_info_in_file(self, path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["area", "coordinate center x", "coordinate center y"])
            for row in self.info_drops[1]:
                writer.writerow([coordinate for coordinate in row[2]] + [row[1]])
        QMessageBox.information(self, "Файл успешно создан", "Результаты обработки записаны в файл")


    def show_input_dialog(self):
        results_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))), 'results')
        os.makedirs(results_folder, exist_ok=True)
        text, ok = QInputDialog.getText(None, "Введите имя файла", "Имя файла:")
        
        if ok:
            if text != '':
                path = os.path.join(results_folder, f"{text}.csv")
                if not os.path.exists(path):
                    self.file_name_entered.emit(path)
                else:
                    QMessageBox.information(self, "Файл с таким именем уже существует", "Файл с таким именем уже существует")
            else:
                self.file_name_entered.emit(os.path.join(results_folder, f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"))

        
    def emit_come_back_download_menu(self):
        self.come_back_download_menu.emit()
