# Room-Scanner
Raspberry Pi takes 360 degree view and clicks data points to understand its environment.  Collaborative project by James Touri and Alex Henderson

The room scanner takes data from it’s surroundings with a 1D laser to build a simulated environment for a robot to understand landmarks and move around with Gaussian Probability for localization solutions. 

## What it does
The room scanner is a device that is powered by a raspberry pi and uses a LaserPing to scan distances of the objects close by.  It uses a 1D signal and gives a voltage as a reading to describe how many volts it has to exert to reach an object.  The distances are then converted to X and Y coordinates based on the voltage and the milliseconds calculated to find number of degrees.

## Requirements and Dependencies

Python 3
[Raspberry pi](https://www.raspberrypi.org/)

[Matplotlib](https://matplotlib.org/users/installing.html)

[LaserPing by Parallax](https://www.parallax.com/product/28041) 

[Arduino analog reading converter](https://www.arduino.cc/en/Tutorial/ReadAnalogVoltage)

[RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

## Building the Device

![](https://github.com/jamestouri/Room-Scanner/blob/master/20180325_1730261.jpg)
Powered and run by a Raspberry Pi 3, a 3d printed rotary table turns via a geared DC can motor. The motor will be run via a 11.1v lipoly battery and the pi will be run using a 7.4v lipoly battery and a 5v switching regulator. We are utilizing a Laser PING IR rangefinder that we be switched from analog to digital signal via a Arduino nano.

We will be running the motor at 10V with a voltage regulator to ensure the motor stays at 10V and constant speed (if this proves to be a problem we will look into a geared motor with an encoder and mosfet).

## Converting the data points from the voltage

The data points were received in voltages and milliseconds.  It took approximately 2000 milliseconds (2 seconds) to go in a full rotation, and we recorded the time it received a certain voltage.  From there we converted the time it took to attain that voltage and attained the degrees.  You can see the function more in depth from the data_process.py, DistanceSensor Class.


From there we plot them on a X and Y plane to create an environment for the robot to maneuver around it. In the robot.py file, we have a robot class for sensing where it is based on the landmarks from the voltages provided with random noise. 


## Next steps

We have not added random noise to the raspberry pi device as it rotates in a circle, for which we will. We would also like to add the ability for the robot to get from point A to B with that is optimal with and goes around landmarks correctly. 

