import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit

def clockwise(pin1,pin2):
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)

def anticlockwise(pin1,pin2):
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)

def stop(pin1,pin2):
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)

motor1_pin1 = 5
motor1_pin2 = 6
en_pin = 26
pressure_pin = 7

kit = ServoKit(channels=16,frequency=50)

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1,GPIO.OUT)
GPIO.setup(motor1_pin2,GPIO.OUT)
GPIO.setup(en_pin,GPIO.OUT)

en_pwm = GPIO.PWM(en_pin, 100)
en_pwm.start(0)

kit.servo[pressure_pin].angle = 60

time.sleep(1)

stop(motor1_pin1,motor1_pin2)
en_pwm.ChangeDutyCycle(30)

for i in range(3):
        clockwise(motor1_pin1,motor1_pin2)
        time.sleep(0.11)
        stop(motor1_pin1,motor1_pin2)

        anticlockwise(motor1_pin1,motor1_pin2)
        time.sleep(0.027)
        stop(motor1_pin1,motor1_pin2)
        time.sleep(1)


GPIO.cleanup()