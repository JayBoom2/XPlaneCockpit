#!/usr/bin/env python3

#
# Send data to a listening xplane
#

#
# Imports
#

import struct
import socket

class XPlaneUDPClient(object):

	def __init__(self, ip, port):

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.ip = ip
		self.port = port

	def send_data(self, index, item, value):

		payload = self.pack_data(index, item, value)
		self.socket.sendto(payload, (self.ip, self.port))

	def pack_data(self, index, item, value):

		header = struct.pack('5s', b'DATA\0')
		data_buf = bytearray(struct.pack('iffffffff', index, -999, -999, -999, -999, -999, -999, -999, -999))
		struct.pack_into('f', data_buf, (item+1)*4, value)
		return header + data_buf

if __name__ == '__main__':
	HOST, PORT = 'localhost', 49000
	client = XPlaneUDPClient(HOST, PORT)
	client.send_data(14, 1, 0.5) # This example sets the brakes
