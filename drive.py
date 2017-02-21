#!/usr/bin/python
from wallaby import *

def driveTimed(left, right, time):
    motor(0, left)
    motor(3, right)
    msleep(time)

def sleep(time):

    driveTimed(0, 0, time)

def drive(left, right):
    motor(0,left)
    motor(3,right)