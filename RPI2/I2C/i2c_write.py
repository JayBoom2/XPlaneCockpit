#!/usr/bin/env python3

#
# Test script to write bytes to i2c device
#

#
# Imports
#

import smbus

def main():
	bus = smbus.SMBus(1)
	output = 'Test'
	output_array = []
	for byte in str.encode(output):
		output_array.append(byte)
		print(byte)
	#	bus.write_byte(4, byte)
	bus.write_i2c_block_data(4, 0xFF, output_array)

if __name__ == '__main__':
	main()
