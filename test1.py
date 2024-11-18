import cv2
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact

model = YOLO('best.pt')

# K2GP66Fhs6M
image = cv2.imread('oXo8QYHk9bc.jpg')
 

def interactive_plot(alpha, iou, conf, imgsz):
    np.random.seed(42)
    # Инференс с использованием модели YOLOv5
    results = model(image, imgsz=imgsz, iou=iou, conf=conf, verbose=False);

   # Получение бинарных масок и их количество
    masks = results[0].masks.data  # Формат: [число масок, высота, ширина]
    num_masks = masks.shape[0]

    # Определение случайных цветов и прозрачности для каждой маски
    colors = [tuple(np.random.randint(0, 256, 3).tolist()) for _ in range(num_masks)]  # Случайные цвета

    # Создание изображения для отображения масок
    mask_overlay = np.zeros_like(image)

    # Наложение масок на изображение
    for i in range(num_masks):
        color = colors[i]  # Случайный цвет
        mask = masks[i].cpu()

        # Изменение размера маски до размеров исходного изображения с использованием метода ближайших соседей
        mask_resized = cv2.resize(np.array(mask), (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)
        #print(mask.shape, img.shape, mask_resized.shape)

        # Создание маски с цветом и прозрачностью
        color_mask = np.zeros_like(image)
        color_mask[mask_resized > 0] = color
        mask_overlay = cv2.addWeighted(mask_overlay, 1, color_mask, alpha, 0)

    # Объединение исходного изображения и масок
    result_image = cv2.addWeighted(image, 1, mask_overlay, 1, 0)

    # Отобразите итоговое изображение с наложенными масками
    plt.figure(figsize=(8, 8), dpi=150)
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    plt.imshow(result_image)
    plt.axis('off')
    plt.show()

# Создайте виджеты для изменения параметров
alpha_slider = widgets.FloatSlider(value=0.20, min=0.0, max=1.0, step=0.05, description='Alpha')
iou_slider = widgets.FloatSlider(value=0.65, min=0.0, max=1.0, step=0.05, description='IOU')
conf_slider = widgets.FloatSlider(value=0.15, min=0.0, max=1.0, step=0.05, description='Confidence')
imgsz_slider = widgets.IntSlider(value=640, min=32, max=2560, step=32, description='imgsz')

# Используйте interact для связи виджетов с функцией
interact(interactive_plot, alpha=alpha_slider, iou=iou_slider, conf=conf_slider, imgsz=imgsz_slider);