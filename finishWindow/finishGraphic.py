from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QInputDialog, QHBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal
import pyqtgraph as pg
import numpy as np
import os
import csv
import datetime

class GraphicsDraw(QWidget):
    come_back_download_menu = pyqtSignal()

    def __init__(self, info_drops):
        super().__init__()
        self.info_drops = info_drops
        self.graphWidget = pg.PlotWidget()
        self.info_drops = info_drops
        self.setWindowTitle("График")
        hz_layout = QHBoxLayout() 
        hz_layout.setContentsMargins(0, 0, 0, 0)
        hz_layout.setSpacing(4)
        count_drops = QLabel(self)
        count_drops.setText(f"Количество капель: {self.info_drops[0]}")
        self.come_back_to_download_menu_btn = QPushButton("Назад в меню загрузки")
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_download_menu)
        hz_layout.addWidget(count_drops)
        hz_layout.addWidget(self.come_back_to_download_menu_btn)
        hz_layout.addWidget(self.saving_btn)
        layout = QVBoxLayout()
        layout.addLayout(hz_layout)
        layout.addWidget(self.graphWidget)
        self.setLayout(layout)

        # Строим график
        self.plot_graph()


    def plot_graph(self):
        # Пример данных для гистограммы
        categories = ['20-40', '40-60', '60-80', '80-100', '100-120'] #20(пример) км шаг
        values = [10, 15, 7, 12, 5] #частота 
        # чтобы шаг и частота соответствовали по индексам

        # Позиции для столбцов
        x = np.arange(len(categories))

        # Создаем BarGraphItem
        bar_item = pg.BarGraphItem(x=x, height=values, width=0.6, brush='r')

        # Добавляем BarGraphItem на график
        self.graphWidget.addItem(bar_item)

        # Настройка оси X
        axis = self.graphWidget.getAxis('bottom')  # Получаем ось X
        axis.setTicks([[(i, categories[i]) for i in range(len(categories))]])

        # Добавляем заголовок
        self.graphWidget.setTitle("Гистограмма")

        def save_info_in_file(self, path):
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["area", "coordinate center x", "coordinate center y"])
                for row in self.info_drops[1]:
                    writer.writerow([coordinate for coordinate in row[2]] + [row[1]])
            QMessageBox.information(self, "Файл успешно создан", "Результаты обработки записаны в файл")


    def show_input_dialog(self):
        # results_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))), 'results')
        # os.makedirs(results_folder, exist_ok=True)
        results_folder = '/Users/yurazhilin/Desktop/pyQtApp'
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
