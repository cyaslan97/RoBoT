#!/usr/bin/python
from settings import generalSettings
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Sensor():
    def __init__(self):
        pass
    

class distanceSensor(Sensor):
    def __init__(self):
        super.__init__()

    @staticmethod
    def getDistance():
        PIN_TRIGGER = generalSettings.distanceSensorPin_TRIGGER
        PIN_ECHO = generalSettings.distanceSensorPin_ECHO
        GPIO.setup(PIN_TRIGGER,GPIO.OUT)
        GPIO.setup(PIN_ECHO,GPIO.IN)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)


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
