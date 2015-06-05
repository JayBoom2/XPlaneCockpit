#!/usr/bin/env python3

#
# Blink an LED on GPIO pin 17
#

#
# Imports
#

from RPi import GPIO
from time import sleep
from sys import exit

def main():

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)

	while True:
		
		GPIO.output(17, True)
		sleep(1)
		GPIO.output(17, False)
		sleep(1)

if __name__ == '__main__':

	try:
		main()
	except	KeyboardInterrupt:
		GPIO.cleanup()
		exit(1)
