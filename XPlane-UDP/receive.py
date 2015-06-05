#!/usr/bin/env python3

#
# Receive data from xplane
#

#
# Imports
#

import socketserver
import threading
import struct

class XPlaneUDPHandler(socketserver.BaseRequestHandler):

	def handle(self):

		raw_data = self.request[0]
		unpacked_data = self.unpack_data(raw_data)
		print(unpacked_data)

	def unpack_data(self, buf):

		unpacked_data = {}
		payload = struct.iter_unpack('iffffffff', buf[5:])
		for item in payload:
			if item != None:
				unpacked_data[item[0]] = item[1:]
		return unpacked_data
		

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
	pass

if __name__ == '__main__':
	HOST, PORT = 'localhost', 48000
	server = ThreadedUDPServer((HOST, PORT), XPlaneUDPHandler)

	try:
		server_thread = threading.Thread(target=server.serve_forever)
		server_thread.daemon = False
		server_thread.start()
	except KeyboardInterrupt:
		server.shutdown()
