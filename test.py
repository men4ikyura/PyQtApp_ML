from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget
import sys

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.download_btn = QPushButton("Загрузить изображение")
        self.show_hst_btn = QPushButton("Показать историю результатов")
        self.setting_btn = QPushButton("Настройки приложения")

        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.download_btn)
        self.layout_main.addWidget(self.show_hst_btn)
        self.layout_main.addWidget(self.setting_btn)

        self.setLayout(self.layout_main)

class SettingUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QPushButton("Это настройки")
        layout.addWidget(title)
        self.setLayout(layout)

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = MainUI()
        self.setCentralWidget(self.main_ui)
        self.setWindowTitle("Главное окно")
        self.resize(600, 400)

    def update_display(self, param):
        # Здесь вы можете изменить параметры отображения в зависимости от значения param
        if param == 'option1':
            self.resize(600, 400)  # Например, установить определенный размер
            self.main_ui.download_btn.setVisible(True)  # Или скрыть/показать элементы
        elif param == 'option2':
            self.resize(800, 600)
            self.main_ui.download_btn.setVisible(False)

class SettingController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings_ui = SettingUI()
        self.setCentralWidget(self.settings_ui)
        self.setWindowTitle("Настройки")
        self.resize(400, 300)

    def update_display(self, param):
        # Здесь также можно изменить параметры отображения
        if param == 'dark_mode':
            self.setStyleSheet("background-color: black; color: white;")  # Применение темы
        else:
            self.setStyleSheet("background-color: white; color: black;")

class AppHandler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWnd = MainController()
        self.settingsWnd = SettingController()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.mainWnd)
        self.stack.addWidget(self.settingsWnd)
        self.setCentralWidget(self.stack)

        self.mainWnd.main_ui.setting_btn.clicked.connect(self.show_settings_window)

    def show_main_window(self, param=None):
        """Переключение на главное окно и обновление его отображения"""
        self.stack.setCurrentWidget(self.mainWnd)
        if param:
            self.mainWnd.update_display(param)

    def show_settings_window(self, param=None):
        """Переключение на окно настроек и обновление его отображения"""
        self.stack.setCurrentWidget(self.settingsWnd)
        if param:
            self.settingsWnd.update_display(param)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppHandler()
    window.show()
    window.show_main_window(param='option1')  # Пример вызова с параметром
    sys.exit(app.exec())
