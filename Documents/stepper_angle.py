import RPi.GPIO as GPIO
import time

def turn_stepper(num_steps):
    for i in range(num_steps*4):
        GPIO.output(step_pin,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(step_pin,GPIO.LOW)
        time.sleep(0.001)

dir_pin = 24
step_pin = 23
ms_pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(dir_pin,GPIO.OUT)
GPIO.setup(step_pin,GPIO.OUT)
GPIO.setup(ms_pin,GPIO.OUT)

GPIO.output(ms_pin,GPIO.HIGH)

#GPIO.output(dir_pin,GPIO.LOW)
GPIO.output(dir_pin,GPIO.HIGH)

try:
	while True:
		steps = int(input('enter steps'))
		if 0 <= steps <= 200:
			turn_stepper(num_steps=steps)
		else:
			print('try again')

except KeyboardInterrupt:
	GPIO.cleanup()
