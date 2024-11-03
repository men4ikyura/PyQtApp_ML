import cv2
from ultralytics import YOLO
import numpy as np
import ipywidgets as widgets
import time



def interactive_plot(file_path, alpha, iou, conf, imgsz):
    model = YOLO('best.pt')
    image = cv2.imread(file_path)
    np.random.seed(42)
    
    # Выполняем инференс
    results = model(image, imgsz=imgsz, iou=iou, conf=conf, verbose=False)
    
    # Получаем маски
    masks = results[0].masks.data.cpu().numpy()  # Преобразуем в numpy массив
    num_masks = masks.shape[0]
    
    # Возвращаем данные вместо визуализации
    return {
        "num_masks": num_masks,
        "masks": masks
    }

def get_process_result(file_path):
    # Настройка виджетов
    alpha_slider = widgets.FloatSlider(value=0.20, min=0.0, max=1.0, step=0.05, description='Alpha')
    iou_slider = widgets.FloatSlider(value=0.65, min=0.0, max=1.0, step=0.05, description='IOU')
    conf_slider = widgets.FloatSlider(value=0.15, min=0.0, max=1.0, step=0.05, description='Confidence')
    imgsz_slider = widgets.IntSlider(value=640, min=32, max=2560, step=32, description='imgsz')

    # Передаем значения слайдеров, а не сами объекты
    result = interactive_plot(file_path, alpha_slider.value, iou_slider.value, conf_slider.value, imgsz_slider.value)
    return result

# Пример вызова
# print(get_process_result('/Users/yurazhilin/Desktop/pyQtApp/drop1.jpg'))
