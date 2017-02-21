from wallaby import *
import constants as c
from movement import *

def init():
    set_servo_position(c.portClaw, c.clawOpen)
    set_servo_position(c.portArm, c.armUp)
    enable_servos()
    create_disconnect()
    if not create_connect_once():
        print "Create not connected..."
        exit(0)

def shutdown():
    create_safe()
    create_disconnect()
    print "DONE"

def grabHay():
    set_servo_position(c.portArm, c.armUp)
    msleep(300)
    set_servo_position(c.portClaw, c.clawOpen)
    msleep(300)
    set_servo_position(c.portArm, c.armDown)
    msleep(300)
    set_servo_position(c.portClaw, c.clawClose)
    msleep(300)
    set_servo_position(c.portArm, c.armUp)
    msleep(300)
    create_drive_direct(100,100)
    msleep(1000)

def goToBackWall():
    print "test"
    driveTimed(60, 50, 1000)
    print "test2"
    driveTimed(400, 382, 5400)
    driveTimed(60, 55, 3000)

def turnToHay():
    driveTimed(-300, -300, 500)

def waitForButton():
    while not digital(13):
        pass