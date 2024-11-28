from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QFileDialog, QHBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, Qt
import pyqtgraph as pg
import numpy as np
from PyQt6.QtGui import QIntValidator
import csv
import datetime

class GraphicsDraw(QWidget):

    come_back_download_menu = pyqtSignal()
    file_name_entered = pyqtSignal(str)

    def __init__(self, info_drops):
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.info_drops = info_drops
        hz_layout = QHBoxLayout() 
        vr_layout = QVBoxLayout()
        vr_layout.setContentsMargins(0, 0, 0, 0)
        vr_layout.setSpacing(0)
        hz_layout.setContentsMargins(0, 0, 0, 0)
        hz_layout.setSpacing(4)
        count_drops = QLabel(self)
        count_drops.setText(f"Количество капель: {info_drops[0]}")
        self.saving_btn = QPushButton("Сохранить результаты")
        self.saving_btn.setFixedSize(250, 30)
        # self.saving_btn.clicked.connect(self.show_input_dialog)
        self.saving_btn.clicked.connect(self.save_file)
        self.come_back_to_download_menu_btn = QPushButton("Назад в меню загрузки")
        self.come_back_to_download_menu_btn.setFixedSize(250, 30)
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_download_menu)
        # self.file_name_entered.connect(self.save_info_in_file)
        hz_layout.addWidget(count_drops)
        hz_layout.addWidget(self.saving_btn)
        hz_layout.addWidget(self.come_back_to_download_menu_btn)
        vr_layout = QVBoxLayout()
        vr_layout.addLayout(hz_layout)
        vr_layout.addWidget(self.graphWidget)
        # кнопка для перерисовки графика
        self.redraw_graphic_btn = QPushButton("Перерисовать график")
        # self.redraw_graphic_btn.clicked.connect(self.plot_graph2)
        #поле для инпута шага
        self.label_imgsz = QLabel(self)
        self.label_imgsz.setText("Шаг величины диаметра")
        self.label_imgsz.setMaximumWidth(200)
        self.line_edit = QLineEdit(self)
        self.line_edit.setText('20')
        self.line_edit.setMaximumWidth(150)
        validator = QIntValidator(0, 4000, self)  
        self.line_edit.setValidator(validator)
        self.layout3 = QHBoxLayout() 
        self.layout3.addWidget(self.label_imgsz)
        self.layout3.addWidget(self.line_edit)
        self.layout3.addWidget(self.redraw_graphic_btn)
        self.layout3.setAlignment(self.line_edit, Qt.AlignmentFlag.AlignLeft)
        vr_layout.addLayout(self.layout3)
        self.setLayout(vr_layout)

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

    # def plot_graph2(self):
    #     # Пример данных для гистограммы
    #     categories = ['30-40', '43-60', '60-80', '80-130', '100-120'] #20(пример) км шаг
    #     values = [10, 15, 7, 12, 5] #частота 
    #     # чтобы шаг и частота соответствовали по индексам

    #     # Позиции для столбцов
    #     x = np.arange(len(categories))

    #     # Создаем BarGraphItem
    #     bar_item = pg.BarGraphItem(x=x, height=values, width=0.6, brush='r')

    #     # Добавляем BarGraphItem на график
    #     self.graphWidget.addItem(bar_item)

    #     # Настройка оси X
    #     axis = self.graphWidget.getAxis('bottom')  # Получаем ось X
    #     axis.setTicks([[(i, categories[i]) for i in range(len(categories))]])

    #     # Добавляем заголовок
    #     self.graphWidget.setTitle("Гистограмма")


    def save_file(self):
        # Открыть диалоговое окно для сохранения файла
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Сохранить CSV файл", 
            "",  # Путь по умолчанию
            "CSV файлы (*.csv);;Все файлы (*)"  # Фильтр для CSV
        )
        if file_path:  # Если путь выбран
            # Убедимся, что файл сохраняется с расширением .csv
            if not file_path.endswith(".csv"):
                file_path += ".csv"
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["area", "coordinate center x", "coordinate center y"])
                for row in self.info_drops[1]:
                    writer.writerow([coordinate for coordinate in row[2]] + [row[1]])

    # def save_info_in_file(self, path):
    #     with open(path, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["area", "coordinate center x", "coordinate center y"])
    #         for row in self.info_drops[1]:
    #             writer.writerow([coordinate for coordinate in row[2]] + [row[1]])
    #     QMessageBox.information(self, "Файл успешно создан", "Результаты обработки записаны в файл")


    # def show_input_dialog(self):
    #     # results_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))), 'results')
    #     # os.makedirs(results_folder, exist_ok=True)
    #     results_folder = '/Users/yurazhilin/Desktop/pyQtApp'
    #     text, ok = QInputDialog.getText(None, "Введите имя файла", "Имя файла:")
        
    #     if ok:
    #         if text != '':
    #             path = os.path.join(results_folder, f"{text}.csv")
    #             if not os.path.exists(path):
    #                 self.file_name_entered.emit(path)
    #             else:
    #                 QMessageBox.information(self, "Файл с таким именем уже существует", "Файл с таким именем уже существует")
    #         else:
    #             self.file_name_entered.emit(os.path.join(results_folder, f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"))


    # def save_info_in_file(self, path):
    #     with open(path, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["area", "coordinate center x", "coordinate center y"])
    #         for row in self.info_drops[1]:
    #             writer.writerow([coordinate for coordinate in row[2]] + [row[1]])
    #     QMessageBox.information(self, "Файл успешно создан", "Результаты обработки записаны в файл")


    def emit_come_back_download_menu(self):
        self.come_back_download_menu.emit()