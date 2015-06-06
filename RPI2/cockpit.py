#!/usr/bin/env python3

#
# This is the main script that will run the cockpit program
#

#
# Imports
#
import XPlaneUDP
from time import sleep

#
# Main
#

def main():
	try:
		server = XPlaneUDP.Server()
		while True:
			sleep(1)

	except KeyboardInterrupt:
		server.shutdown()

if __name__ == '__main__':
	main()
