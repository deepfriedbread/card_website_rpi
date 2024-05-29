import numpy as np
import tensorflow as tf
#from keras import models
from picamera2 import Picamera2
from PIL import Image
import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit
import pandas as pd

def clockwise(pin1,pin2):
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)

def anticlockwise(pin1,pin2):
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)

def stop(pin1,pin2):
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)

csv_path = r'sv4/sv4.csv'
df = pd.read_csv(csv_path)

motor1_pin1 = 5
motor1_pin2 = 6
en_pin = 26
pressure_pin = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1,GPIO.OUT)
GPIO.setup(motor1_pin2,GPIO.OUT)
GPIO.setup(en_pin,GPIO.OUT)

en_pwm = GPIO.PWM(en_pin, 100)
en_pwm.start(0)

kit = ServoKit(channels=16,frequency=50)
kit.servo[pressure_pin].angle = 60

stop(motor1_pin1,motor1_pin2)
en_pwm.ChangeDutyCycle(30)

model = tf.keras.models.load_model(r'sv4/PAR_99_3_test.h5', compile=False)

picam = Picamera2()
video_config = picam.create_video_configuration(main={"size": (1640,1232)}, lores={"size":(640,480)},display="lores")
picam.configure(video_config)

picam.start()

time.sleep(1)

#video = cv2.VideoCapture(0)
#video.set(3, 640)
#video.set(4, 480)

for i in range(9):
        clockwise(motor1_pin1,motor1_pin2)
        time.sleep(0.11)
        stop(motor1_pin1,motor1_pin2)

        anticlockwise(motor1_pin1,motor1_pin2)
        time.sleep(0.027)
        stop(motor1_pin1,motor1_pin2)
        time.sleep(0.5)
        
        image = picam.capture_array()
        im = Image.fromarray(image).convert('RGB').resize((224,224))
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        
        start_time = time.time()
        
        predicted_class = np.argmax(model.predict(img_array), axis=1)
        
        print(time.time() - start_time)
        
        class_info = df[['name','number','rarity']].iloc[predicted_class]
        print(f"{class_info['name'].values[0]} {class_info['number'].values[0]} {class_info['rarity'].values[0]}")
        #im.save(f"{class_info['name'].values[0]}.png")
        
#im.save(f"{224}.png")
GPIO.cleanup()
'''
try:
    while True:
        image = picam.capture_array()
        #success, image = video.read()
        im = Image.fromarray(image)
        im = im.convert('RGB')
        im = im.resize((224,224))
        #im.save("image.jpg")
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)
        print(predicted_class)

except KeyboardInterrupt:
    im.save("224.png")
'''