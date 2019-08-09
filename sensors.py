#!/usr/bin/python
from settings import generalSettings
import gpiozero
import time

class Sensor():
    def __init__(self):
        pass
    

class distanceSensor(Sensor):
    def __init__(self):
        super.__init__()

    @staticmethod
    def getDistance():
        try:
            PIN_TRIGGER = generalSettings.distanceSensorPin_TRIGGER
            PIN_ECHO = generalSettings.distanceSensorPin_ECHO

            sensorOutput = gpiozero.OutputDevice(PIN_TRIGGER, active_high=True, initial_value=False)
            sensorInput = gpiozero.InputDevice(PIN_ECHO)

            sensorOutput.on()

            time.sleep(0.00001)

            sensorOutput.off()

            global pulse_start_time
            global pulse_end_time
            while not sensorInput.is_active:
                pulse_start_time = time.time()
            while sensorInput.is_active:
                pulse_end_time = time.time()
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            return distance
        finally:
            pass

class infraredSensor(Sensor):
    def __init__(self):
        super.__init__()

    # from left to right
    @staticmethod
    def getSensor1():
        sensorInput = gpiozero.InputDevice(generalSettings.infraredSensorPins[0])
        return sensorInput.is_active
    
    @staticmethod
    def getSensor2():
        sensorInput = gpiozero.InputDevice(generalSettings.infraredSensorPins[1])
        return sensorInput.is_active
        
    @staticmethod
    def getSensor3():
        sensorInput = gpiozero.InputDevice(generalSettings.infraredSensorPins[2])
        return sensorInput.is_active

    @staticmethod
    def getSensor4():
        sensorInput = gpiozero.InputDevice(generalSettings.infraredSensorPins[3])
        return sensorInput.is_active

    @staticmethod
    def getSensor5():
        sensorInput = gpiozero.InputDevice(generalSettings.infraredSensorPins[4])
        return sensorInput.is_active

    @staticmethod
    def getAllSensors():
        return (infraredSensor.getSensor1(), infraredSensor.getSensor2(), infraredSensor.getSensor3(), infraredSensor.getSensor4(), infraredSensor.getSensor5())
