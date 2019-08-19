import RPi.GPIO as GPIO
import time

class robotEngines():
    def __init__(self, motor1pin1, motor1pin2, motor2pin1, motor2pin2, PWMpin1, PWMpin2):
        self.motor1pin1 = motor1pin1
        self.motor1pin2 = motor1pin2
        self.motor2pin1 = motor2pin1
        self.motor2pin2 = motor2pin2
        self.PWMpin1 = PWMpin1
        self.PWMpin2 = PWMpin2
        GPIO.setup(motor1pin1, GPIO.OUT)
        GPIO.setup(motor1pin2, GPIO.OUT)
        GPIO.setup(motor2pin1, GPIO.OUT)
        GPIO.setup(motor2pin2, GPIO.OUT)

        GPIO.output(motor1pin1, 0)
        GPIO.output(motor1pin2, 0)
        GPIO.output(motor2pin1, 0)
        GPIO.output(motor2pin2, 0)

        GPIO.setup(PWMpin1, 0)
        GPIO.setup(PWMpin2, 0)

        self.PWMEngines = (GPIO.PWM(PWMpin1, 100), GPIO.PWM(PWMpin2, 100))
        self.initiatePWMEngines()
        self.partialSpeedX(0.6)

    def initiatePWMEngines(self):
        (self.PWMEngines[0]).start(1)
        (self.PWMEngines[1]).start(1)

    def partialSpeed(self, degree):
        (self.PWMEngines[0]).ChangeDutyCycle(degree)
        (self.PWMEngines[1]).ChangeDutyCycle(degree)

    def partialSpeedX(self, degree):

        (self.PWMEngines[0]).ChangeDutyCycle(0.8)
        (self.PWMEngines[1]).ChangeDutyCycle(0.6)

    def goForward(self):

        GPIO.output(self.motor1pin1, 1)
        GPIO.output(self.motor1pin2, 0)

        GPIO.output(self.motor2pin1, 1)
        GPIO.output(self.motor2pin2, 0)

    def goBackwards(self):
        GPIO.output(self.motor1pin1, 0)
        GPIO.output(self.motor1pin2, 1)

        GPIO.output(self.motor2pin1, 0)
        GPIO.output(self.motor2pin2, 1)

    def turnLeft(self):

        GPIO.output(motor1pin1, 0)
        GPIO.output(motor1pin2, 1)

        GPIO.output(motor2pin1, 1)
        GPIO.output(motor2pin2, 0)

    def turnRight(self):
        GPIO.output(motor1pin1, 1)
        GPIO.output(motor1pin2, 0)

        GPIO.output(motor2pin1, 0)
        GPIO.output(motor2pin2, 1)
        
    def turnLeftOneTier(self):
        GPIO.output(motor1pin1, 1)
        GPIO.output(motor1pin2, 0)

        GPIO.output(motor2pin1, 0)
        GPIO.output(motor2pin2, 0)

    def turnRightOneTier(self):

        GPIO.output(motor1pin1, 0)
        GPIO.output(motor1pin2, 0)

        GPIO.output(motor2pin1, 1)
        GPIO.output(motor2pin2, 0)
        
    def stop(self):

        GPIO.output(motor1pin1, 0)
        GPIO.output(motor1pin2, 0)

        GPIO.output(motor2pin1, 0)
        GPIO.output(motor2pin2, 0)

    def partialSpeedY(self, degreeL, degreeR):
        self.PWMEngines[0].value = degreeL
        self.PWMEngines[1].value = degreeR

    def MoveForwardWithParameters(SpeedL, SpeedR, sleeptime):
        partialSpeedY(degreeL, degreeR)
        goForward()
        time.sleep(sleeptime)
        partialSpeedY(1,1)

