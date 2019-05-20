
import time

class PID():

    def __init__(self, kp, ki, kd, direction):
        self.direction = direction
        self.setParams(kp, ki, kd)
    
    @classmethod
    def millis(self):
        return int(round(time.time() * 1000))


    def compute(self, actual, target):
        pass
        
    
    def setParams(self, kp, ki, kd):
        sampleTimeInSec = self.sampleTime / 1000
        self.kp = kp
        self.ki = ki * sampleTimeInSec
        self.kd = kd * sampleTimeInSec

        if(self.controllerDirection == "REVERSE"):
            self.kp = (0 - kp)
            self.ki = (0 - ki)
            self.kd = (0 - kd)

    def setOutputOffset(self, offset):
        pass
    
    def setOutputLimits(self, low, high):
        pass

    def setUpdateTime(self, updateTime):
        pass