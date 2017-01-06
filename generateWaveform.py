import RPi.GPIO as GPIO #GPIO pins for raspberry pi 
import time 		# for using functions like time	
from time import sleep	# for giving some delay
from sys import argv	# for taking argument at command line
import datetime		# for displaying current time 


# Pin 23 will be used to generate output waveform
# Define constants
constWaveformSignalPin = 23
positiveWidth = 0.003 
period = 0.2

# don't show me warnings like GPIO pin is already being used by other processes, just overwrite it. 
GPIO.setwarnings(False)

# We'll be using GPIO BCM notation for pinouts of raspberry pi
GPIO.setmode(GPIO.BCM)

# Set Pin 23 to generate output waveform
GPIO.setup(constWaveformSignalPin, GPIO.OUT)



# Generate PWM by keeping waveform pin high for 3 ms and then low for next 197 ms. 
# Total period will be approximately 200 ms and frequency will be 5 hz. 
try: 
	while True:
		GPIO.output(constWaveformSignalPin, 1)
		sleep(positiveWidth)
		GPIO.output(constWaveformSignalPin, 0)
		sleep((period - positiveWidth))
# release every gpio pin 
finally:
	GPIO.cleanup()

