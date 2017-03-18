import motorsPlusPlus as x
import utils as u
import constants as c
from wallaby import *

headToHead = True

def test():
    print('testing')
    motor_power(c.ARMMOTOR,44)
    msleep(3500)
    u.DEBUGwithWait()

def armUp():
    motor_power(c.ARMMOTOR, 50)
    msleep(3500)
    motor_power(c.ARMMOTOR, 0)

def armDown():
    motor_power(c.ARMMOTOR, -37)
    msleep(3500)
    motor_power(c.ARMMOTOR, 0)


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

def pomGrabberTest():
    enable_servos()
    armUp()
    msleep(3000)
    u.move_servo(c.servoGrabber, c.grabberClose, 50)
    msleep(1000)
    u.move_servo(c.servoGrabber, c.grabberWide, 50)
    armDown()
    msleep(3000)
    ''' x.drive_speed(8, 50)
    u.move_servo(c.servoGrabber, c.grabberClose, 20)
    armUp()
    msleep(3000)
    u.DEBUGwithWait()
'''

def selfTest():
    enable_servos()
    u.move_servo(c.servoArm, c.armUp, 50)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(200)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    armUp()
    u.move_servo(c.servoGrabber, c.grabberClose, 50)
    msleep(1000)
    u.move_servo(c.servoGrabber, c.grabberWide, 50)
    while seeHay():
        pass
    x.drive_condition(100, 100, seeLine)
    x.rotate(-90, 50)
    x.rotate(90, 50)
    u.move_servo(c.servoArm, c.armDown, 50)
    armDown()



def init():
    if c.isClone:
        print ('I am Clone')
    else:
        print ('I am Prime')
    print ('Testing servos and motors')
    selfTest()
    print('Put me at back wall and press button')
    u.waitForButton()
    position()
    u.waitForButton()
    c.startTime = seconds()

def testCode():
    x.drive_speed(10, 50)
    u.move_servo(c.servoGrabber, c.grabberClose, 20)


def position():
    x.drive_speed(4, 50)
    x.pivot_left(30, 25)
    x.drive_speed(3, 50)


def getFirstHay():
    if c.isClone:
        x.drive_speed(10, 50)
        u.move_servo(c.servoClaw, c.clawClose, 70)
    else:
        x.drive_speed(2, 75)#50
        u.move_servo(c.servoClaw, c.clawClose, 70)#50
        x.drive_speed(5, 75)#50
    u.move_servo(c.servoGrabber, c.grabberClose, 50)#30
    u.move_servo(c.servoArm, c.armUp, 100)
    armUp()


    # msleep(300)

def goToFarWall():
    if c.isClone:
        x.pivot_left(70, 50)
    else:
        x.pivot_left(70, 50)
    x.drive_speed(73, 100)
    x.drive_condition(100, 100, seeWall)
    x.drive_speed(14,100)

def goToFarWall2():
    if c.isClone:
        x.pivot_left(70, 50)
    else:
        x.pivot_left(68, 50)
    x.drive_speed(45, 100)
    x.rotate(-35, 50)
    x._drive(60, 60)
    while(analog(c.LINE_FOLLOW_TOPHAT) < 1500):
        pass
    x._drive(0, 0)
    x.pivot_right(40, 50)
    while(seeWall()):
        if (analog(c.LINE_FOLLOW_TOPHAT) < 1500):
            x._drive(80,50)
        else:
            x._drive(50,80)
    x.drive_speed(7, 100)


def seeWall():
    return analog(0) < 1000

def seeHay():
    return analog(0) < 2200

def seeLine():
    return analog(5) < 3000

def turnToHay():
    if c.isClone:
        x.drive_speed(6, -100)
        x.rotate(45, 25)
        x.drive_timed(20, 80, 1.3)
        x.drive_condition(100, 100, seeHay)
        center()
        x.drive_speed(-2.2, 25)
    else:
        x.drive_speed(5, -100)#-75
        x.rotate(90, 50)
        print "Before: " + str(analog(0))
        x.drive_condition(100, 100, seeHay)
        center()
        x.drive_speed(-2.4, 75)#50
    print "After: " + str(analog(0))
    msleep(500)

def stackHay():
    u.move_servo(c.servoArm, c.armCube, 10)#35
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 60)#30
    msleep(300)
    u.move_servo(c.servoClaw, c.clawHayGrab, 60)#30
    msleep(300)
    x.drive_speed(0.75, -75)#-50
    msleep(300)
    x.rotate(3, 5)
    msleep(1000)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)#40
    msleep(300)
    x.rotate(3, -5)
    msleep(300)
    x.drive_speed(2.11, 80)#60
    u.move_servo(c.servoClaw, c.clawClose, 30)#50
    msleep(300)
    x.drive_speed(2.7, -100)#-75300
    u.move_servo(c.servoArm, c.armUp, 30)#50

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
    if c.isClone:
        x.drive_speed(1, -100)
    else:
        x.drive_speed(.5, -100)#-75
    x.pivot_left(-112,50)
    x.drive_condition(100, 100, seeHay)
    center()
    x.drive_speed(-2.4, 75)#50
    msleep(500)

def stackSecondHay():
    u.move_servo(c.servoArm, c.armCube, 10)#35
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 30)#50
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 30)#50
    msleep(300)

    x.drive_speed(0.5, -75)#-25
    msleep(300)
    x.rotate(3, 5)
    msleep(300)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)#40
    msleep(300)
    x.rotate(3, -5)
    msleep(300)
    x.drive_speed(2.11, 80)#60
    u.move_servo(c.servoClaw, c.clawClose, 30)#50
    msleep(300)
    x.drive_speed(2.7, -100)#-50
    if c.isClone:
        u.move_servo(c.servoArm, c.armUp, 15)  # 50
    else:
        u.move_servo(c.servoArm, c.armUp, 30)  # 50

def turnToThirdHay():
    x.pivot_right(-110,50)
    if c.isClone:
        x.drive_speed(.75, -100)
    else:
        x.drive_speed(.5, -100)#-75
    if c.isClone:
        x.pivot_left(-116,50)
    else:
        x.pivot_left(-112, 50)
    x.drive_condition(100, 100, seeHay)
    center()
    x.drive_speed(-2.4, 75)#50
    msleep(500)

def stackThirdHay():
    u.move_servo(c.servoArm, c.armCube, 10)#35
    msleep(300)
    u.move_servo(c.servoClaw, c.clawMid, 30)#50
    msleep(300)
    u.move_servo(c.servoClaw, c.clawOpen, 30)#50
    msleep(300)

    x.drive_speed(0.5, -75)#-25
    msleep(300)
    x.rotate(3, 5)
    msleep(300)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)#40
    msleep(300)
    x.rotate(3, -5)
    msleep(300)
    x.drive_speed(2.11, 80)#60
    u.move_servo(c.servoClaw, c.clawClose, 30)#50
    msleep(300)
    x.drive_speed(2.7, -100)#-50
    if c.isClone:
        u.move_servo(c.servoArm, c.armUp, 15)  # 50
    else:
        u.move_servo(c.servoArm, c.armUp, 30)  # 50

def hayToBarn():
    x.rotate(180,30)
    #x.drive_speed(12,100)#60
    x.drive_condition(100,100, seeLine)
    u.move_servo(c.servoArm, c.armCube, 10)
    #x.drive_speed(5, 100)#60
    u.move_servo(c.servoArm, c.armJustOffTheGround,10)
    u.move_servo(c.servoClaw, c.clawOpen,30)
    if  c.isClone:
        x.rotate(3, 5)
    else:
        x.rotate(7,5)
    x.drive_speed(5, -90)#-30
    u.move_servo(c.servoArm, c.armDownFurrow, 10)
    x.drive_speed(10, -100)#-70


def goToFurrow():
    x.rotate(170, 50)
    u.move_servo(c.servoArm, c.armUp, 10)
    x.drive_timed(100,80,4) #(10,50)

def deliverPoms():
    armDown()
    msleep(300)
    motor_power(c.ARMMOTOR, 50)
    msleep(150)
    u.move_servo(c.servoGrabber, c.grabberWide, 10)


'''def putPomsInFurrow():
    u.move_servo(c.servoArm, c.armDownFurrow, 10)
    u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    x.pivot_right(-30, 35)
    u.move_servo(c.servoArm, c.armUp, 10)
    u.move_servo(c.servoGrabber, c.grabberClose, 10)
    u.move_servo(c.servoArm, c.armDownFurrow, 10)
    u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    msleep(300)
    #u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    #x.pivot_right(-40,35)
    u.move_servo_timed(c.servoArm, c.armUp, 10)
    #x.pivot_right(50,35)
    msleep(300)'''

'''def putPomsInFurrow2():
    u.move_servo(c.servoArm, c.armDownFurrow, 10)
    u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    u.move_servo(c.servoGrabber, c.armUp)
    u.move_servo(c.servoGrabber, c.armDownFurrow)
    u.move_servo(c.servoGrabber, c.grabberClose, 10)
    u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    u.move_servo_timed(c.servoGrabber, c.armUp, 10)
    x.pivot_right(-30, 35)
    msleep(300)
    #u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    #x.pivot_right(-40,35)
    u.move_servo_timed(c.servoArm, c.armUp, 10)
    #x.pivot_right(50,35)
    msleep(300)'''

'''def smash():
    u.move_servo(c.servoArm, c.armDownFurrow, 10)
    msleep(100)
    u.move_servo(c.servoGrabber, c.grabberOpen, 10)
    msleep(400)
    u.move_servo(c.servoArm, c.armUp)
    print "hello bela"
    for _ in range(0, 2):
        u.move_servo(c.servoGrabber, c.grabberClose)
        u.move_servo(c.servoArm, c.armDown)
        msleep(100)
        u.move_servo(c.servoGrabber, c.grabberOpen)
        msleep(100)
        u.move_servo(c.servoArm, c.armUp)
        msleep(300)
    u.move_servo(c.servoArm, c.armDown)
    x.pivot_right(-15, 30)
    u.move_servo(c.servoGrabber, c.grabberClose)
    u.move_servo(c.servoGrabber, c.grabberOpen)
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoGrabber, c.grabberClose)
    x.pivot_right(15, 30)'''

def getToRamp():
    x.drive_speed(-15, 100)
    x.rotate(100,50)


def getToCenter():
    x.drive_speed(-10, 50)
    msleep(100)
    x.rotate(90, 50)
    msleep(100)
    x.drive_speed(43, 90)
    msleep(100)
    x.rotate(-90,50)
    u.move_servo(c.servoArm, c.armUp, 10)
    msleep(100)
    x.drive_speed(24, 70)
    x.drive_speed(-7, 50)
    msleep(100)
    x.drive_timed(90, 20, 2.5)
    msleep(100)
    u.move_servo(c.servoArm, c.armUnderHandle)
    x.drive_timed(20, 90, .2)
    x.drive_speed(12, 75)
    u.move_servo(c.servoArm, c.armUp)
    x.drive_timed(25, 90, .3)
    x.drive_speed(14, 75)
    x.drive_speed(-5, 50)
    msleep(100)
    x.rotate(90, 50)

    u.DEBUGwithWait()
    #x.rotate(-100, 50)
    #u.move_servo(c.servoArm, c.armJustOffTheGround, 10)
    #msleep(100)


'''
def getToCenter():


        x.drive_speed(35, 100)
        msleep(100)
        x.rotate(95, 70)
        msleep(100)
        x.drive_speed(-37, 100)
        msleep(100)
        x.rotate(-90, 70)
        msleep(100)
        x.drive_speed(-20, 100)
        msleep(100)
        x.drive_speed(3, 100)
        msleep(100)
        x.rotate(-40, 70)
        u.DEBUGwithWait()
        msleep(100)
        x.drive_timed(-100, -10, 500)
        msleep(100)
'''





print "Seconds elapsed: " + str(seconds() - c.startTime)
