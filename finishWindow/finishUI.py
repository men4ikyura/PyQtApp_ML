from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QPainter, QPolygon, QPen, QColor
from PyQt6.QtCore import Qt, pyqtSignal, QPoint, QSize
from PIL import Image

class FinishImageWindow(QWidget):
    
    come_back_download_menu = pyqtSignal()



    def __init__(self, info_drops, file_path):
        super().__init__()
        self.info_drops = info_drops
        self.file_path = file_path
        self.setWindowTitle("Завершение обработки изображения")
        main_layout = QVBoxLayout()    
        title_label = QLabel("Обработка завершена")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label = QLabel("Ваше изображение успешно обработано!")
        self.info_label.setStyleSheet("font-size: 16px; text-align: center;")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.come_back_to_download_menu_btn = QPushButton("Назад в меню загрузки")
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_download_menu)
        self.come_back_to_download_menu_btn.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")
        main_layout.addWidget(title_label)
        main_layout.addWidget(self.image_label) 
        main_layout.addWidget(self.info_label)
        main_layout.addWidget(self.come_back_to_download_menu_btn)
        self.setLayout(main_layout)  
        with Image.open(self.file_path) as img:
            width_file, height_file = img.size 
        self.width_file, self.height_file = width_file / 1.5,  height_file / 1.5
        print(self.width_file, self.height_file)

    def sizeHint(self):
        # Возвращает размер, основываясь на содержимом (в данном случае - 800x800)
        return QSize(int(self.width_file), int(self.height_file))


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
        if self.info_drops:
            for info in self.info_drops:
                masks = []

                for coordinate in info[0]:
                    masks.append(QPoint(coordinate[0] / 1.5, coordinate[1] / 1.5))
                masks.append(QPoint(info[0][0][0] / 1.5, info[0][0][1] / 1.5))

                # Рисуем полилинию
                polygon = QPolygon(masks)
                painter.drawPolyline(polygon)

        # Настройки для центра (красный цвет)
        pen_center = QPen()
        pen_center.setWidth(2)
        pen_center.setColor(QColor(255, 0, 0))  # Красный цвет для центра
        painter.setPen(pen_center)  # Устанавливаем новый цвет для центра

        # Устанавливаем кисть для заливки с красным цветом
        painter.setBrush(QColor(255, 0, 0))

        # Рисуем центр
        if self.info_drops:
            for info in self.info_drops:
                center = QPoint(info[2][0] / 1.5, info[2][1] / 1.5)
                painter.drawEllipse(center, 2, 2)

        painter.end()



    def emit_come_back_download_menu(self):
        self.come_back_download_menu.emit()
