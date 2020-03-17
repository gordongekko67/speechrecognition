from PIL.Image import Image
from imageai.Detection import ObjectDetection
import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np


def elaborazione():
      execution_path = os.getcwd()
      detector = ObjectDetection()
      detector.setModelTypeAsRetinaNet()
      detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
      detector.loadModel()
      detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image1.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
      for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


print(cv2.__version__)
vidcap = cv2.VideoCapture('MVI_6838.mp4')
success,image = vidcap.read()
count = 0
filename = "image2.jpg"
success = True
while success:
  cv2.imwrite(filename, image)     # save frame as JPEG file
  elaborazione()
  img = cv2.imread('imagenew.jpg', 1)
  cv2.imshow('image', img)
  cv2.waitKey(3000)
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1




