#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
docstring
"""

from servo import Servo
from eyes import Eyes
from pid import PID

eyes = Eyes()
servo = Servo()


running = True
offsetY = 80
offsetX = 90

def translate(x, lowerIn, upperIn, lowerOut, upperOut):
    """Map in value range to another range"""
    y = (x - lowerIn) / (upperIn - lowerIn) * (upperOut - lowerOut) + lowerOut
    return y


if __name__ == "__main__":
    while(running):
        face_coordinates = eyes.detectFace()
        x = translate(face_coordinates[0], 0, 640, 0, 180)
        y = translate(face_coordinates[1], 0, 480, 50, 110)
        servo.turnXAxis(x)
        servo.turnYAxis(y)
        