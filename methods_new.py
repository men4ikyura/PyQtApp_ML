from ultralytics import YOLO
from PIL import Image
from shapely.geometry import Polygon
import numpy as np
import os


# завернул все в один метод
def main(path_image, conf, iou, retina_masks, imgsz, multiplier_from_pixels_to_microns):

    # НОВЫЙ ПАРАМЕТР(количество пикселей в одном микроне) я его вынес сюда, нужно его вынести в приложение для пользователя
    # этот параметр задает отношение: сколько пикселей в одном микроне, нужен для пересчета диаметра капли из пикселей в микроны
    # тип - число с плавающей точкой больше нуля
    # значение по умолчанию 7.5
    # multiplier_from_pixels_to_microns = 7.5

    model_path = 'best.pt'
    # загружаем модель
    model = YOLO(model_path)

    image = Image.open(path_image)
    
    #ВОТ ТУТ КОСЯК режу черные поля у картинки, и на отрисовку у теюя юрчик идет ИСХОДНАЯ картинка, а не ПОРЕЗАННАЯ, и все мимо рисуется

    # загружаем картинку в модель, imgsz = 640, еще есть параметр conf - тип float от 0 до 1 включительно,
    # это уверенность модели что обьект соотвествует и его надо выделять
    result = model(image, imgsz=imgsz, conf=conf, iou=iou,
                   retina_masks=retina_masks, max_det=2500)

    # может быть что не нашло ни одной капли, нужно вернуть пустой список
    if result[0].masks == None:
        return (0,[])

    #  берем маски из обьекта result, xy - значит что координаты не нормамированные
    masks = result[0].masks.xy

    result_list = make_result_list(masks, multiplier_from_pixels_to_microns)
    # # # получаем список с вычислениями для каждой капли вида (count, [(маска1, площадь1, центр1),
    # # #                                                       (маска2, площадь2, центр2),
    # # #                                                       (маска3, площадь3, центр3)
    # # #
    # # #                                             ])

    return (len(result_list), result_list)


# собираем кортеж для капли вида (маска, площадь, центр)
def count_all_parameters_of_object_on_image(mask, multiplier_from_pixels_to_microns):
    # делаем проверку что в маска капли это не пустой список и еще что есть минимум 4 точки уникальные 
    if len(mask.astype(set)) > 3:
        # замыкаем контур первым пикселем, чтобы полигон норм посчитало
        new_mask = np.vstack([mask, mask[0]])
        # считаем полигон собнсно
        polygon = Polygon(new_mask)
        # берем центр
        center = polygon.centroid
        # считаем диаметер
        diameter = find_diameter_in_pixels(new_mask, center) / multiplier_from_pixels_to_microns
            
        # возвращаем итоговый кортеж
        return (new_mask, diameter, (center.x, center.y))
    return None


# собираем итоговый список всех капель
def make_result_list(masks, multiplier_from_pixels_to_microns):
    res_list = []
    for mask in masks:
        res_tuple = count_all_parameters_of_object_on_image(
            mask, multiplier_from_pixels_to_microns)
        # если прошло проверку что в маска капли это не пустой список, то делаем вычисления дальше и добавляем
        if res_tuple != None:
            res_list.append(res_tuple)
    return res_list


# обрезаем черные поля на картинке, если их нету то ничего не меняется
def find_filled_areas(image_path):
    with Image.open(image_path) as img:
        # Преобразуем изображение в оттенки серого
        gray_image = img.convert("L")

        # Применяем пороговую фильтрацию, чтобы отделить заполненные области (например, значимые пиксели)
        # Порог для выделения "заполненных" областей (чем выше, тем светлее пиксели)
        threshold = 30 # константу сам подобрал на ориг фотках
        bw_image = gray_image.point(lambda p: p > threshold and 255)

        # Используем getbbox(), чтобы найти ограничивающую рамку заполненных областей
        bbox = bw_image.getbbox()  # Возвращает кортеж (left, upper, right, lower)

        if bbox:
            # Обрезаем изображение по найденной рамке
            gray_image = img.crop(bbox)

        return gray_image


def find_diameter_in_pixels(mask, center_point):

    # Расчет расстояний от центра до каждой точки
    distances = np.sqrt((mask[:, 0] - center_point.x) **
                        2 + (mask[:, 1] - center_point.y)**2)

    # Средний радиус умножаем на 2 получаем средний диаметер
    return float(distances.mean() * 2)