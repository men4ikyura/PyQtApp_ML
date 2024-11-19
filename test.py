# import os
# import cv2
# from ultralytics import YOLO
# import numpy as np
# import ipywidgets as widgets

# def interactive_plot(file_path, alpha, iou, conf, imgsz):
#     # Limit the number of threads to 1
#     os.environ["OMP_NUM_THREADS"] = "1"
#     os.environ["MKL_NUM_THREADS"] = "1"
    
#     model = YOLO('best.pt')
#     image = cv2.imread(file_path)
#     np.random.seed(42)
    
#     # Perform inference
#     results = model(image, imgsz=imgsz, iou=iou, conf=conf, verbose=False)
    
#     # Get masks
#     masks = results[0].masks.data.cpu().numpy()  # Convert to numpy array
#     num_masks = masks.shape[0]
    
#     # Return data instead of visualizing
#     return {
#         "num_masks": num_masks,
#         "masks": masks
#     }

# def get_process_result(file_path):
#     # Set up widgets
#     alpha_slider = widgets.FloatSlider(value=0.20, min=0.0, max=1.0, step=0.05, description='Alpha')
#     iou_slider = widgets.FloatSlider(value=0.65, min=0.0, max=1.0, step=0.05, description='IOU')
#     conf_slider = widgets.FloatSlider(value=0.15, min=0.0, max=1.0, step=0.05, description='Confidence')
#     imgsz_slider = widgets.IntSlider(value=640, min=32, max=2560, step=32, description='imgsz')

#     # Pass slider values, not the objects themselves
#     result = interactive_plot(file_path, alpha_slider.value, iou_slider.value, conf_slider.value, imgsz_slider.value)
#     return result

# # Example call
# # print(get_process_result('/Users/yurazhilin/Desktop/pyQtApp/drop1.jpg'))
