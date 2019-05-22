#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing packages
import numpy as np
import cv2


class Eyes(object):
    """ Eyes is used to find the face and track
    the center.
    """

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            '../static/haarcascades/haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(propId=3, value=640)
        self.cap.set(propId=4, value=480)

    def detectFace(self, showFrame=False):
        """ Finds face and returns the center coordinates."""
        center = (0, 0)
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            face = faces[0]
            center = (face[0] + (0.5*face[2]), face[1] + (0.5*face[3]))
            cv2.circle(gray, (int(center[0]), int(
                center[1])), 5, (0, 0, 255), -3)
        if showFrame:
            cv2.imshow("Preview", gray)
        return center

    def close(self):
        """ Stops the camera, closing all windows."""
        self.cap.release()
        cv2.destroyAllWindows()


# Example of usage
if __name__ == "__main__":
    eyes = Eyes()

    while True:
        faces = eyes.detectFace(showFrame=True)
        key = cv2.waitKey(1)
        if key == 27:  # exit on ESC
            eyes.close()
            break
