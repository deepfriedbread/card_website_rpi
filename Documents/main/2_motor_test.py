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
motor2_pin1 = 13
motor2_pin2 = 19
en_pin = 26
pressure_pin = 7

kit = ServoKit(channels=16,frequency=50)

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1,GPIO.OUT)
GPIO.setup(motor1_pin2,GPIO.OUT)
GPIO.setup(motor2_pin1,GPIO.OUT)
GPIO.setup(motor2_pin2,GPIO.OUT)
GPIO.setup(en_pin,GPIO.OUT)

'''
en_pwm = GPIO.PWM(en_pin, 100)
en_pwm.start(100)
stop(motor2_pin1,motor2_pin2)
time.sleep(0.5)
clockwise(motor2_pin1,motor2_pin2)
time.sleep(0.1)

'''
en_pwm = GPIO.PWM(en_pin, 100)
en_pwm.start(0)

kit.servo[pressure_pin].angle = 90

stop(motor1_pin1,motor1_pin2)
stop(motor2_pin1,motor2_pin2)

en_pwm.ChangeDutyCycle(100)

for i in range(3):
        #if (i % 2 == 0) and (i != 0): 
        #        servo_angle -= 5
        clockwise(motor2_pin1,motor2_pin2)
        time.sleep(0.1)
        stop(motor2_pin1,motor2_pin2)
        if i == 0:
                time.sleep(0.5)
                anticlockwise(motor1_pin1,motor1_pin2)
        time.sleep(1)


stop(motor2_pin1,motor2_pin2)
time.sleep(0.5)
stop(motor1_pin1,motor1_pin2)
time.sleep(0.1)

en_pwm.stop()

GPIO.cleanup()