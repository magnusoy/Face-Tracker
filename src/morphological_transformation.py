#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Finding right HSV settings for
locating objects.

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import cv2
import numpy as np


def nothing(x):
    pass


# Start recording on camera
cap = cv2.VideoCapture(0)
# Creates a window containing trackbars
Trackbars = np.zeros([100, 700], np.uint8)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
cv2.createTrackbar('S ROWS', 'Trackbars', 0, 480, nothing)
cv2.createTrackbar('E ROWS', 'Trackbars', 480, 480, nothing)
cv2.createTrackbar('S COL', 'Trackbars', 0, 640, nothing)
cv2.createTrackbar('E COL', 'Trackbars', 640, 640, nothing)

while True:

    # Take each frame
    _, frame = cap.read()

    # Convert RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    s_r = cv2.getTrackbarPos('S ROWS', 'Trackbars')
    e_r = cv2.getTrackbarPos('E ROWS', 'Trackbars')
    s_c = cv2.getTrackbarPos('S COL', 'Trackbars')
    e_c = cv2.getTrackbarPos('E COL', 'Trackbars')

    roi = frame[s_r: e_r, s_c: e_c]

    # Reads trackbar position
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    # Assign trackbar values to HSV-limits.
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    # Creates a mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Removing noise and enlarging the mask
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel)
    dilation = cv2.dilate(mask, kernel)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    result = cv2.bitwise_and(roi, roi)

    # Show frame different frames
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("erosion", erosion)
    cv2.imshow("dilation", dilation)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)
    cv2.imshow("Result", result)

    # Break loop with ESC-key
    key = cv2.waitKey(1)
    if key == 27:
        break

# Close all windows
cap.release()
cv2.destroyAllWindows()
