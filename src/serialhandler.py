# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
from time import sleep


class SerialCommunication(object):
    """
    Serialconnection handler.
    """

    def __init__(self, port, baudrate=9600):
        """
        Establishes a connection to the given port.
        @port : where your device is connected
        @baudrate : the specified connection speed
                    (9600, 19200, 28800, 57600, 115200)
        """

        self.port = port
        self.baudrate = baudrate
        try:
            self.connection = serial.Serial(port, baudrate)
            sleep(2)
        except serial.SerialException as se:
            self.connection = None

    def isConnected(self):
        """
        Checks if the connection is established.
        @return False if not connected
                else True
        """

        result = False
        if self.connection is not None:
            result = True
        return result

    def readInputStream(self):
        """
        Read data sent trough Serial.
        @return decoded message
        """

        raw = self.connection.readline()
        data = raw.decode('latin-1')
        return data.rstrip('\n')

    def sendOutputStream(self, data):
        """
        Send data trough Serial.
        """
        addEndmarker = data + '\n'
        self.connection.write(addEndmarker.encode())

    def disconnect(self):
        """
        Disconnect the connection
        @return True if sucsessfully disconnected
        """

        self.connection.close()
        return True


# Example of usage
if __name__ == "__main__":
    arduino = SerialCommunication("COM3", 115200)

    while(arduino.isConnected()):
        print(arduino.readInputStream())
