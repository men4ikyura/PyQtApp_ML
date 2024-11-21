from ultralytics import YOLO
from PIL import Image
from shapely.geometry import Polygon
import numpy as np


# завернул все в один метод
def main(image_path,model_path='best.pt',conf=0.5,iou=0.5,imgsz=640):

    
    # загружаем модель
    model=YOLO(model_path)


    # картинку загружаем, модуль Image из библиотеки PIL
    image = Image.open(image_path)


    # загружаем картинку в модель, imgsz = 640, еще есть параметр conf - тип float от 0 до 1 включительно, 
    # это уверенность модели что обьект соотвествует и его надо выделять
    result=model(image,imgsz=imgsz,conf=conf,iou=iou,max_det = 2500,retina_masks=True)


    # # берем маски из обьекта result, xy - значит что координаты не нормамированные 
    masks = result[0].masks.xy

    result_list=make_result_list(masks)
    # # # получаем список с вычислениями для каждой капли вида (count, [(маска1, площадь1, центр1), 
    # # #                                                       (маска2, площадь2, центр2),
    # # #                                                       (маска3, площадь3, центр3)
    # # #    
    # # #                                             ])
    
    return (len(result_list),result_list)
    

# собираем кортеж для капли вида (маска, площадь, центр)
def count_all_parameters_of_object_on_image(mask):
    # делаем проверку что в маска капли это не пустой список
    if len(mask)>0:
        # замыкаем контур первым пикселем, чтобы полигон норм посчитало
        new_mask = np.vstack([mask, mask[0]])
        # считаем полигон собнсно
        polygon=Polygon(new_mask) 
        # берем площадь
        area=polygon.area
        # берем центр
        center=polygon.centroid
        # возвращаем итоговый кортеж
        return (new_mask,area,(center.x,center.y))
    return None    


# собираем итоговый список всех капель
def make_result_list(masks):
    res_list=[]
    for mask in masks:
        res_tuple=count_all_parameters_of_object_on_image(mask)
        # если прошло проверку что в маска капли это не пустой список, то делаем вычисления дальше и добавляем
        if res_tuple!=None:
            res_list.append(res_tuple)
    return  res_list
