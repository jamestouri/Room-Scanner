import math
import random
#import matplotlib.pyplot as plt
from data_process import DistanceSensor

laser_data_point = 0.0

landmarks = []

world = 0
world_border = 0

class Robot:
    # Class for Robot Object
    def __init__(self):
        # Place robot on random parts of the map
        self.x = random.random() * world
        self.y = random.random() * world
        self.orientation = random.random() * 2.0 * pi
        
        self.forward_noise = 0.0 #Noise of forward movement
        self.turn_noise = 0.0 # Noise of turn
        self.sense_noise = 0.0 #noise of the sensing
        
        
    def set(set, coordinate_x, coordinate_y, orientation):
        #Robot moves in environment 
        
        if coordinate_x <= 0 or coordinate_x >= world_border:
            raise ValueError('X coordinate out of bounds')
        if coordinate_y <= 0 or coordinate_y >= world_border:
            raise ValueError('Y coordinate out of bounds')
        if orientation <= 0 or orientation >= 2 * pi:
            raise ValueError('Orientation out of bounds')

        self.x = float(coordinate_x)
        self.y = float(coordinate_y)
        self.orientation = float(orientation)
        
    def set_noise(self, new_forward_noise, new_turn_noise, new_sense_noise):
        #Noise Parameters
        
        self.forward_noise = float(new_forward_noise)
        self.turn_noise = float(new_turn_noise)
        self.sense_noise = float(new_sense_noise)
        
    def sense(self):
        # Distances in landmarks  Returns the distances of landmarks 
        
        distances = []
        
        # Guassian probability
        for landmark in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[landmark][0]) ** 2 + (self.y -landmarks[landmark][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            distances.append(dist)
            
        return distances
    
    def move(self, turn, forward):
        #Controlling Robots movement and turns 
        
        if forward < 0:
            raise ValueError("Have Robot turn instead of moving backward")
        
        # Turn with randomness on the command 
        orientation = self.orientation + float(turn) + random.gauss(0.0, self.turn_noise)
        orientation %= 2 * pi
        
        # Move with random noise 
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        
        # cyclic truncate 
        x %= world_size
        x %= world_size
        
        #set particle 
        res = RobotClass()
        res.set(x, y, orientation)
        res.set_noise(self.forward_noise, self.turn_noise, self.sense)
        
        
        return res
    
    @staticmethod
    def gaussian(mu, sigma, x):
        #mu- Distance to landmark
        #sigma- standard deviation
        #x- distance to landmark from robot
        
        #Calculating Gaussian Probability
        return exp(- ((mu -x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    
    
    def measurement(self, measurement):
        prob = 1.0
        
        for landmark in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[landmark][0]) ** 2 + (self.y -landmarks[landmark][1]) ** 2)
            prob *= self.gaussian(dist, self.sense_noise, measurement[i])
        return prob
        
        
        
        
