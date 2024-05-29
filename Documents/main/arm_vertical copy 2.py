import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit

vacuum_pin = 14
solenoid_pin = 15
limit_pin = 4
pin1 = 11
pin2 = 10
pin3 = 9
pin4 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(vacuum_pin,GPIO.OUT)
GPIO.setup(solenoid_pin,GPIO.OUT)
GPIO.setup(limit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(vacuum_pin, GPIO.LOW)
GPIO.output(solenoid_pin, GPIO.LOW)

kit = ServoKit(channels=16,frequency=50)

time.sleep(1)

pin2_angle = 90
pin3_angle = 100
pin3_angle_temp = pin3_angle
bottom_angle = 40

kit.servo[pin1].angle = 170
kit.servo[pin2].angle = pin2_angle
kit.servo[pin3].angle = pin3_angle
kit.servo[pin4].angle = 95
return_angle = 0
time.sleep(1)

GPIO.output(vacuum_pin, GPIO.HIGH)
for i in range(60):
    switch_state = GPIO.input(limit_pin)
    pin3_angle -= 1
    kit.servo[pin3].angle = pin3_angle
    return_angle = i
    if i < 10: 
        pass
        #pin2_angle += 0.6
        #kit.servo[pin2].angle = pin2_angle
    elif i < 30:
        pin2_angle += 0.4
        kit.servo[pin2].angle = pin2_angle
    else:
        pin2_angle += 0.6
        kit.servo[pin2].angle = pin2_angle
    if switch_state == GPIO.LOW:
        print("button pressed")
        pin2_angle -= 1.8
        kit.servo[pin2].angle = pin2_angle
        pin3_angle -= 3
        kit.servo[pin3].angle = pin3_angle
        break
    time.sleep(0.007)


for i in range(int(return_angle)):
    current_angle = (100-return_angle) + i
    pin3_angle += 1
    kit.servo[pin3].angle = pin3_angle
    if current_angle > 90:
        pass
        #kit.servo[pin2].angle -= 0.6
    elif current_angle < 70:
        pin2_angle -= 0.6
        kit.servo[pin2].angle = pin2_angle
    else:
        pin2_angle -= 0.4
        kit.servo[pin2].angle = pin2_angle
    
    time.sleep(0.005)


kit.servo[pin3].angle = 130
time.sleep(0.5)
kit.servo[pin1].angle = 170
kit.servo[pin2].angle = 120


time.sleep(0.5)

for i in range(160):
    kit.servo[pin1].angle = 170-i
    time.sleep(0.005)
time.sleep(0.2)
kit.servo[pin2].angle = 135
kit.servo[pin3].angle = 120
time.sleep(0.2)

GPIO.output(vacuum_pin, GPIO.LOW)
GPIO.output(solenoid_pin, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(solenoid_pin, GPIO.LOW)

time.sleep(0.5)
kit.servo[pin1].angle = 170

time.sleep(0.5)
#kit.servo[pin2].angle = 90
kit.servo[pin3].angle = 100
for i in range(40):
    kit.servo[pin2].angle = 130-i
    time.sleep(0.01)

GPIO.cleanup()