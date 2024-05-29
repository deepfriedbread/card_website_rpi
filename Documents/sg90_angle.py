import RPi.GPIO as GPIO
import time

def angle_to_duty_cycle(angle):
	return 2.5 + (angle/18)

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(7.5)

try:
	while True:
		angle = float(input('enter angle from 5 to 175'))
		if 5 <= angle <= 175:
			duty_cycle = angle_to_duty_cycle(angle)
			pwm.ChangeDutyCycle(duty_cycle)
			#time.sleep(1)
		else:
			print('try again')

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()

