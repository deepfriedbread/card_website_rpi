import RPi.GPIO as GPIO
import time

def angle_to_dc(angle):
        return 2.5 + (angle/18)

step_pin = 23  # Step pin
dir_pin = 18   # Direction pin
servo_pin = 17

# Set the GPIO mode and setup the pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

# Set the direction (CW or CCW)
GPIO.output(dir_pin, GPIO.HIGH)  # GPIO.HIGH for clockwise (CW), GPIO.LOW for counterclockwise (CCW)
for i in range(110):
	GPIO.output(step_pin,GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(step_pin,GPIO.LOW)
	time.sleep(0.001)

GPIO.output(dir_pin,GPIO.LOW)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(angle_to_dc(85))

# Number of steps and delay between steps (adjust as needed)
num_steps = 200
delay = 0.001

try:
        while True:
                tryagain = int(input('steps '))
                if tryagain > 1:
                        for i in range(tryagain):
                                GPIO.output(step_pin,GPIO.HIGH)
                                time.sleep(0.001)
                                GPIO.output(step_pin, GPIO.LOW)
                                time.sleep(0.001)
except KeyboardInterrupt:
        pwm.ChangeDutyCycle(angle_to_dc(90))
        pwm.stop()
        GPIO.cleanup()
