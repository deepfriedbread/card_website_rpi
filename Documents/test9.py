import RPi.GPIO as GPIO
import time

def angle_to_duty_cycle(angle):
        return 2.5 + (angle/18)

servo_pin = 17
rack_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(rack_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(7.5)

rack_pwm = GPIO.PWM(rack_pin,50)
rack_pwm.start(7.5)

try:
	rack_pwm.ChangeDutyCycle(2.5)
	time.sleep(0.3)
	pwm.stop()
	rack_pwm.stop()
	GPIO.cleanup()
except KeyboardInterrupt:
	pwm.stop()
	rack_pwm.stop()
	GPIO.cleanup()
