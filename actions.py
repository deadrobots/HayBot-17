from wallaby import *
import constants as c
from movement import *
from utils import *

def init():
    set_servo_position(c.portClaw, c.clawOpen)
    set_servo_position(c.portArm, c.armUp)
    enable_servos()
    camera_open()
    camera_update()
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

def goToBackWall():
    print "test"
    driveTimed(60, 50, 1000)
    print "test2"
    driveTimed(400, 382, 5400)
    driveTimed(60, 55, 3000)

def turnToHay():
    driveTimed(-150, -150, 500)
    yellow=0
    lookingforyellow = True
    driveTimed(-55, 60, 3000)
    while (lookingforyellow):
        camera_update()
        if get_object_count(yellow) > 0:
            area = get_object_area(yellow, 0)
            x = get_object_center(yellow, 0).x
            y = get_object_center(yellow, 0).y
            if (get_object_area(yellow, 0) > 1600 and get_object_area(yellow, 0) < 4000):
                print "Hay Bale " + str(area)
                lookingforyellow = False
                driveTimed(-60, -55, 1000)
            else:
                print  "Too small"
        else:
            print "No hay bale"
def grabFirstHayBale():
    driveTimed(100, 0, 300)
    driveTimed(100, 100, 400)
    move_servo_timed(c.portArm, c.armBlock, 2000)
    msleep(300)
    move_servo_timed(c.portClaw, c.clawWide, 2000)
    msleep(300)
    move_servo_timed(c.portArm, c.armHigh, 500)
    msleep(300)
    driveTimed(-100, -110, 400)
    move_servo_timed(c.portArm, c.armGrab, 500)
    msleep(300)
    driveTimed(60, 65, 400)
    move_servo_timed(c.portClaw, c.clawClose, 500)
    msleep(300)
    move_servo_timed(c.portArm, c.armUp,500)
    msleep(3000)




def waitForButton():
    while not digital(13):
        pass