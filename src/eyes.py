#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2


class Eyes(object):
    """
    docstring
    """

    def __init__(self):        
        self.face_cascade = cv2.CascadeClassifier('../static/haarcascades/haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(propId=3, value=640)
        self.cap.set(propId=4, value=480)
    
    def detectFace(self):
        """
        docstring
        """
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) > 0:
            face = faces[0]
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            center = ((face[0] + face[1]) / 2, (face[1] + face[3]) / 2)
            #cv2.circle(frame, (int(center[0]), int(center[1])), 3, (0, 0, 255), -3)
            #return center
        cv2.imshow("preview", frame)
        return 0, 0
    
    def close(self):
        """
        docstring
        """
        self.cap.release()
        cv2.destroyAllWindows()

    def showFrame(self):
        ret, frame = self.cap.read()
        cv2.imshow("Frame", frame)


eyes = Eyes()

while True:
    faces = eyes.detectFace()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
