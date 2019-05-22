#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Face Tracker main application
"""

# Importing packages
from servo import Servo
from eyes import Eyes
from cv2 import waitKey
import time

# Create objects
camera = Eyes()
body = Servo()

outX = 90
outY = 90

def constrain(x, low, high):
    """ Constrains the input to the lower
    and upper limit"""

    if x < low:
        y = low
    elif x > high:
        y = high
    else:
        y = x
    return y

def translate(x, lowerIn, upperIn, lowerOut, upperOut):
    """Map in value range to another range"""
    y = (x - lowerIn) / (upperIn - lowerIn) * (upperOut - lowerOut) + lowerOut
    return y

def millis():
        return int(round(time.time() * 1000))
    
lastCall = millis()
# Main loop
if __name__ == "__main__":
    while(True):
        faceCoords = camera.detectFace(False)
        x = faceCoords[0]
        y = faceCoords[1]
        if x > 0:     
            if millis() > lastCall:
                outX = translate(x, 0, 640, 50, 120)
                outY = translate(y, 0, 480, 70, 110)
                lastCall = millis() + 1
   
            
        body.turnXAxis(outX)
        body.turnYAxis(outY)
        
                
        key = waitKey(1)
        if key == 27:  # exit on ESC
            eyes.close()
            break
        
