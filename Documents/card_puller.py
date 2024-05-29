import RPi.GPIO as GPIO
import time

def angle_to_duty_cycle(angle):
    return 2.5 + (angle/18)

def turn_stepper(steps):
    for i in range(steps):
        GPIO.output(step_pin,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(step_pin,GPIO.LOW)
        time.sleep(0.001)

def card_grab():
	rack_pwm.ChangeDutyCycle(12.5)
	time.sleep(0.82)
	gripper_pwm.ChangeDutyCycle(angle_to_duty_cycle(60))
	time.sleep(0.1)
	rack_pwm.ChangeDutyCycle(2.5)
	time.sleep(0.82)
	gripper_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
	time.sleep(0.1)


def card_swipe(cards):
    GPIO.output(dir_pin,GPIO.HIGH)
    if cards >= 1:
        for i in range(cards):
            if i == 0:      
                platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
            if i == 2:
                platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
            if i == 3:
                platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(95))

            turn_stepper(200)
            card_grab()
            time.sleep(1)

gripper_pin = 17
rack_pin = 18
platform_pin = 27
dir_pin = 24
step_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(gripper_pin,GPIO.OUT)
GPIO.setup(rack_pin,GPIO.OUT)
GPIO.setup(platform_pin,GPIO.OUT)
GPIO.setup(dir_pin,GPIO.OUT)
GPIO.setup(step_pin,GPIO.OUT)

gripper_pwm = GPIO.PWM(gripper_pin, 50)
gripper_pwm.start(7.5)
gripper_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))

rack_pwm = GPIO.PWM(rack_pin, 50)
rack_pwm.start(7.5)

platform_pwm = GPIO.PWM(platform_pin, 50)
platform_pwm.start(angle_to_duty_cycle(90))



try:
    card_swipe(6)
    platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
    time.sleep(1)
    gripper_pwm.stop()
    rack_pwm.stop()
    platform_pwm.stop()
    GPIO.cleanup()
    

except KeyboardInterrupt:
    gripper_pwm.stop()
    rack_pwm.stop()
    platform_pwm.stop()
    GPIO.cleanup()
