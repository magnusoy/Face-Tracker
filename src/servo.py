# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 Adafruit Servokit wrapper for easy usages.
"""

# Importing servo package
from adafruit_servokit import ServoKit


class Servo(object):
    """Servo controller for both axes."""

    def __init__(self, channels=16):
        self.kit = ServoKit(channels=channels)
    
    def turnYAxis(self, position):
        """ Turns Y-axis to the given position."""
        self.kit.servo[0].angle = position
    
    def turnXAxis(self, position):
        """ Turns X-axis to the given position."""
        self.kit.servo[1].angle = position
