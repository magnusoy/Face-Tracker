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
eyes = Eyes()
servo = Servo()

# Gloabl varibales
offsetY = 90
offsetX = 90
outputX = offsetX
outputY = offsetY

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


# Main loop
if __name__ == "__main__":
    while(True):
        face_coordinates = eyes.detectFace()
        x = face_coordinates[0]
        y = face_coordinates[1]

        if x == 0:
            #servo.turnXAxis(offsetX)
            #servo.turnXAxis(offsetY)
            pass
        else:
            
            errorX = x - 320  # The error from the center X-axis
            errorY = y - 240  # The error from the center Y-axis
            print(errorX)
            # Will move until the error is lower than abs(3) in the X-axis
            if errorX > 3:
                outputX += 4
                outputX = constrain(outputX, 0, 180)
                servo.turnXAxis(outputX)
            elif errorX < -3:
                outputX -= 4
                outputX = constrain(outputX, 0, 180)
                

            # Will move until the error is lower than abs(3) in the Y-axis
            if errorY > 3:
                outputY = offsetY + 4
                outputY = constrain(outputY, 50, 120)
            elif errorY < -3:
                outputY = offsetY - 4
                outputY = constrain(outputY, 50, 120)

        servo.turnXAxis(outputX)
        servo.turnYAxis(outputY)
        
                
        key = waitKey(1)
        if key == 27:  # exit on ESC
            eyes.close()
            break
        
