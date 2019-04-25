import RPi.GPIO as GPIO
import time

class Distance():
    GPIO_TRIGGER = 18
    GPIO_ECHO = 24
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def getDistance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
    
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
            
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
            
        TimeElapsed = StopTime - StartTime
        
        distance = (TimeElapsed * 34300) / 2
        
        return distance