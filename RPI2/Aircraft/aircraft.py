#!/usr/bin/env python3

#
# Create an "aircraft" which will handle coordinating and managing attributes.
#

#
# Imports
#

class Aircraft(object):

	def __init__(self):

		# Aircraft attributes

		# Speed, position, etc.
		self.kias = 0 # knots
		self.ktas = 0 # knots
		self.vvi = 0 # fpm (vertical indicated)
		self.pitch = 0 # degrees
		self.roll = 0 # degrees
		self.true_heading = 0 # degrees
		self.magnetic_heading = 0 # degrees
		self.altitude = 0 # indicated in feet

		# Equipment
		self.gear = 0 # gear position
		self.wbrake = 0 # parking brake
		self.prop = 0 # prop position (for constant speed)

		# Engine
		self.throttle = 0 # throttle position
		self.mixture = 0 # ratio
		self.carb_heat = 0 # ratio
		self.magneto = 0 # switch position
		self.starter = 0
		self.rpm = 0 
		self.oil_pressure = 0 # psi
		self.oil_temperature = 0 # degrees
		self.fuel_pressure = 0 # psi
		self.fuel_pump 0 # fuel pump switch on/off

		# Electrical
		self.battery_amps = 0
		self.battery_volts = 0
		self.generator = 0 # amps
		self.battery_switch = 0
		self.generator_switch = 0
		
		# COM
		self.com1_freq = 0
		self.com1_stby = 0
		self.com2_freq = 0
		self.com2_stby = 0

		# NAV
		self.nav1_freq = 0
		self.nav1_stby = 0
		self.nav1_obs = 0 # obs dial degrees
		self.nav1_flag = 0
		self.nav1_type = 0
		self.nav1_to_from = 0
		self.nav1_magnetic_course = 0 # degrees
		self.nav1_relative_bearing = 0 # degrees
		self.nav1_dme_distance = 0 
		self.nav1_horizontal_deflection = 0
		self.nav1_vertical_deflection = 0

		self.nav2_freq = 0
		self.nav2_stby = 0
		self.nav2_obs = 0 # obs dial degrees
		self.nav2_flag = 0
		self.nav2_type = 0
		self.nav2_to_from = 0 
		self.nav2_magnetic_course = 0 # degrees
		self.nav2_relative_bearing = 0 # degrees
		self.nav2_dme_distance = 0 
		self.nav2_horizontal_deflection = 0
		self.nav2_vertical_deflection = 0

		# ADF
		self.adf_freq = 0
		self.adf_card_heading = 0
		self.adf_relative_bearing = 0
		self.adf_type = 0

		# DME
		self.dme_mode = 0
		self.dme_dist = 0
		self.dme_speed = 0
		self.dme_time = 0
		self.dme_freq = 0

		# GPS
		self.gps_mode = 0
		self.gps_dist = 0
		self.gps_obs = 0 # obs dial setting for GPS degrees
		self.gps_magnetic_course = 0 # degrees
		self.gps_relative_bearing = 0 # degrees
		self.gps_horizontal_deflection = 0 # in dots
		self.gps_vertical_deflection = 0 # in dots

		# Transponder
		self.transponder_mode = 0
		self.transponder_setting = 1200
		self.transponder_ident = 0 # If ident button is pushed
		self.transponder_interrogate = 0 # For blinkly transponder light

		# Marker
		self.outer_marker = 0
		self.middle_marker = 0
		self.inner_marker = 0
		self
