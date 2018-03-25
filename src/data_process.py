# import RPi.GPIO as GPIO
import time  
from math import sin, cos
from math import pi


class DistanceSensor:
    
    def __init__(self):
    	
        #Plots an x and y coordinate graph
        self.radius = 0.0


        
    def coordinates_converter(self, voltage, millisec_from_beginning, max_distance, milliseconds_full_circle):
    	#Voltage- data given from the LaserPing reader. Ours ranged from .3 - 5V
    	#millisec_from_beginning- measure in milliseconds since beginning of calculation
    	#Milliseconds_full_circle- how many milliseconds for a full 360 degree rotation for the laser
    	#Max_distance- the length for a 5V reading 
    	
        radius_in_millimeters = float(max_distance * (voltage / 5.0))
        print(radius_in_millimeters)

        degrees_of_rotation = float((millisec_from_beginning / milliseconds_full_circle) * 360)
        print(degrees_of_rotation)

        x_coordinate, y_coordinate = float(radius_in_millimeters * sin(degrees_of_rotation)), float(radius_in_millimeters * cos(degrees_of_rotation))

        return x_coordinate, y_coordinate 
        
     