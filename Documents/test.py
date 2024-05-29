
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pwmPin = 18
GPIO.setup(pwmPin,GPIO.OUT)
pwm = GPIO.PWM(pwmPin,50)
pwm.start(0)
try:
	while True:
		pwmPercent = float(input('PWM %'))
		#dutyCycle = 7.5+(pwmPercent / 100)*5
		dutyCycle = 7.5 + (pwmPercent - 90) / 18
		pwm.ChangeDutyCycle(dutyCycle)
		sleep(1)

except KeyboardInterrupt:
	pwm.ChangeDutyCycle(7.5)
	pwm.stop()
	GPIO.cleanup()
	print('cleanup')
