import time
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO

def clockwise(pin1,pin2):
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)

def anticlockwise(pin1,pin2):
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)

def stop(pin1,pin2):
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)

kit = ServoKit(channels=16,frequency=50)

gripper_pin = 13
rack_pin = 14
platform_pin = 15

pressure_pin = 0
#pusher_pin = 

scissormotor_pin1 = 23
scissormotor_pin2 = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(scissormotor_pin1,GPIO.OUT)
GPIO.setup(scissormotor_pin2,GPIO.OUT)

stop(scissormotor_pin1,scissormotor_pin2)

#delete later
time.sleep(0.5)

kit.servo[gripper_pin].angle = 80
kit.servo[rack_pin].angle = 90
kit.servo[platform_pin].angle = 125

time.sleep(5)

#move cards back far enough to drop
kit.servo[platform_pin].angle = 170
time.sleep(0.5)
kit.servo[rack_pin].angle = 180
time.sleep(1)
kit.servo[gripper_pin].angle = 150
time.sleep(0.3)
kit.servo[platform_pin].angle = 80
time.sleep(0.5)

kit.servo[gripper_pin].angle = 90
time.sleep(0.5)

#drop cards
kit.servo[rack_pin].angle = 90
time.sleep(0.1)
kit.servo[gripper_pin].angle = 155
time.sleep(0.5)
kit.servo[platform_pin].angle = 40
time.sleep(1)

GPIO.cleanup()
