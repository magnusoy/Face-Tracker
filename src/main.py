#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Face Tracker main application
"""

# Importing packages
from servo import Servo
from eyes import Eyes
from pid import PID

# Create objects
eyes = Eyes()
servo = Servo()
pidX = PID(kp=2.0, ki=0.0, kd=0.0, direction="DIRECT")
pidY = PID(kp=2.0, ki=0.0, kd=0.0, direction="DIRECT")

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


pidX.setUpdateTime(50)
pidY.setUpdateTime(50)

pidX.setOutputOffset(90)
pidY.setOutputOffset(90)

pidX.setOutputLimits(0, 180)
pidX.setOutputLimits(50, 130)

# Main loop
if __name__ == "__main__":
    while(True):
        face_coordinates = eyes.detectFace()
        x = face_coordinates[0]
        y = face_coordinates[1]

        outputX = pidX.compute(x, 320)
        outputY = pidY.compute(y, 240)

        servo.turnXAxis(outputX)
        servo.turnYAxis(outputY)
