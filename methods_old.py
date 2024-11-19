from ultralytics import YOLO
from PIL import Image, ImageDraw
from shapely.geometry import Polygon


# завернул все в один метод
def main_procces(image_path,conf=0.2,iou=0,imgsz=640):

    model_path = "/Users/yurazhilin/Desktop/pyQtApp/best.pt"
    # загружаем модель
    model=YOLO(model_path)


    # картинку загружаем, модуль Image из библиотеки PIL
    image = Image.open(image_path)


    # загружаем картинку в модель, imgsz = 640, еще есть параметр conf - тип float от 0 до 1 включительно, 
    # это уверенность модели что обьект соотвествует и его надо выделять
    result=model(image,imgsz=imgsz,conf=conf,iou=iou)


    # берем маски из обьекта result, xy - значит что координаты не нормамированные 
    masks = result[0].masks.xy


    # получаем список с вычислениями для каждой капли вида [(маска1, площадь1,центр1), (маска2,площадь2,центр2)...]
    return make_result_list(masks)
    

# считает маску одной капли, берет mask и возвращает список кортежей вида (x1,x2)
def get_image_masks(mask):
    mask_of_drops=[]
    for coords in mask:
        mask_of_drops.append((int(coords[0]),int(coords[1])))  
    return mask_of_drops


# считаем площадь отдельной капли в пикселях
def count_object_area(mask):
    # Создаем объект Polygon из списка координат
    polygon = Polygon(mask)
    # Возвращаем площадь многоугольника в пикселях
    return polygon.area


# считаем центр капли получаем кортеж (x,y) там точность знаков 15, поэтому аккуратней
def find_object_center(mask):
    # Создаем объект Polygon из списка координат
    polygon = Polygon(mask)
    # Получаем центр многоугольника
    centroid = polygon.centroid
    return (centroid.x, centroid.y)  # Возвращаем координаты центра


# собираем кортеж для капли вида (маска, площадь, центр)
def count_all_parameters_of_object_on_image(mask):
    return (get_image_masks(mask),count_object_area(mask),find_object_center(mask))


# собираем итоговый список всех капель
def make_result_list(masks):
    res_list=[]
    for mask in masks:
        res_list.append(count_all_parameters_of_object_on_image(mask))
    return  res_list


