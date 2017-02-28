import motorsPlusPlus as x
import utils as u
import constants as c
from wallaby import enable_servos, msleep, seconds, analog, motor
from wallaby import *

headToHead = True

def test():
    print('testing')
    enable_servos()
    # u.move_servo_timed(c.servoArm, c.armUp, 10)
    # u.waitForButton()
    x.drive_speed(85,100)
    # motor_power(c.LMOTOR, 100)
    # motor_power(c.RMOTOR, 100)
    # msleep(11000)
    u.DEBUG()
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
    # x.drive_speed(87, 100)
    x.drive_condition(100, 100, seeWall)
    x.drive_speed(14,100)

def seeWall():
    return analog(0) < 1000

def seeHay():
    return analog(0) < 2200

def turnToHay():
    x.drive_speed(5, -50)
    x.rotate(90, 50)
    x.drive_condition(100,100,seeHay)
    center()
    x.drive_speed(-2, 50)
    msleep(500)

def stackHay():
    u.move_servo(c.servoArm, c.armCube, 35)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    msleep(300)
    x.drive_speed(1, -50)
    #x.pivot_right(10, 5)
    msleep(1000)
    u.move_servo(c.servoArm, c.armDown, 40)
    msleep(300)
    x.drive_speed(2.11, 40)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(300)
    x.drive_speed(3, -50)
    u.move_servo(c.servoArm, c.armUp, 50)
    # u.move_servo(c.servoArm, c.armCube, 50)
    # msleep(300)
    # u.move_servo(c.servoClaw, c.clawMid, 50)
    # msleep(300)
    # u.move_servo(c.servoClaw, c.clawOpen, 50)
    # msleep(300)

def seeObject():
    print analog(0)
    return analog(0) > 2000

def seeObjectAndWait():
    return not seeObject() and u.getWait()

def center():
    x.drive_condition(25, -25, seeObject)
    u.setWait(1.5)
    x.drive_condition(-25, 25, seeObjectAndWait)
    x.pivot_left(5, -50)

def turnToSecondHay():
    x.pivot_right(-110,50)
    x.drive_speed(.5, -50)
    x.pivot_left(-112,50)
    x.drive_condition(100, 100, seeHay)
    center()
    x.drive_speed(-2, 50)
    msleep(500)

def stackSecondHay():
    # x.drive_speed(6.2, 50)
    # msleep(500)
    u.move_servo(c.servoArm, c.armCube, 35)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 50)
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    msleep(300)

    x.drive_speed(1, -50)
    # x.rotate(5, 50)
    msleep(300)
    u.move_servo(c.servoArm, c.armDown, 40)
    msleep(300)
    x.drive_speed(2.11, 40)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(300)
    x.drive_speed(3, -50)
    u.move_servo(c.servoArm, c.armUp, 50)



    print "Seconds elapsed: " + str(seconds() - c.startTime)
