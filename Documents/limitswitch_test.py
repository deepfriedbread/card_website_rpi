import RPi.GPIO as GPIO
import time

limit_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(limit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

prev_switch_state = GPIO.input(limit_pin)

try:
    # Main loop
    while True:
        switch_state = GPIO.input(limit_pin)
        # Check if the state has changed since the last iteration
        if switch_state == GPIO.LOW and prev_switch_state == GPIO.HIGH:
            print("Button pressed")

        # Update the previous state
        prev_switch_state = switch_state

        # Optional: Add a small delay to reduce CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()