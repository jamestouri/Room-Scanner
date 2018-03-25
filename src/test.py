import math 
from math import pi, cos, sin
from data_process import DistanceSensor
 

# Testing 
def test_coordinates_converter():
	test_process = DistanceSensor()
	test_list = [.8, 401]

	output = test_process.coordinates_converter(test_list[0], test_list[1],  2000, 2000)
	assert (output == 320.0, 72.18)

print(test_coordinates_converter())

