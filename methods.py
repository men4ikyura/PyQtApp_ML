from ultralytics import YOLO
from PIL import Image
from shapely.geometry import Polygon


# завернул все в один метод
def main(image_path,model_path='best.pt',conf=0.2,iou=0,imgsz=640):


    # загружаем модель
    model=YOLO(model_path)


    # картинку загружаем, модуль Image из библиотеки PIL
    image = Image.open(image_path)


    # загружаем картинку в модель, imgsz = 640, еще есть параметр conf - тип float от 0 до 1 включительно, 
    # это уверенность модели что обьект соотвествует и его надо выделять
    result=model(image,imgsz=imgsz,conf=conf,iou=iou, max_det = 2500, retina_masks = True)


    # берем маски из обьекта result, xy - значит что координаты не нормамированные 
    masks = result[0].masks.xy


    # получаем список с вычислениями для каждой капли вида [(маска1, площадь1, центр1), 
    #                                                       (маска2, площадь2, центр2),
    #                                                       (маска3, площадь3, центр3)
    #                                                       ]
    return make_result_list(masks)
    

# вовзращает маску ОДНОЙ капли в ОТДЕЛЬНОСТИ
# маска капли это список пикселей, один пиксель это кортеж с координатами этого пикселя вида (x1,y1)
# точность координат до десятых, то есть каждая координата имеет тип float 
def get_image_masks(mask):
    mask_of_water=[]
    for coords in mask:
        mask_of_water.append((float(coords[0]),float(coords[1])))  
    return mask_of_water


# считаем площадь отдельной капли в ПИКСЕЛЯХ вернет float с точностью до десятых
def count_object_area(mask):
    # Создаем объект Polygon из списка координат
    polygon = Polygon(mask)
    # Возвращаем площадь многоугольника в пикселях
    return polygon.area


# считаем центр капли получаем кортеж (x,y) вернет float  точность 12 знаков после запятой
def find_object_center(mask):
    # Создаем объект Polygon из списка координат
    polygon = Polygon(mask)
    # Получаем центр многоугольника
    centroid = polygon.centroid
    return (centroid.x, centroid.y)  # Возвращаем координаты центра


# собираем кортеж для капли вида (маска, площадь, центр)
def count_all_parameters_of_object_on_image(mask):
    image_mask=get_image_masks(mask)
    # делаем проверку что в маска капли это не пустой список
    if len(image_mask)>0:
        return (get_image_masks(mask),count_object_area(mask),find_object_center(mask))
    return None    


# собираем итоговый список всех капель
def make_result_list(masks):
    res_list=[]
    for mask in masks:
        res_tuple=count_all_parameters_of_object_on_image(mask)
        # если прошло проверку что в маска капли это не пустой список, то делаем вычисления дальше и добавляем
        if res_tuple!=None:
            res_list.append(count_all_parameters_of_object_on_image(mask))
    return  res_list

