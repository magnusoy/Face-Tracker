#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Face Tracker main application
"""

# Importing packages
from servo import Servo
from eyes import Eyes

# Create objects
eyes = Eyes()
servo = Servo()

# Gloabl varibales
offsetY = 80
offsetX = 90


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
            servo.turnXAxis(offsetX)
            servo.turnXAxis(offsetY)
        else:
            errorX = x - 320  # The error from the center X-axis
            errorY = y - 240  # The error from the center Y-axis

            # Will move until the error is lower than abs(3) in the X-axis
            if errorX > 3:
                outputX = offsetX + 2
                outputX = constrain(offsetX, 0, 180)
                servo.turnXAxis(outputX)
            elif errorX < -3:
                outputX = offsetX - 2
                outputX = constrain(offsetX, 0, 180)
                servo.turnXAxis(outputX)

            # Will move until the error is lower than abs(3) in the Y-axis
            if errorY > 3:
                outputY = offsetY + 2
                outputY = constrain(offsetY, 50, 120)
                servo.turnXAxis(outputY)
            elif errorY < -3:
                outputY = offsetY - 2
                outputY = constrain(offsetY, 50, 120)
                servo.turnXAxis(outputY)
