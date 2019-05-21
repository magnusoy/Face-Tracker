
import time

class PID():

    def __init__(self, kp, ki, kd, direction):
        self.direction = direction
        self.updateTime = 10
        self.setParams(kp, ki, kd)
        self.outputLast = 0.0
        self.outputSum = 0.0
        self.error = 0.0
        self.outputLimitLow = 0.0
        self.outputLimitHigh = 0.0
        self.lastUpdateTime = self.millis()
        self.outputValue = 90
        

    
    @classmethod
    def millis(self):
        return int(round(time.time() * 1000))


    def compute(self, actual, target):
        if actual > 0:
            lastError = self.error
            self.error = target - actual

            output = self.error * self.kp
            self.outputSum += self.error * self.ki
            self.outputLast = (lastError - self.error) * self.kd
            self.outputValue = self.offset + output + self.outputSum + self.outputLast
            if self.outputValue > self.outputLimitHigh:
                self.outputValue = self.outputLimitHigh
            if self.outputValue < self.outputLimitLow:
                self.outputValue = self.outputLimitLow

            self.lastUpdateTime = self.millis()

            return self.outputValue
        else:
            return self.outputValue

    def setParams(self, kp, ki, kd):
        sampleTimeInSec = self.updateTime / 1000
        self.kp = kp
        self.ki = ki * sampleTimeInSec
        self.kd = kd * sampleTimeInSec

        if(self.direction == "REVERSE"):
            self.kp = (0 - kp)
            self.ki = (0 - ki)
            self.kd = (0 - kd)

    def setOutputOffset(self, offset):
        self.offset = offset
    
    def setOutputLimits(self, low, high):
        self.outputLimitLow = low
        self.outputLimitHigh = high

    def setUpdateTime(self, updateTime):
        self.updateTime = updateTime
    
    
    def reset(self):
        pass
