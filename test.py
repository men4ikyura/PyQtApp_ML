from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class ModelParametersUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Текст с HTML-разметкой
        text = """
        <h2>Параметры для настройки модели обнаружения объектов</h2>

        <h3>1. <b>conf</b> — Порог уверенности обнаружения объекта</h3>
        <p><b>Описание:</b> Указывает минимальный уровень уверенности модели для обнаружения объекта. Если уверенность ниже этого значения, объект будет проигнорирован.</p>
        <p><b>Тип значения:</b> Дробное число от 0 до 1.</p>
        <p><b>Значение по умолчанию:</b> 0.25.</p>
        <p><b>Рекомендации:</b></p>
        <ul>
            <li><b>Не рекомендуется</b> устанавливать значение:
                <ul>
                    <li><b>Меньше 0.1</b> — может значительно снизить скорость обработки из-за ложных срабатываний.</li>
                    <li><b>Больше 0.9</b> — может привести к пропуску значительной части объектов и снижению точности.</li>
                </ul>
            </li>
        </ul>

        <h3>2. <b>iou</b> — Порог пересечения объектов</h3>
        <p><b>Описание:</b> Определяет, как модель обрабатывает пересекающиеся объекты.</p>
        <ul>
            <li>При <b>низких значениях</b> из двух пересекающихся объектов будет выделен только один.</li>
            <li>При <b>высоких значениях</b> будут выделены оба объекта.</li>
        </ul>
        <p><b>Тип значения:</b> Дробное число от 0 до 1.</p>
        <p><b>Значение по умолчанию:</b> 0.7.</p>

        <h3>3. <b>imgsz</b> — Размер входного изображения</h3>
        <p><b>Описание:</b> Определяет размер изображения, которое подается на вход модели. Изображение будет сжато до размеров <b>imgsz × imgsz</b> пикселей.</p>
        <p><b>Тип значения:</b> Целое число больше нуля.</p>
        <p><b>Значение по умолчанию:</b> 1280.</p>
        <p><b>Рекомендации:</b></p>
        <ul>
            <li>Устанавливать значение, которое делится на 32.</li>
            <li>Если обработка изображения занимает много времени или возникают ошибки, уменьшите значение до <b>620</b>. Это снизит точность, но повысит скорость обработки.</li>
        </ul>

        <h3>4. <b>retina_masks</b> — Точность контуров объекта</h3>
        <p><b>Описание:</b> Определяет уровень детализации контуров объекта.</p>
        <ul>
            <li>При значении <b>True</b> контуры капель будут более точными, что улучшит вычисление их размеров.</li>
            <li>При значении <b>False</b> контуры будут менее детализированными, но скорость обработки увеличится.</li>
        </ul>
        <p><b>Тип значения:</b> Логическое (<b>True</b> или <b>False</b>).</p>
        <p><b>Значение по умолчанию:</b> <b>True</b>.</p>
        <p><b>Рекомендации:</b> Если обработка происходит медленно или возникают ошибки, отключите параметр (<b>False</b>), чтобы повысить скорость работы модели.</p>
        """

        # Создание QLabel для отображения текста
        label = QLabel(text)
        label.setWordWrap(True)  # Включить перенос слов для удобного отображения текста

        # Добавляем QLabel в layout
        layout.addWidget(label)

        self.setLayout(layout)
        self.setWindowTitle("Параметры модели")
        self.resize(800, 600)  # Задаем размер окна

if __name__ == "__main__":
    app = QApplication([])
    window = ModelParametersUI()
    window.show()
    app.exec()