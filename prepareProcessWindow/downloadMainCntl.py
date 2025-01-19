# # from processWindow.downloadMainUI import DownloadMainWindowUI
# # from PyQt5.QtWidgets import QFileDialog, QStackedWidget
# # from PyQt5.QtWidgets import QMainWindow
# # from stackCntrl.stackCntrl import StackCntrl
# # from processWindow.showImageWnd import ShowImageWindow

# # class DownloadMainController(QMainWindow):


# #     def __init__(self):
# #         super().__init__()
# #         self.come_back_main_menu_btn = None
# #         self.downloadMainWindowUI = DownloadMainWindowUI()
# #         self.stack = QStackedWidget()
# #         self.setup_start_downaload_ui()
# #         self.setCentralWidget(self.stack)
# #         self.resize(600, 600)
        

    
# #     def setup_start_downaload_ui(self):
# #         self.add_item_to_stack(self.downloadMainWindowUI) 
    

# #     def show_image_window(self, file_path):
# #         StackCntrl.clear_stacked_widget(self.stack)
# #         image_window = ShowImageWindow(file_path)
# #         self.stack.addWidget(image_window)
# #         self.stack.setCurrentWidget(image_window)
# #         image_window.come_back_to_download_menu_btn.clicked.connect(self.setup_start_downaload_ui)


# #     def add_item_to_stack(self,  name):
# #         StackCntrl.clear_stacked_widget(self.stack)
# #         self.stack.addWidget(name)
# #         self.stack.setCurrentWidget(name)
# #         print(name)
# #         if name.__name__  == "DownloadMainWindowUI":
# #             self.come_back_main_menu_btn = name.come_back_main_menu_btn
# #             print(self.come_back_main_menu_btn)
# #             name.file_selected.connect(self.show_image_window) 

# from processWindow.downloadMainUI import DownloadMainWindowUI
# from PyQt5.QtWidgets import QStackedWidget, QMainWindow
# from stackCntrl.stackCntrl import StackCntrl
# from processWindow.showImageWnd import ShowImageWindow

# class DownloadMainController(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.downloadMainWindowUI = DownloadMainWindowUI()
#         self.come_back_main_menu_btn =  self.downloadMainWindowUI.come_back_main_menu_btn 
#         self.downloadMainWindowUI.file_selected.connect(self.show_image_window)
#         self.stack = QStackedWidget()
#         self.setCentralWidget(self.stack)
#         self.resize(600, 600)
#         self.setup_start_download_ui()

#     def setup_start_download_ui(self):
#         print("рисуем главное меню")
#         self.add_item_to_stack(self.downloadMainWindowUI)
#         print(self.come_back_main_menu_btn)


#     def show_image_window(self, file_path):
#         image_window = ShowImageWindow(file_path)
#         self.stack.addWidget(image_window)
#         self.stack.setCurrentWidget(image_window)
#         image_window.come_back_to_download_menu_btn.clicked.connect(self.setup_start_download_ui)

#     def add_item_to_stack(self, widget_instance):
#         StackCntrl.clear_stacked_widget(self.stack)
#         self.stack.addWidget(widget_instance)
#         self.stack.setCurrentWidget(widget_instance)

#         # if isinstance(widget_instance, DownloadMainWindowUI):
#         #     print("here")
#         #     self.come_back_main_menu_btn = widget_instance.come_back_main_menu_btn
#         #    

# # Добавьте метод в DownloadMainWindowUI для сигнала выбора файла
# # Убедитесь, что вы используете сигнал правильно


        

        

    
        



        
