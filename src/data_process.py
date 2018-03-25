# import RPi.GPIO as GPIO
import time  
import math

class DistanceSensor:
    
    def __init__(self, max_distance):
    	#Milliseconds_full_circle- how many milliseconds for a full 360 degree rotation for the laser
    	#Max_distance- the length for a 5V reading 
        #brings in array of data from laser 
        self.voltage_list = []
        #Plots an x and y coordinate graph
        self.max_distance = max_distance

        self.world_size = max_distance ** 2 * pi

        self.milliseconds_full_circle = 0

        
    def coordinates_converter(self, voltage, millisec_from_beginning):
    	#Voltage- data given from the laserping reader. Ours ranged from .3 - 5V
    	#millisec_from_beginning- measure in milliseconds since beginning of calculation

        radius_in_millimeters = self.max_distance * (voltage / 5.0)

        degrees_of_rotation = (millisec_from_beginning / milliseconds_full_circle) * 360 

        x_coordinate, y_coordinate = radius_in_millimeters * sin(degrees_of_rotation), radius_in_millimeters * cos(degrees_of_rotation)

        return x_coordinate, y_coordinate
        
     