from settings import generalSettings
import RPi.GPIO as GPIO
import engine
import sensors
import time
import threading

def engineFunc(engines):
    while True:
        command = str(raw_input("# : "))
        if command is str("w"):
            engines.goForward()
        elif command == "s":
            engines.goBackwards()
        elif command == "a":
            engines.turnLeft()
        elif command == "d":
            engines.turnRight()
        elif command == "g":
            engines.turnLeftOneTier()
        elif command == "h":
            engines.turnRightOneTier()
        elif command == "p":
            engines.stop()
        elif command == "a35":
            generalSettings.abortMotorsAndFunctionality = True

        if generalSettings.abortMotorsAndFunctionality:
            break

        time.sleep(1)


def distanceSensorFunc(engines):
    while True:
        distance = sensors.distanceSensor.getDistance()

        if distance < 10:
            engines.stop()
        
        time.sleep(0.05)

        if generalSettings.abortMotorsAndFunctionality:
            break


def autoPilotTurn(engines):

    sensorsStatus = sensors.infraredSensor.getAllSensors()

    # check if on T line
    if sensorsStatus == (False, False, False, False, False) or sensorsStatus == (False, False, False, False, True) or sensorsStatus == (True, False, False, False, False):
        engines.turnRight()
        time.sleep(0.2)
        sensorsStatus = sensors.infraredSensor.getAllSensors()
        while (sensorsStatus != (True, True, False, True, True) and
        sensorsStatus != (True, True, True, False, True) and 
        sensorsStatus != (True, False, True, True, True) and 
        sensorsStatus != (True, False, False, True, True) and 
        sensorsStatus != (True, True, False, False, True) and
        sensorsStatus != (True, False, False, False, True) and
        sensorsStatus != (True, False, True, False, True)):
            time.sleep(0.02)
            sensorsStatus = sensors.infraredSensor.getAllSensors()
            print("#######")
            print("sensor1: ", sensors.infraredSensor.getSensor(0))
            print("sensor2: ", sensors.infraredSensor.getSensor(1))
            print("sensor3: ", sensors.infraredSensor.getSensor(2))
            print("sensor4: ", sensors.infraredSensor.getSensor(3))
            print("sensor5: ", sensors.infraredSensor.getSensor(4))
        engines.stop()
        autoPilot(engines)
    else:
        autoPilot(engines)



# autopilot function
def autoPilot(engines):
    counter = 0
    lastDirection = 0
    while True:
        print("###### : ", counter)
        print("sensor1: ", sensors.infraredSensor.getSensor(0))
        print("sensor2: ", sensors.infraredSensor.getSensor(1))
        print("sensor3: ", sensors.infraredSensor.getSensor(2))
        print("sensor4: ", sensors.infraredSensor.getSensor(3))
        print("sensor5: ", sensors.infraredSensor.getSensor(4))

        if generalSettings.abortMotorsAndFunctionality:
            break
        counter = counter + 1

        sensorsStatus = sensors.infraredSensor.getAllSensors()

        if sensorsStatus == (True, True, True, True, True):
            engines.stop()
        elif sensorsStatus == (True, True, False, True, True):
            engines.goForward()
        elif sensorsStatus == (True, False, False, True, True):
            engines.turnLeftOneTier()
        elif sensorsStatus == (True, True, False, False, True):
            engines.turnRightOneTier()
        elif sensorsStatus == (True, False, False, False, True):
            engines.goForward()
        elif sensorsStatus == (False, True, False, True, True):
            engines.turnLeftOneTier()
        elif sensorsStatus == (True, True, False, True, False):
            engines.turnRightOneTier()
        elif sensorsStatus == (False, False, False, True, True):
            engines.turnLeftOneTier()
        elif sensorsStatus == (True, True, False, False, False):
            engines.turnRightOneTier()
        elif sensorsStatus == (False, True, False, True, False):
            engines.goForward()
        elif sensorsStatus == (False, True, True, True, True):
            engines.turnLeft()
        elif sensorsStatus == (True, True, True, True, False):
            engines.turnRight()
        elif sensorsStatus == (False, False, True, True, True):
            engines.turnLeft()
        elif sensorsStatus == (True, True, True, False, False):
            engines.turnRight()
        elif sensorsStatus == (True, False, True, True, True):
            engines.turnRightOneTier()
        elif sensorsStatus == (True, True, True, False, True):
            engines.turnLeftOneTier()
        # T line
        elif sensorsStatus == (False, False, False, False, False):
            autoPilotTurn(engines)
        elif sensorsStatus == (False, False, False, False, True):
            autoPilotTurn(engines)
        elif sensorsStatus == (True, False, False, False, False):
            autoPilotTurn(engines)
        # T line ends
        else:
            engines.goForward()
        
        if generalSettings.abortMotorsAndFunctionality:
            break

        time.sleep(0.07)
        

def main():

    GPIO.setmode(GPIO.BCM)

    engines = engine.robotEngines(generalSettings.motor1pins[0], generalSettings.motor1pins[1], generalSettings.motor2pins[0], generalSettings.motor2pins[1], generalSettings.PWMpins[0], generalSettings.PWMpins[1])

    autoPilotThread = threading.Thread(target=autoPilot, args=(engines,))
    autoPilotThread.start()

    distanceSensorThread = threading.Thread(target=distanceSensorFunc, args=(engines,))
    distanceSensorThread.start()

    controlPanelThread = threading.Thread(target=engineFunc, args=(engines,))
    controlPanelThread.start()

    autoPilotThread.join()
    distanceSensorThread.join()
    controlPanelThread.join()

    
if __name__ == "__main__":
    main()
