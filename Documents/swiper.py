import RPi.GPIO as GPIO
import time

def angle_to_duty_cycle(angle):
    return 2.5 + (angle/18)

def turn_stepper(steps):
    for i in range(steps*2):
        GPIO.output(step_pin,GPIO.HIGH)
        time.sleep(0.0005)
        GPIO.output(step_pin,GPIO.LOW)
        time.sleep(0.0005)    

def pack_cycle(number_of_turns=11):
    #GPIO.output(dir_pin,GPIO.HIGH)
    #turn_stepper(110)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(84))
    time.sleep(0.5)
    #GPIO.output(dir_pin,GPIO.LOW)
    #turn_stepper(200+90)
    turn_stepper(200+15)
    time.sleep(2)
    for i in range(number_of_turns - 1):
        if i == 1:
            pwm.ChangeDutyCycle(angle_to_duty_cycle(85))
        if i == 3:
            pwm.ChangeDutyCycle(angle_to_duty_cycle(86))
        if i == 5:
            pwm.ChangeDutyCycle(angle_to_duty_cycle(87))
        if i == 8:
            pwm.ChangeDutyCycle(angle_to_duty_cycle(88))
        turn_stepper(200)
        time.sleep(2)
    #GPIO.output(dir_pin,GPIO.HIGH)
    turn_stepper(185)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(96))

servo_pin = 17
dir_pin = 18
step_pin = 23
#number_of_turns = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(dir_pin,GPIO.OUT)
GPIO.setup(step_pin,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.output(24,GPIO.HIGH)
pwm = GPIO.PWM(servo_pin,50)
pwm.start(angle_to_duty_cycle(96))

#cards ready to enter
#set to 110 on startup, as a default position
#GPIO.output(dir_pin,GPIO.HIGH)
#turn_stepper(90)
GPIO.output(dir_pin,GPIO.LOW)
turn_stepper(185)

try:
    while True:
        check = input(str('say 1 '))
        if check == '1':
            pack_cycle()
except KeyboardInterrupt:
	GPIO.output(dir_pin,GPIO.LOW)
	#turn_stepper(110)
	turn_stepper(15)
	time.sleep(1)
	pwm.ChangeDutyCycle(angle_to_duty_cycle(95))
	GPIO.cleanup()
