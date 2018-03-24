import RPi.GPIO as GPIO
import time  
import math

class DistanceSensor:
    
    def __init__(self, max_distance):
        #brings in array of data from laser 
        self.voltage_list = []
        #Plots an x and y coordinate graph
        self.world_size = max_distance ** 2 * pi
        
    def coordinates_converter(self, voltage, rps, speed, max_distance):
        millimeters_away = max_distance * (voltage / 5.0)
        
    