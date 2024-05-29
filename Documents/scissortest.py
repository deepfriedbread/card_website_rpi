import RPi.GPIO as GPIO
import time
from Encoder import Encoder

pin1 = 13
pin2 = 19
limit_pin = 20


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(limit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
enc = Encoder(23,24)

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
    target_position = 100  # Define your target position here
    while True:
        current_position = enc.read()
        switch_state = GPIO.input(limit_pin)
        if current_position < target_position:
              anticlockwise()
        if switch_state == GPIO.LOW:
            print("switch pressed", current_position)
            stop()
            time.sleep(2)
            print("Reached position:", current_position)
            GPIO.cleanup()
            break

        elif current_position > target_position:
            stop()
            time.sleep(2)
            print("Reached position:", current_position)
            GPIO.cleanup()
            break

        time.sleep(0.001)  # Adjust the delay as needed for the desired update rate

except KeyboardInterrupt:
    print("Exiting...")
    stop()
    GPIO.cleanup()