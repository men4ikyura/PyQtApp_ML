from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QFileDialog, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, Qt, QLocale
import pyqtgraph as pg
import numpy as np
from PyQt5.QtGui import QDoubleValidator
import csv
import pandas as pd


class GraphicsDraw(QWidget):

    come_back_download_menu = pyqtSignal()
    file_name_entered = pyqtSignal(str)

    def __init__(self, info_drops):
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.info_drops = info_drops
        self.diametrs = self.get_diameters(self.info_drops)
        locale = QLocale(QLocale.Language.English,
                         QLocale.Country.UnitedStates)
        QLocale.setDefault(locale)
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
        self.saving_btn.clicked.connect(self.save_file)
        self.come_back_to_download_menu_btn = QPushButton(
            "Назад в меню загрузки")
        self.come_back_to_download_menu_btn.setFixedSize(250, 30)
        self.come_back_to_download_menu_btn.clicked.connect(
            self.emit_come_back_download_menu)
        hz_layout.addWidget(count_drops)
        hz_layout.addWidget(self.saving_btn)
        hz_layout.addWidget(self.come_back_to_download_menu_btn)
        vr_layout = QVBoxLayout()
        vr_layout.addLayout(hz_layout)
        vr_layout.addWidget(self.graphWidget)
        # кнопка для перерисовки графика
        self.redraw_graphic_btn = QPushButton("Перерисовать график")
        self.redraw_graphic_btn.clicked.connect(self.redraw_graphic)
        # поле для инпута шага
        self.label_imgsz = QLabel(self)
        self.label_imgsz.setText("Шаг величины диаметра")
        self.label_imgsz.setMaximumWidth(200)
        self.line_edit = QLineEdit(self)
        self.line_edit.setText('0.2')
        self.older_line_edit = float(self.line_edit.text())
        self.line_edit.setMaximumWidth(150)
        validator = QDoubleValidator(0.0, 4000.0, 2, self)
        self.line_edit.setValidator(validator)
        self.layout3 = QHBoxLayout()
        self.layout3.addWidget(self.label_imgsz)
        self.layout3.addWidget(self.line_edit)
        self.layout3.addWidget(self.redraw_graphic_btn)
        self.layout3.setAlignment(self.line_edit, Qt.AlignmentFlag.AlignLeft)
        vr_layout.addLayout(self.layout3)
        self.setLayout(vr_layout)
        counts, ranges = self.redo_range(
            self.diametrs, float(self.line_edit.text()))
        self.plot_graph(counts, ranges)

    def redraw_graphic(self):
        if float(self.line_edit.text()) != self.older_line_edit:
            counts, ranges = self.redo_range(
                self.diametrs, float(self.line_edit.text()))
            self.plot_graph(counts, ranges)
            self.older_line_edit = float(self.line_edit.text())

    def plot_graph(self, counts, ranges):
        x = np.arange(len(counts))
        bar_item = pg.BarGraphItem(x=x, height=counts, width=0.4, brush='r')
        self.graphWidget.clear()
        self.graphWidget.addItem(bar_item)
        axis = self.graphWidget.getAxis('bottom')
        ticks = [(i, f'{ranges[i]:.1f}-{ranges[i+1]:.1f}')
                 for i in range(len(ranges) - 1)]
        axis.setTicks([ticks])
        self.graphWidget.setTitle("Гистограмма распределения площадей капель")
        self.graphWidget.setLabel('left', "Количество капель")
        self.graphWidget.setLabel('bottom', "Площадь капли (микроны)")

    def get_diameters(self, info_drops):
        diametrs = [row[1] for row in info_drops[1]]
        diametrs.sort()
        return diametrs

    def redo_range(self, diametrs, step):
        ranges = np.arange(diametrs[0], diametrs[-1] + step, step)
        binned = pd.cut(diametrs, bins=ranges, right=False)
        counts = pd.Series(binned).value_counts().sort_index().tolist()
        return counts, ranges

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить CSV файл",
            "",
            "CSV файлы (*.csv);;Все файлы (*)"
        )
        if file_path:
            if not file_path.endswith(".csv"):
                file_path += ".csv"
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["diametr (micrometer)", "coordinate center x", "coordinate center y"])
                for row in self.info_drops[1]:
                    writer.writerow([row[1]] + [row[2][0], row[2][1]])

    def emit_come_back_download_menu(self):
        self.come_back_download_menu.emit()
