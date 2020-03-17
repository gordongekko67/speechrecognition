import RPi.GPIO as GPIO
import time

in1 = 18
in2 = 27
in3 = 22  
in4 = 23
#en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

#GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

#p=GPIO.PWM(en,1000)

def stop():
    print("robot stop")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)

def forward():
    print("robot forward")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    
def backward():
    print("robot backward")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH) 

def right():
    print("robot right")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)

def left():
    print("robot left")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)



forward()
time.sleep(2)
backward()
time.sleep(2)
stop()
print("Hello world")
    




