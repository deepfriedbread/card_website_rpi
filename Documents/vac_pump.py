import RPi.GPIO as GPIO
import time

vacuum_pin = 14
solenoid_pin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(vacuum_pin,GPIO.OUT)
GPIO.setup(solenoid_pin,GPIO.OUT)

try:
	GPIO.output(vacuum_pin, GPIO.LOW)
	GPIO.output(solenoid_pin, GPIO.LOW)
	time.sleep(3)
	GPIO.output(vacuum_pin, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(solenoid_pin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(solenoid_pin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(vacuum_pin, GPIO.LOW)
	time.sleep(1)
	GPIO.cleanup()

except KeyboardInterrupt:
	GPIO.cleanup()
    