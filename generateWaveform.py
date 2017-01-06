
import RPi.GPIO as GPIO #GPIO pins for raspberry pi 
import time 		# for using functions like time	
from time import sleep	# for giving some delay
from sys import argv	# for taking argument at command line
import datetime		# for displaying current time 

import sys, getopt	# for parsing arguments on command line

# Pin 23 will be used to generate output waveform
# Define constants
constWaveformSignalPin = 23
positiveWidth = 0.003 
period = 0.2
frequency = 0

# don't show me warnings like GPIO pin is already being used by other processes, just overwrite it. 
GPIO.setwarnings(False)

# We'll be using GPIO BCM notation for pinouts of raspberry pi
GPIO.setmode(GPIO.BCM)

# Set Pin 23 to generate output waveform
GPIO.setup(constWaveformSignalPin, GPIO.OUT)

# argv = all the arguments except 0 which is file name
argv = sys.argv[1:]


# setup values of opts and args
try:	
	opts, args = getopt.getopt(argv, "h:f:", ["help", "frequency="])

except getopt.GetoptError:
	print 'exampleFile.py -f <ExampleFrequency>'
	sys.exit(2)

if not opts:
	print 'Please enter frequnecy'
	print 'exampleFile.py -f <ExampleFrequency>'
	sys.exit(2)

# go through argument values and parse them
for opt, arg in opts:
	if opt in ("-h", "--help"):
		print 'exampleFile.py -f <ExampleFrequency>'
		sys.exit()
	elif opt in ("-f", "--frequency"):
		frequency =  arg


#calculate period based on the frequcney
try: 
	period = 1 / float(frequency)
except ZeroDivisionError: 
	print 'frequency is 0. 1 / 0. Unable to calculat Period. Setting period back to default 0.2'
	period = 0.2

print "Value of frequency"
print frequency

print "Value of period"
print period



# Generate PWM by keeping waveform pin high for 3 ms and then low for next 197 ms. 
# Total period will be approximately 200 ms and frequency will be 5 hz. 
try: 
	while True:
		GPIO.output(constWaveformSignalPin, 1)
		sleep(positiveWidth)
		GPIO.output(constWaveformSignalPin, 0)
		try: 
			sleep((period - positiveWidth))
		except IOError: 
			print 'Remember: period can\'t be less than positive Width of the waveform. Invalid frequency selected'
			sys.exit(2)
# release every gpio pin 
finally:
	GPIO.cleanup()

