#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Face Tracker main application
"""

# Importing packages
from servo import Servo
from eyes import Eyes
from cv2 import waitKey

# Create objects
camera = Eyes()
body = Servo()


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

# Main loop
if __name__ == "__main__":
    while(True):
        faceCoords = camera.detectFace()
        x = faceCoords[0]
        y = faceCoords[1]

        outX = translate(x, 0, 640, 0, 180)
        outY = translate(y, 0, 480, 0, 180)

        body.turnXAxis(outX)
        body.turnYAxis(outY)
        
                
        key = waitKey(1)
        if key == 27:  # exit on ESC
            eyes.close()
            break
        
