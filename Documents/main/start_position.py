import time
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from Encoder import Encoder


kit = ServoKit(channels=16,frequency=50)

gripper_pin = 13
rack_pin = 14
platform_pin = 15
pressure_pin = 7
pusher_pin = 12

GPIO.setmode(GPIO.BCM)

#delete later
time.sleep(1)

#starting position
kit.servo[gripper_pin].angle = 80
kit.servo[platform_pin].angle = 135
kit.servo[rack_pin].angle = 0

time.sleep(2)
'''
kit.servo[platform_pin].angle = 170
time.sleep(0.5)
kit.servo[platform_pin].angle = 125
'''
GPIO.cleanup()