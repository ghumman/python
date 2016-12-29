import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.OUT)


finalTime = time.time() 
frequency = 0

def my_callback(channel):
	if GPIO.input(25):
		global finalTime
		global frequency
		start = time.time()
		duration = start - finalTime 
		frequency = 1 / duration
		print frequency
		finalTime = time.time() 
	
GPIO.add_event_detect(25, GPIO.RISING, callback=my_callback, bouncetime=80)

GPIO.output(24, 0)
lowFreq = 0

try: 
	while True:
	
		print "Frequency before if function"
		print frequency
		if frequency < 4: 
			print "Inside frequency < 4"
			lowFreq+=1
			if lowFreq > 4:
				print "Frequency has gone below 4"
				GPIO.output(24, 1)
		sleep(1)


finally:
	GPIO.clearnup()


