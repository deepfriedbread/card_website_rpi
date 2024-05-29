import RPi.GPIO as GPIO
import time

step_pin = 23  # Step pin
dir_pin = 18   # Direction pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.output(dir_pin, GPIO.HIGH)  # GPIO.HIGH for clockwise (CW), GPIO.LOW for counterclockwise (CCW)

# Number of steps and delay between steps (adjust as needed)
num_steps = 200
delay = 0.001

# Generate step pulses to move the motor
for i in range(1):
	for _ in range(num_steps):
    		GPIO.output(step_pin, GPIO.HIGH)
    		time.sleep(delay)
    		GPIO.output(step_pin, GPIO.LOW)
    		time.sleep(delay)
	time.sleep(1)
time.sleep(2)
# Cleanup and exit
GPIO.cleanup()
