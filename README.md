# XPlaneCockpit
Hardware Cockpit using Arduino and RPI2 for XPlane 10.

Items with an asterisk are to-do and need to be created/completed.

RPI2 -> Software for the Raspberry Pi
	cockpit.py -> Runs the server, primary script. Right now it just runs the UDP server.
		*-> Needs to create an XPlaneUDPClient
		*-> Needs to create an "Aircraft" object
		*-> Needs to start an I2C server and have a loop for polling I2C devices.
		*-> Needs to handle back and forth of aircraft object info from I2C poll.

	XPlaneUDP -> Software for communicating with xplane using UDP
		server.py -> The code for the UDP server that receives data from xplane
			XPlaneUDPHandler -> socketserver subclass, handles xplane's UDP protocol. 
				*-> Will take an "aircraft" object so it can update attributes as they are received from xplane.
			XPlaneUDPServer -> Threaded server which uses XPlaneUDPHandler
		client.py -> The code for sending data to xplane
			XPlaneUDPClient -> Class which acts as a UDP client, sending data to xplane (the UDP server)
		receive.py -> Test script for receving data from xplane (server.py was created from this)
		send.py -> Test script for sending data to xplane using UDP
			XPlaneUDPClient -> Class which acts as a UDP client, sending data to xplane (the UDP server)
		*dataref_schema.json -> JSON which maps acutal aircraft options to their location in xplane dataref structures received via UDP (is this needed?)

	*Aircraft -> Software that abstracts making modifications to/from an "aircraft" in xplane.
		*aircraft.py -> Code for abstracting an "aircraft"
			*Aircraft -> Class which is an "aircraft", has attributes like, altitudle, airspeed, etc. Has methods to "set brakes", "set NAV1 Frequecy", etc. 
				-> Aircraft will take a "client" object to send to xplane.
				-> Aircraft will take an I2C "server" object to send data to I2C devices.

	I2C -> Software for interacting with the arduino using I2C
		blink.py -> Test script which blinks an LED connected to the RPI GPIO pins.
		i2c_read.py -> Test script for writing data to an arduino using I2C
		i2c_write.py -> Test script for writing data to an arduino using I2C
		*server.py -> The code for communicating on the I2C bus.
			*Server -> Class which handles writing to/from I2C bus.
				*-> Needs a "poll" method, which will query devices and return usable values (IDENT, NAV1 Frequency, etc)
