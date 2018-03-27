import math
import random
import matplotlib.pyplot as plt 
from robot import Robot
from data_process import DistanceSensor
import time 




def main():
	#List of coordinated Data
	coordinate_data = []
	robot = Robot()
	laser = DistanceSensor()

	# x, y = laser.coordinates_converter(1.3, 210, 2000, 2000)
	#Sleep for 10 seconds to give us time to get everything set 
	time.sleep(10)
	voltage_list = laser.record_voltage_and_time(12, 10, 18, 31, 10, 2000)

	
	#Converting coordinates from voltages to X and Y plane
	for volt in range(len(voltage_list)):
		coordinate_data.append([laser.coordinates_converter(voltage_list[volt][0], voltage_list[volt][1], 2000, 2000)])



