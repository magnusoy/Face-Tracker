#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Face Tracker main application
"""

# Importing packages
from servo import Servo
from eyes import Eyes
from pid import PID
from cv2 import waitKey

# Create objects
eyes = Eyes()
servo = Servo()
pidX = PID(kp=0.1, ki=0.0, kd=0.07, direction="REVERSE")
pidY = PID(kp=0.1, ki=0.0, kd=0.07, direction="REVERSE")


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


pidX.setUpdateTime(40)
pidY.setUpdateTime(40)

pidX.setOutputOffset(90)
pidY.setOutputOffset(90)

pidX.setOutputLimits(0, 180)
pidY.setOutputLimits(0, 180)

# Main loop
if __name__ == "__main__":
    while(True):
        face_coordinates = eyes.detectFace(True)
        x = face_coordinates[0]
        y = face_coordinates[1]
        #print(face_coordinates)

        outputX = pidX.compute(x, 302)
        outputY = pidY.compute(y, 191)
        #print((outputX, outputY))
        servo.turnXAxis(outputX)
        servo.turnYAxis(outputY)

        key = waitKey(1)
        if key == 27:  # exit on ESC
            eyes.close()
            break
