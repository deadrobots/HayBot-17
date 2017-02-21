#!/usr/bin/python
from wallaby import *
from drive import *
from servos import *
from sensors import *

def goToBot():
    driveTimed(100, 98, 3000)
    sleep(1000)
    driveTimed(-50, 50, 670)
    sleep(1000)
    moveServo(0, 1750, 5)#Servo Position OPEN
    sleep(1000)

def grabBotGuy():
    moveServo(2, 1277, 15)#Servo Position MIDDLE
    sleep(1000)
    driveTimed(50, 50, 3500)
    sleep(1000)
    moveServo(0, 1200, 5)#Servo Position CLOSED
    sleep(1000)

def turnToCow():
    moveServo(2,1150,5)#Servo Position MIDDLE-UP
    sleep(1000)
    driveTimed(-70,-70,1700)


    sleep(1000)
    driveTimed(-50,50, 850)
    sleep(1000)
    driveTimed(-70, -70, 2000)

def goToBin():
    sleep(1000)
    driveTimed(100,96,4000)
    sleep(1000)
    driveTimed(-66,66,520)

def grabBin():
    sleep(1000)
    moveServo(2, 470,5)
    sleep(1000)
    driveTimed(-60, -60, 1700)
    sleep(1000)
    moveServo(2, 850,5)
    sleep(1000)

def goToHopper():
    driveTimed(50, 50, 1400)
    driveTimed(45, 100, 1500)
    driveTimed(70, 1070, 2000)
def cowSpot():
    lookForCow()

def startup():
    enable_servos()
    set_servo_position(2,500)
    msleep(100)
    moveServo(2,1300,5)
