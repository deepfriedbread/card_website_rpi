import time
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO

limit_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(limit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

kit = ServoKit(channels=16,frequency=50)

time.sleep(1)

kit.continuous_servo[12].throttle = -0.5

try:
    while True:
        switch_state = GPIO.input(limit_pin)

        if switch_state == GPIO.LOW:
            print("button pressed")
            kit.continuous_servo[12].throttle = 0.1
            break

        # Optional: Add a small delay to reduce CPU usage
        time.sleep(0.001)
    GPIO.cleanup()
    

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()
