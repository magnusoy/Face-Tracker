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


class Tracker(object):

    def __init__(self, offset, gain):
        self.output = 0.0
        self.gain = gain
        self.offset = offset

    @classmethod
    def constrain(self, x, low, high):
        if x < low:
            y = low
        elif x > high:
            y = high
        else:
            y = x
        return y

    def track(self, actual, target):
        if actual > 0:
            error = target - actual
            self.output = self.offset + (error * self.gain)
            if error > 2:
                self.output += 2
            elif error < -2:
                self.output -= 2
            self.output = self.constrain(self.output, 0, 180)
        return self.output


# Create objects
camera = Eyes()
body = Servo()
trackX = Tracker(offset=90, gain=0.1)
trackY = Tracker(offset=90, gain=0.1)

# Main loop
if __name__ == "__main__":
    while(True):
        faceCoords = camera.detectFace()
        outX = trackX.track(faceCoords[0], 310)
        outY = trackX.track(faceCoords[1], 190)
        body.turnXAxis(outX)
        body.turnYAxis(outY)

        key = waitKey(1)
        if key == 27:  # exit on ESC
            eyes.close()
            break

