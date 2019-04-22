#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
docstring
"""

from serialhandler import SerialCommunication
from eyes import Eyes

arduino = SerialCommunincation("COM3", 9600)
eyes = Eyes()

if __name__ == "__main__":
    while(arduino.isConnected()):
        face_coordinates = eyes.detectFace()
        data = ','.join(map(str, face_coordinates))
        arduino.sendOutputStream(data)

