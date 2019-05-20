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
pidX = PID(1.0, 0.0, 0.0)

running = True

if __name__ == "__main__":
    while(running):
        face_coordinates = eyes.detectFace()
