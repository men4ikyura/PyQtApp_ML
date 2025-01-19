from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QSlider, QHBoxLayout, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal, QLocale
from PyQt5.QtGui import QIntValidator, QDoubleValidator
import json
import os


class SettingsUI(QWidget):

    come_back = pyqtSignal()

    def __init__(self):
        super().__init__()

        
        self.data = self.load_data()
        self.setup_settings_ui()
        


    def setup_settings_ui(self):
        locale = QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        QLocale.setDefault(locale)
        # settings button
        self.come_back_main_menu_btn = QPushButton("Назад")
        self.come_back_main_menu_btn.setFixedSize(300, 30)
        self.come_back_main_menu_btn.clicked.connect(self.emit_come_back_signal)

        # settings saving button
        self.save_settings_button = QPushButton("Сохранить настройки")
        self.save_settings_button.setFixedSize(300, 30)
        self.save_settings_button.clicked.connect(self.update_parametrs)

        layout = QVBoxLayout(self)
        title = QLabel("Установите параметры по умолчанию")


        #settings iou
        self.iou = self.data.get("iou", 0.7)
        self.slider_iou = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_iou.setMaximumWidth(150)
        self.slider_iou.setRange(0, 100)
        self.slider_iou.setValue(int(self.iou*100))
        self.slider_iou.valueChanged.connect(self.update_iou)
        self.result_label_iou = QLabel(f'iou: {self.iou}', self)
        self.label_iou = QHBoxLayout()
        self.label_iou.addWidget(self.result_label_iou)
        self.label_iou.addWidget(self.slider_iou)
        self.label_iou.setAlignment(self.slider_iou, Qt.AlignmentFlag.AlignLeft)

        #setting conf 
        self.conf = self.data.get("conf", 0.25)
        self.slider_conf = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_conf.setMaximumWidth(150)
        self.slider_conf.setRange(0, 100)
        self.slider_conf.setValue(int(self.conf*100))
        self.slider_conf.valueChanged.connect(self.update_conf)
        self.result_label_conf = QLabel(f'conf: {self.conf}', self)
        self.label_conf = QHBoxLayout()
        self.label_conf.addWidget(self.result_label_conf)
        self.label_conf.addWidget(self.slider_conf)
        self.label_conf.setAlignment(self.slider_conf, Qt.AlignmentFlag.AlignLeft)

        #setting imgsz 
        self.imgsz = self.data.get("imgsz", 640)
        self.result_label_imgsz = QLabel(self)
        self.result_label_imgsz.setText("imgsz")
        self.result_label_imgsz.setMaximumWidth(50)
        self.line_edit_imgsz = QLineEdit()
        self.line_edit_imgsz.setText(str(self.imgsz))
        self.line_edit_imgsz.setMaximumWidth(150)
        validator = QIntValidator(0, 4000, self)  
        self.line_edit_imgsz.setValidator(validator)
        self.label_imgsz = QHBoxLayout() 
        self.label_imgsz.addWidget(self.result_label_imgsz)
        self.label_imgsz.addWidget(self.line_edit_imgsz)
        self.label_imgsz.setAlignment(self.line_edit_imgsz, Qt.AlignmentFlag.AlignLeft)

        #settings pixels
        self.pixels = self.data.get("pixels", 7.5)
        self.result_label_pixels = QLabel(self)
        self.result_label_pixels.setText("Количесвто пикселей в микроне")
        self.result_label_pixels.setMaximumWidth(250)
        self.line_edit_pixels = QLineEdit(self)
        self.line_edit_pixels.setText(str(self.pixels))
        self.line_edit_pixels.setMaximumWidth(150)
        validator = QDoubleValidator(0.0, 50.0, 2, self)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        validator.setRange(0.0, 50.0, 2)
        self.line_edit_pixels.setValidator(validator)
        self.label_pixels = QHBoxLayout() 
        self.label_pixels.addWidget(self.result_label_pixels)
        self.label_pixels.addWidget(self.line_edit_pixels)
        self.label_pixels.setAlignment(self.line_edit_pixels, Qt.AlignmentFlag.AlignLeft)

        #settings retina_masks
        self.retina_masks = self.data.get("retina_masks", False)
        self.retina_masks_box = QCheckBox("retina_masks")
        self.retina_masks_box.setChecked(self.retina_masks)

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(self.label_conf)
        layout.addLayout(self.label_iou)
        layout.addLayout(self.label_imgsz)
        layout.addWidget(self.retina_masks_box)
        layout.addLayout(self.label_pixels)
        layout.addWidget(self.save_settings_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.come_back_main_menu_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        layout.addStretch() 
        self.setLayout(layout)
        # self.setCentralWidget(central_widget)

    def update_imgsz(self, value):
        self.result_label_imgsz.setText(f'imgsz: {value * 100}')

    def update_conf(self, value):
        self.result_label_conf.setText(f'conf: {value / 100}') 

    def update_iou(self, value):
        self.result_label_iou.setText(f'iou: {value / 100}')  

    @staticmethod
    def create_settings_file():
        with open("./settings.json", "w") as file:
            default_parametrs = {
                "iou": 0.7,
                "conf": 0.25,
                "retina_masks": False,
                "imgsz": 640,
                "pixels": 7.5
            }
            json.dump(default_parametrs, file, ensure_ascii=False,  indent=4)


    def load_data(self):
        with open("./settings.json") as file:
            return json.load(file)
                
    def update_parametrs(self):
        with open("./settings.json", "w") as file:
            new_parametrs = {
                "iou": self.slider_iou.value() / 100,
                "conf": self.slider_conf.value() / 100,
                "retina_masks": self.retina_masks_box.isChecked(),
                "imgsz": int(self.line_edit_imgsz.text()),
                "pixels": float(self.line_edit_pixels.text())
            }
            json.dump(new_parametrs, file, ensure_ascii=False,  indent=4)
    
    def emit_come_back_signal(self):
        self.come_back.emit() 
        