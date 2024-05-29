import RPi.GPIO as GPIO
import time
from Encoder import Encoder

pin1 = 23
pin2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
enc = Encoder(5,6)

def clockwise():
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)

def anticlockwise():
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)

def stop():
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)

clockwiseRotation = None

try:
    stop()
    time.sleep(3)
    print(enc.read())
    clockwise()
    time.sleep(0.5)
    print(enc.read())
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Exiting...")
    stop()
    GPIO.cleanup()