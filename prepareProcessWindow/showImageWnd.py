from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QSlider, QCheckBox, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIntValidator
from PyQt6.QtCore import Qt, pyqtSignal, QSize


class ShowImageWindow(QWidget):
    
    come_back = pyqtSignal()
    go_to_processing = pyqtSignal(str, float, float, bool, int)
    file_path_signal = pyqtSignal(str)


    def __init__(self, file_path, *args):
        super().__init__()
        self.file_path = file_path
        self.file_label = QLabel(self)
        
        if not args:
            self.args = (0.25, 0.70, True, 1280)
        else:
            self.args = args
    
        self.come_back_to_download_menu_btn = QPushButton("Выбрать другой файл") 
        self.start_process_image_btn = QPushButton("Начать обработку изображения")
        
        self.come_back_to_download_menu_btn.clicked.connect(self.emit_come_back_signal)
        self.start_process_image_btn.clicked.connect(self.emit_go_to_processing)
        self.layout2 = QVBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText("Выберите параметры обработки:")
        self.file_label.setText(f"Выбранный файл: {self.file_path}")
        
        self.layout2.addWidget(self.file_label)
        self.layout2.addWidget(self.text)
        

        # слайдер conf
        self.slider_conf = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_conf.setMaximumWidth(150)
        self.slider_conf.setRange(0, 100)
        self.slider_conf.setValue(int(self.args[0]*100))
        self.slider_conf.valueChanged.connect(self.update_conf)
        self.result_label_conf = QLabel(f'conf: {self.args[0]}', self)
        # слайдер iou
        self.slider_iou = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_iou.setMaximumWidth(150)
        self.slider_iou.setRange(0, 100)
        self.slider_iou.setValue(int(self.args[1]*100))
        self.slider_iou.valueChanged.connect(self.update_iou)
        self.result_label_iou = QLabel(f'iou: {self.args[1]}', self)

        #выбор imgsz
        self.label_imgsz = QLabel(self)
        self.label_imgsz.setText("imgsz")
        self.label_imgsz.setMaximumWidth(50)
        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.args[3]))
        self.line_edit.setMaximumWidth(150)
        validator = QIntValidator(0, 4000, self)  
        self.line_edit.setValidator(validator)


        #выбор retina_masks
        self.retina_masks_box = QCheckBox("retina_masks")
        self.retina_masks_box.setChecked(self.args[2])

        

        self.layout2.addWidget(self.result_label_conf)
        self.layout2.addWidget(self.slider_conf)
        #добавление iou
        self.layout2.addWidget(self.result_label_iou)
        self.layout2.addWidget(self.slider_iou)
        #добавление imgsz
        # layout2.addWidget(self.result_label_imgsz)
        # layout2.addWidget(slider_imgsz)
        #добавление retina_masks
        self.layout2.addWidget(self.retina_masks_box)
        self.layout3 = QHBoxLayout() 
        self.layout3.addWidget(self.label_imgsz)
        self.layout3.addWidget(self.line_edit)
        self.layout3.setAlignment(self.line_edit, Qt.AlignmentFlag.AlignLeft)
        self.layout2.addLayout(self.layout3)
        self.setup_before_process_image_ui(self.file_path)
        self.layout2.addWidget(self.come_back_to_download_menu_btn)
        self.layout2.addWidget(self.start_process_image_btn)
        self.setLayout(self.layout2) 
        self.resize(600, 500) 



    def setup_before_process_image_ui(self, file_path):
        if file_path:
            pixmap = QPixmap(file_path)
            width, height = 300, 300 
            scaled_pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            image_label = QLabel(self)
            image_label.setPixmap(scaled_pixmap)
            self.layout2.addWidget(image_label)
             


    def update_imgsz(self, value):
        self.result_label_imgsz.setText(f'imgsz: {value * 100}')

    def update_iou(self, value):
        self.result_label_iou.setText(f'iou: {value / 100}')

    def update_conf(self, value):
        self.result_label_conf.setText(f'conf: {value / 100}')
    

    def sizeHint(self):
        # Возвращает размер, основываясь на содержимом (в данном случае - 800x800)
        return QSize(self.width(), self.height())
    
    # def emit_file_path_signal(self):
    #     self.file_path_signal.emit(self.file_path)

    def emit_come_back_signal(self):
        self.come_back.emit() 


    def emit_go_to_processing(self):
        self.go_to_processing.emit(self.file_path, self.slider_conf.value() / 100, self.slider_iou.value() / 100, self.retina_masks_box.isChecked(), int(self.line_edit.text())) 

