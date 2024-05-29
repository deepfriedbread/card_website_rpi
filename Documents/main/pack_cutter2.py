import time
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from Encoder import Encoder

def clockwise(pin1,pin2):
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)

def anticlockwise(pin1,pin2):
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)

def stop(pin1,pin2):
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)

def scissor_cycle():
    while True:
        current_position = enc.read()
        switch_state = GPIO.input(limit_pin)

        anticlockwise(scissormotor_pin1,scissormotor_pin2)

        if switch_state == GPIO.LOW:
            stop(scissormotor_pin1,scissormotor_pin2)
            time.sleep(1)
            print("Reached position:", current_position)

            while current_position > 0:
                 clockwise(scissormotor_pin1,scissormotor_pin2)
                 current_position = enc.read()
                 time.sleep(0.001)
            print("Reached position:", current_position) 
            stop(scissormotor_pin1,scissormotor_pin2)
            time.sleep(1)
            break

        time.sleep(0.001)

kit = ServoKit(channels=16,frequency=50)
enc = Encoder(23,24)

gripper_pin = 13
rack_pin = 14
platform_pin = 15
pressure_pin = 7
pusher_pin = 12
limit_pin = 20

scissormotor_pin1 = 13
scissormotor_pin2 = 19


GPIO.setmode(GPIO.BCM)
GPIO.setup(limit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(scissormotor_pin1,GPIO.OUT)
GPIO.setup(scissormotor_pin2,GPIO.OUT)

stop(scissormotor_pin1,scissormotor_pin2)

#delete later
time.sleep(1)

#starting position
kit.servo[gripper_pin].angle = 80
kit.servo[rack_pin].angle = 90
kit.servo[platform_pin].angle = 90
kit.servo[pressure_pin].angle = 120

time.sleep(1)

#receive card from robot arm
kit.servo[platform_pin].angle = 130
kit.servo[rack_pin].angle = 100
time.sleep(5)

#rock backwards to move cards backwards, then put into position for cutting
kit.servo[platform_pin].angle = 170
time.sleep(0.3)
kit.servo[gripper_pin].angle = 150
time.sleep(0.3)
kit.servo[platform_pin].angle = 135
time.sleep(0.5)
kit.servo[gripper_pin].angle = 80
time.sleep(0.5)
kit.servo[rack_pin].angle = 0
time.sleep(1)
#scissor_cycle()


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
kit.servo[platform_pin].angle = 10
time.sleep(1)

GPIO.cleanup()
