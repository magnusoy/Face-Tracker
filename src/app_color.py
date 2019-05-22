#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Face Tracker main application
"""

# Importing packages
from servo import Servo
from color_tracking import ObjectTracker
import cv2
import time

# Create servo object
body = Servo()

outX = 90
outY = 90


def translate(x, lowerIn, upperIn, lowerOut, upperOut):
    """Map in value range to another range"""
    y = (x - lowerIn) / (upperIn - lowerIn) * (upperOut - lowerOut) + lowerOut
    return y


def millis():
    """ Returns current time in milliseconds."""
    return int(round(time.time() * 1000))


# Main loop
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    camera = ObjectTracker(capture=cap, watch=True)
    lastCall = millis()
    while(True):
        faceCoords = camera.getCoordinates()
        x = faceCoords[0]
        y = faceCoords[1]
        if x > 0:
            if millis() > lastCall:
                outX = translate(x, 0, 640, 50, 120)
                outY = translate(y, 0, 480, 70, 110)
                lastCall = millis() + 1

        body.turnXAxis(outX)
        body.turnYAxis(outY)

        key = cv2.waitKey(1)
        if key == 27:  # exit on ESC
            camera.stop()
            break
