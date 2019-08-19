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

        GPIO.output(PIN_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, False)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(PIN_ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance


class infraredSensor(Sensor):
    def __init__(self):
        super.__init__()

    # from left to right
    @staticmethod
    def getSensor(SensorNumber):
        sensorInput =  GPIO.setup(generalSettings.infraredSensorPins[SensorNumber],GPIO.IN)
        isActive= True
        if GPIO.input(generalSettings.infraredSensorPins[SensorNumber]) == 0:
            isActive = False
        return isActive

    @staticmethod
    def getAllSensors():
        return (infraredSensor.getSensor(0), infraredSensor.getSensor(1), infraredSensor.getSensor(2), infraredSensor.getSensor(3), infraredSensor.getSensor(4))
