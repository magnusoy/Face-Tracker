
import time

class PID():

    def __init__(self, kp, ki, kd, direction):
        self.direction = direction
        self.setParams(kp, ki, kd)
        self.outputLast = 0.0
        self.outputSum = 0.0
        self.error = 0.0
        self.outputLimitLow = 0.0
        self.outputLimitHigh = 0.0
        self.lastUpdateTime = self.millis()

    
    @classmethod
    def millis(self):
        return int(round(time.time() * 1000))


    def compute(self, actual, target):
        lastError = self.error
        self.error = target - actual
        output = self.error * self.kp
        self.outputSum += error * self.ki
        self.outputLast = (lastError - error) * self.kd
        outputValue = self.offset + output + outputSum + outputLast
        if outputValue > self.outputLimitHigh:
            outputValue = self.outputLimitHigh
        if outputValue < self.outputLimitLow:
            outputValue = self.outputLimitLow

        self.lastUpdateTime = self.millis()

        return outputValue

    def setParams(self, kp, ki, kd):
        sampleTimeInSec = self.sampleTime / 1000
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