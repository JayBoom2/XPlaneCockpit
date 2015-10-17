#!/usr/bin/env python3

#
# Contains the class which will handle UDP communication with XPlane
#

#
# Imports
#

import socketserver
import threading
import struct

#
# Class to handle receiving UDP data from XPlane
#
class XPlaneUDPHandler(socketserver.BaseRequestHandler):

	#
	# Handler for receving data
	#
	def handle(self):

		raw_data = self.request[0]
		unpacked_data = self.unpack_data(raw_data)
		print(unpacked_data)

	#
	# Unpack the UDP payload into a dict
	#
	# Returned dict format:
	# {<Index in XPlane Data Options>: [Item0, Item1, Item2, Item3, Item4, Item5, Item6, Item7]
	#
	# Note: If value of Item is -999 then that item is not used.
	#
	def unpack_data(self, buf):

		unpacked_data = {}
		payload = struct.iter_unpack('iffffffff', buf[5:])
		for item in payload:
			if item != None:
				unpacked_data[item[0]] = item[1:]
		return unpacked_data

#
# Class for threading mixin
#
class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
	pass

#
# Server Class
#
class XPlaneUDPServer():

	#
	# Init (Start the server)
	#
	def __init__(self, host='0.0.0.0', port=48000):

		self.server = ThreadedUDPServer((host, port), XPlaneUDPHandler)

		self.server_thread = threading.Thread(target=self.server.serve_forever)
		self.server_thread.daemon = False
		self.server_thread.start()

	#
	# Shutdown the server
	#
	def shutdown(self):

		self.server.shutdown()
