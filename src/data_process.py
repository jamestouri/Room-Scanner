import RPi.GPIO as GPIO
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

    # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    def record_voltage_and_time(adcnum, clockpin, mosipin, misopin, cspin, milliseconds_full_circle):
        # the raspberry pi comes in digital data, or 1's and 0's. We need to read it in analog data
        if ((adcnum > 7) or (adcnum < 0)):
            return -1
         # We will be returning this list
        voltage_list = [] 


        while i < milliseconds_full_circle + 1:
            GPIO.output(cspin, True)
            GPIO.output(clockpin, False)  
            GPIO.output(cspin, False)
            commandout = adcnum
            commandout |= 0x18  # start bit + single-ended bit
            commandout <<= 3    # we only need to send 5 bits here
            for i in range(5):
                    if (commandout & 0x80):
                            GPIO.output(mosipin, True)
                    else:
                            GPIO.output(mosipin, False)
                    commandout <<= 1
                    GPIO.output(clockpin, True)
                    GPIO.output(clockpin, False)
     
            adcout = 0
            # read in one empty bit, one null bit and 10 ADC bits
            for i in range(12):
                    GPIO.output(clockpin, True)
                    GPIO.output(clockpin, False)
                    adcout <<= 1
                    if (GPIO.input(misopin)):
                            adcout |= 0x1
     
            GPIO.output(cspin, True)
            


            # set up the SPI interface pins
            GPIO.setup(SPIMOSI, GPIO.OUT)
            GPIO.setup(SPIMISO, GPIO.IN)
            GPIO.setup(SPICLK, GPIO.OUT)
            GPIO.setup(SPICS, GPIO.OUT)
             
            # 10k trim pot connected to adc #0
            potentiometer_adc = 0;
        
           
            
            # Here to gather the voltage data and read them in Analog time
            voltage_point = adcout * (5.0 / adcout) 
            time.sleep(0.001)
            voltage_list.append((voltage_point, i))
            i += 1
        return voltage_list


        
     