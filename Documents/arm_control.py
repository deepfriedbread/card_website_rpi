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

kit = ServoKit(channels=16,frequency=50)

time.sleep(1)

'''
kit.servo[pin1].angle = 170
kit.servo[pin2].angle = 110
kit.servo[pin3].angle = 70

GPIO.cleanup()

try:
    while True:
        switch_state = GPIO.input(limit_pin)

        if switch_state == GPIO.LOW:
            print("button pressed")
            
            break

        # Optional: Add a small delay to reduce CPU usage
        time.sleep(0.001)
    GPIO.cleanup()
    

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()


'''
kit.servo[pin1].angle = 170
kit.servo[pin2].angle = 110
kit.servo[pin3].angle = 70
kit.servo[pin4].angle = 90

try:
	GPIO.output(vacuum_pin, GPIO.LOW)
	GPIO.output(solenoid_pin, GPIO.LOW)
	time.sleep(1)
	kit.servo[pin3].angle = 50
	time.sleep(0.5)
	GPIO.output(vacuum_pin, GPIO.HIGH)
	time.sleep(0.5)
	kit.servo[pin2].angle = 130
	kit.servo[pin3].angle = 120
	time.sleep(0.5)
	kit.servo[pin1].angle = 10
	time.sleep(1)
	GPIO.output(vacuum_pin, GPIO.LOW)
	GPIO.output(solenoid_pin, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(solenoid_pin, GPIO.LOW)
	time.sleep(0.5)
	kit.servo[pin1].angle = 170
	time.sleep(0.5)
	kit.servo[pin2].angle = 110
	kit.servo[pin3].angle = 70
	time.sleep(0.1)
	GPIO.cleanup()

	

except KeyboardInterrupt:
	GPIO.cleanup()

