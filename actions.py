import motorsPlusPlus as x
import utils as u
import constants as c
from wallaby import enable_servos, msleep, seconds

headToHead = True

def test():
    print('testing')
    u.move_servo_timed(c.servoArm, c.armUp, 10)
    x.drive_speed(24,50)
    msleep(300)
    # x.rotate(90, 25)
    # from wallaby import *
    # motor(c.LMOTOR,50)
    # motor(c.RMOTOR,0)
    # msleep(5000)

def stackHayTest():
    enable_servos()
    u.move_servo(c.servoArm, c.armDown, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    msleep(1500)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 50)
    msleep(3000)
    u.move_servo(c.servoArm, c.armCube, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    msleep(300)
    x.pivot_right(10,30)
    msleep(1000)
    u.move_servo(c.servoArm, c.armDown, 40)
    msleep(300)
    x.drive_speed(1.5,40)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 50)
    msleep(1500)
    #
    # u.move_servo(c.servoArm, c.armCube, 50)
    # msleep(300)
    # u.move_servo(c.servoClaw, c.clawMid, 50)
    # msleep(300)
    # u.move_servo(c.servoClaw, c.clawOpen, 50)
    # msleep(300)
    # u.move_servo(c.servoArm, c.armDown, 40)
    # msleep(300)
    # x.drive_speed(1.5,40)
    # u.move_servo(c.servoClaw, c.clawClose, 50)
    # msleep(300)
    # u.move_servo(c.servoArm, c.armUp, 50)
    # msleep(2000)

def init():
    enable_servos()
    u.move_servo(c.servoClaw, c.clawOpen, 100)
    u.move_servo(c.servoArm, c.armDown, 100)
    msleep(300)
    u.waitForButton()
    c.startTime = seconds()

def getFirstHay():
    x.drive_speed(1.5, 50)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 50)
    msleep(300)

def goToFarWall():
    x.drive_speed(3, 50)
    x.pivot_left(90, 50)
    x.drive_speed(87, 100)

def turnToHay():
    x.drive_speed(4, -50)
    x.rotate(90, 50)
    x.drive_speed(4, 50)
    msleep(500)

def stackHay():
    u.move_servo(c.servoArm, c.armCube, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    msleep(300)

    print "Seconds elapsed: " + str(seconds() - c.startTime)