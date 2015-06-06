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
	#bus.write_i2c_block_data(4, 0xFF, output_array)
	data = bus.read_i2c_block_data(4, 0xFF)
	print(bytes(data))
	data2 = bus.read_word_data(4, 0xFF)
	print(data2)

if __name__ == '__main__':
	main()
