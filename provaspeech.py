# Programma di pilotaggio robot
from PIL.Image import Image
from imageai.Detection import ObjectDetection
import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from picamera import PiCamera


import speech_recognition as sr
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from time import sleep

# definizioe dei GPIO 
in1 = 18
in2 = 27
in3 = 22  
in4 = 23
en1 = 24
en2 = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(en1,GPIO.LOW)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(en2,GPIO.LOW)


p1=GPIO.PWM(en1,1500)
p2=GPIO.PWM(en2,1500)
p1.start(24)
p2.start(25)
  
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    


# referenze libreria: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#speech-recognition-library-reference

recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

text = ""

def stop():
    print("robot stop")
    GPIO.output(en1, GPIO.LOW)
    GPIO.output(en2, GPIO.LOW)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    client.publish("Tutorial2", "Robot stop")
    camera = PiCamera() 
    camera.start_preview()
    time.sleep(10)
    camera.capture('/home/pi/Enricosource/image.jpg')
    camera.stop_preview()
    elaborazione()
    

def forward():
    print("robot forward")
    GPIO.output(en1, GPIO.HIGH)
    GPIO.output(en2, GPIO.HIGH)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    client.publish("Tutorial2", "Robot avanti")
    
    
    
def backward():
    print("robot backward")
    GPIO.output(en1, GPIO.HIGH)
    GPIO.output(en2, GPIO.HIGH)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    client.publish("Tutorial2", "Robot indietro")

def right():
    print("robot right")
    GPIO.output(en1, GPIO.HIGH)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    sleep(0.35)
    GPIO.output(in3, GPIO.LOW)
    client.publish("Tutorial2", "Robot destra")

def left():
    print("robot left")
    GPIO.output(en1, GPIO.HIGH)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    sleep(0.35)
    GPIO.output(in2, GPIO.LOW)
    client.publish("Tutorial2", "Robot sinistra")




def avanti():
    print("robot avanti")
    forward()
    sleep(2)
    stop()


def indietro():
    print("robot indietro")
    backward()
    sleep(2)
    stop()
    
    
    
    
def ferma():
    print("robot ferma")
    stop()

def destra():
    print("robot destra")
    right()
    stop()
    
def sinistra():
    print("robot sinistra")
    left()
    stop()
    
def on_connect(client, userdata, flags, rc):
    print("connected with code "+ str(rc))
    # substrice topic
    client.subscribe("Topic/#")

def on_message(client, userdata, msg):
    print(str(msg.payload))

def elaborazione():
      execution_path = os.getcwd()
      detector = ObjectDetection()
      detector.setModelTypeAsRetinaNet()
      detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
      detector.loadModel()
      detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
      for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("fkjqkoul","wK0aUWpQWS35")
client.connect("tailor.cloudmqtt.com", 16434 , 60 )

client.publish("Tutorial2", "Getting started with MQTT TEST")

while(text != "esci"):
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print("Google ha capito: \n", text)
        
        if (text == "esci"):
             break
            
        if (text =="avanti"):
            avanti()
            
        if (text =="indietro"):
            indietro()
            
        if (text =="ferma"):
            stop()
         
        if (text =="destra"):
            right()
            
        if (text =="sinistra"):
            left()
         
            
    except Exception as e:
        print("errore")
        print(e)