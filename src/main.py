import math
import random
import matplotlib.pyplot as plt 
from robot import Robot
from data_process import DistanceSensor




def main():

	coordinate_data = []

	robot = Robot()
	laser = DistanceSensor()

	# x, y = laser.coordinates_converter(1.3, 210, 2000, 2000)


	voltage_list = [[.3, 130], [1.2, 800], [.8, 401]]

	for volt in range(len(voltage_list)):
		coordinate_data.append([laser.coordinates_converter(voltage_list[volt][0], voltage_list[volt][1], 2000, 2000)])



