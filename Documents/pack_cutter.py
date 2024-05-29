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

def cut_cycle():
    #set position
    platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(140))
    rack_pwm.ChangeDutyCycle(angle_to_duty_cycle(100))
    time.sleep(3)
    #robot arm will insert pack here
    #cut pack
    platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(170))
    time.sleep(0.5)
    platform_pwm.ChangeDutyCycle(angle_to_duty_cycle(125))
    time.sleep(0.1)
    rack_pwm.ChangeDutyCycle(angle_to_duty_cycle(30))
    time.sleep(1)
    anticlockwise(scissormotor_pin1,scissormotor_pin2)
    time.sleep(1.6)
    stop(scissormotor_pin1,scissormotor_pin2)
    time.sleep(2)
    clockwise(scissormotor_pin1,scissormotor_pin2)
    time.sleep(1.6)
    stop(scissormotor_pin1,scissormotor_pin2)

gripper_pin = 17
rack_pin = 18
platform_pin = 27
scissormotor_pin1 = 23
scissormotor_pin2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(gripper_pin,GPIO.OUT)
GPIO.setup(rack_pin,GPIO.OUT)
GPIO.setup(platform_pin,GPIO.OUT)
GPIO.setup(scissormotor_pin1,GPIO.OUT)
GPIO.setup(scissormotor_pin2,GPIO.OUT)

gripper_pwm = GPIO.PWM(gripper_pin, 50)
gripper_pwm.start(7.5)

rack_pwm = GPIO.PWM(rack_pin, 50)
rack_pwm.start(7.5)

platform_pwm = GPIO.PWM(platform_pin, 50)
platform_pwm.start(7.5)

stop(scissormotor_pin1,scissormotor_pin2)

try:
    time.sleep(1)
    cut_cycle()
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
