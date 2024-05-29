import RPi.GPIO as GPIO
import time
from Encoder import Encoder

pin1 = 13
pin2 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
enc = Encoder(24,23)


def clockwise():
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)

def anticlockwise():
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)

def stop():
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)

try:
    time.sleep(3)
    target_position = 200  # Define your target position here
    while True:
        current_position = enc.read()

        if current_position < target_position:
              clockwise()
        else:
            stop()
            time.sleep(3)
            print("Reached position:", current_position)
            '''
            while current_position > 0:
                 anticlockwise()
                 current_position = enc.read()
                 time.sleep(0.001)
            print("Reached position:", current_position) 
            '''
            stop()
            time.sleep(1)
            GPIO.cleanup()
            break

        time.sleep(0.001)  # Adjust the delay as needed for the desired update rate
except KeyboardInterrupt:
    print("Exiting...")
    stop()
    GPIO.cleanup()
'''
try:
    target_position = 1000  # Define your target position here
    if target_position > 0: 
        clockwiseRotation = True
    else:
        clockwiseRotation = False

    while True:
        current_position = enc.read()

        if (current_position < target_position) and (clockwiseRotation == True):
              clockwise()
        elif (current_position > target_position) and (clockwiseRotation == False):
              anticlockwise()
        else:
            stop()
            time.sleep(1)
            print("Reached position:", current_position)
            while current_position > 0:
                 anticlockwise()
                 current_position = enc.read()
                 time.sleep(0.001)
            print("Reached position:", current_position) 
            stop()
            time.sleep(1)
            GPIO.cleanup()
            break

        time.sleep(0.001)  # Adjust the delay as needed for the desired update rate

except KeyboardInterrupt:
    print("Exiting...")
    stop()
    GPIO.cleanup()
'''