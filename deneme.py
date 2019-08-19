from settings import generalSettings
import RPi.GPIO as GPIO
import engine
import sensors
import time
import threading



def main():
    GPIO.setmode(GPIO.BCM)

    engines = engine.robotEngines(generalSettings.motor1pins[0], generalSettings.motor1pins[1], generalSettings.motor2pins[0], generalSettings.motor2pins[1], generalSettings.PWMpins[0], generalSettings.PWMpins[1])
    
    while True:
      engines.goForward()



if __name__ == "__main__":
    main()