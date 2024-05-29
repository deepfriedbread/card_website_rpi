import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16,frequency=50)

try:
	while True:
		angle = float(input('enter angle from 0 to 180'))
		if 0 <= angle <= 180:
			kit.servo[8].angle = angle
			#time.sleep(1)
		else:
			print('try again')

except KeyboardInterrupt:
	print('end')
    #kit.servo[0].angle = 90