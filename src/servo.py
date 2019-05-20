# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

from adafruit_servokit import ServoKit

class Servo(object):

    def __init__(self, channels=16):
        self.kit = ServoKit(channels=channels)
    
    def turnYAxis(self, position):
        self.kit.servo[0].angle(position)
    
    def turnXAxis(self, position):
        self.kit.servo[1].angle(position)
