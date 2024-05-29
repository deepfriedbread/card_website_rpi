import RPi.GPIO as GPIO
import time

def angle_to_duty_cycle(angle):
	return 2.5 + (angle/18)

def clockwise(pin1,pin2):
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)

def anticlockwise(pin1,pin2):
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)

def stop(pin1,pin2):
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)

motor1_pin1 = 21
motor1_pin2 = 20
motor2_pin1 = 16
motor2_pin2 = 12
servo_pin = 1
en_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1,GPIO.OUT)
GPIO.setup(motor1_pin2,GPIO.OUT)
GPIO.setup(motor2_pin1,GPIO.OUT)
GPIO.setup(motor2_pin2,GPIO.OUT)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(en_pin,GPIO.OUT)

servo_pwm = GPIO.PWM(servo_pin,50)
servo_pwm.start(7.5)
en_pwm = GPIO.PWM(en_pin, 100)
en_pwm.start(0)

num_cards = 10

servo_angle = (2.5*(num_cards-1)) + 38
servo_angle = 68
servo_pwm.ChangeDutyCycle(angle_to_duty_cycle(servo_angle))
time.sleep(1)

stop(motor1_pin1,motor1_pin2)
stop(motor2_pin1,motor2_pin2)

en_pwm.ChangeDutyCycle(100)

for i in range(num_cards):
        #if (i % 2 == 0) and (i != 0): 
        #        servo_angle -= 5
        servo_angle -= 2.5
        servo_pwm.ChangeDutyCycle(angle_to_duty_cycle(servo_angle))
        clockwise(motor2_pin1,motor2_pin2)
        time.sleep(0.1)
        stop(motor2_pin1,motor2_pin2)
        if i == 0:
                time.sleep(0.5)
                anticlockwise(motor1_pin1,motor1_pin2)
        time.sleep(1)
'''
anticlockwise(motor1_pin1,motor1_pin2)
time.sleep(0.5)
clockwise(motor2_pin1,motor2_pin2)
time.sleep(0.1)
stop(motor2_pin1,motor2_pin2)
time.sleep(0.5)
anticlockwise(motor2_pin1,motor2_pin2)
time.sleep(0.3)
servo_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
time.sleep(0.2)
stop(motor2_pin1,motor2_pin2)
time.sleep(0.5)
clockwise(motor2_pin1,motor2_pin2)
time.sleep(0.5)
'''

stop(motor2_pin1,motor2_pin2)
time.sleep(0.5)
stop(motor1_pin1,motor1_pin2)
time.sleep(0.1)
servo_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
time.sleep(0.5)

en_pwm.stop()
servo_pwm.stop()
GPIO.cleanup()
