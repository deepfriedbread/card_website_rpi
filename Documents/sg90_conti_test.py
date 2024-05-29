import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(7.5)

time.sleep(1)

pwm.ChangeDutyCycle(2.5)
time.sleep(0.2)
pwm.ChangeDutyCycle(12.5)
time.sleep(0.2)
pwm.ChangeDutyCycle(7.5)

time.sleep(2)
pwm.stop()
GPIO.cleanup()