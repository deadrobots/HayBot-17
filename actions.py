import motorsPlusPlus as x
import utils as u
import constants as c
from wallaby import *

headToHead = True


def grayson():
    x.drive_speed_arm_up(45, 100)
    exit(0)


def position():
    x.drive_speed(4, 50)
    x.pivot_left(30, 25)
    x.drive_speed(3, 50)


def init():
    x.armDown()
    if c.isClone:
        print ('I am Clone')
    else:
        print ('I am Prime')
    print ('Testing servos and motors')

    set_servo_position(c.servoGrabber, c.grabberOpen)
    set_servo_position(c.servoClaw, c.clawOpen)
    selfTest()
    print('Put me at back wall and press button')
    set_servo_position(c.servoClaw, c.clawOpen)
    u.wait4light()
    shut_down_in(119.9)
    c.startTime = seconds()


def getFirstHay():
    x.drive_speed(10, 50)
    u.move_servo(c.servoClaw, c.clawClose, 70)
    u.move_servo(c.servoGrabber, c.grabberClose, 50)  # 30
    x.armUp()
    u.move_servo(c.servoArm, c.armUp, 100)
    msleep(7000)


def goToFarWall2():
    x.drive_speed(-2,50)
    if c.isClone:
        x.pivot_left(72, 50)
    else:
        x.pivot_left(72, 50)
    x.drive_speed_arm_up(60, 100)
    if c.isClone:
        x.rotate(-87,50)
    else:
        x.rotate(-90, 50)
    x._drive(70, 70)
    while (analog(c.LINE_FOLLOW_TOPHAT) < 1500):
        pass
    x._drive(0, 0)
    if c.isClone:
        x.drive_speed(19,100)
    else:
        x.drive_speed(15,100)
    if c.isClone:
        msleep(8300)
    else:
        msleep(8000)
    x.drive_speed(-25,100)
    x.rotate(93,50) # 90
    if c.isClone:
        x.drive_speed(29, 100)
    else:
        x.drive_speed(25,100)
    x.pivot_right(6, 50)
    '''x.drive_condition(1, 30, seeLine)

    #x.pivot_left(40,-50)

#    x.pivot_right(40, 50)

    u.setWait(4)
    while u.getWait():
        if analog(c.LINE_FOLLOW_TOPHAT) > 1500:
            x._drive(80, 50)
        else:
            x._drive(50, 80)

    while dontSeeWall():
        if analog(c.LINE_FOLLOW_TOPHAT) > 1500:
            x._drive(80, 50)
        else:
            x._drive(50, 80)


    x.rotate(-10,40)
    x.drive_speed(17, 75)
    x.pivot_left(6, 50)
    u.waitForButton()
'''

def dontSeeWall():
    return analog(c.ET) < 1000


def seeHay():
    xx = analog(c.ET)
    print "ET: " + str(xx)
    return xx < 2200


def seeLine():
    return analog(c.LINE_FOLLOW_TOPHAT) < 1500


def turnToHay():
    '''x.drive_speed(12, -70)
    x.pivot_right(99, 50)
    x.drive_speed(23,80)
    x.rotate(-90,50)
    x.drive_speed(14,80)'''
    x.pivot_right(6, 50)
    x.drive_speed(-5,70)
    if c.isClone:
        x.rotate(90,40)
    else:
        x.rotate(94,40)
    # x.drive_speed(3,-40) # odd backup
    print "Before: " + str(analog(0))
    print "Before: " + str(analog(0))
    if c.isClone:
        x.drive_condition(50, 50, seeHay)
    else:
        x.drive_condition(50, 50, seeHay)
    center()
    x.drive_speed(-1.5, 75)
    print "After: " + str(analog(0))
    msleep(500)


def stackHay():
    u.move_servo(c.servoArm, c.armCube, 10)  # 35
    #msleep(100)
    # u.move_servo(c.servoClaw, c.clawMid, 60)  # 30
    # msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 30)  # 50
    #msleep(100)
    x.drive_speed(0.25, -75)  # (0.75, -50)
    #msleep(100)
    x.rotate(3, 15)
    #msleep(100)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)  # 40
    #msleep(100)
    x.rotate(3, -15)
    #msleep(100)
    x.drive_speed(2.11, 80)  # 60
    u.move_servo(c.servoClaw, c.clawClose, 30)  # 50
    #msleep(100)
    x.drive_speed(2.7, -100)  # -75300
    u.move_servo(c.servoArm, c.armUp, 30)  # 50



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



# def turnToSecondHay():
#     x.pivot_right(-110, 50)
#     if c.isClone:
#         x.drive_speed(1, -100)
#         x.pivot_left(-110, 50)
#     else:
#         x.drive_speed(.1, -100)  # -75
#         x.pivot_left(-115, 50)
#     x.drive_condition(100, 100, seeHay)
#     center()
#     if c.isClone:
#         x.drive_speed(-2.4, 75)  # 50
#     else:
#         x.drive_speed(-1.5, 75)
#     msleep(500)

def GoToSecondHay():
    x.drive_speed(3,-80)
    x.rotate(-88.5,50)
    x.drive_speed(10,70)
    x.pivot_right(6, 50)
    x.drive_speed(-12,70)
    x.rotate(93,50)
    x.drive_condition(50, 50, seeHay)
    center()
    if c.isClone:
        x.drive_speed(-2.4, 75)  # 50
    else:
        x.drive_speed(-1.5, 75)
    msleep(500)


def stackSecondHay():
    u.move_servo(c.servoArm, c.armCube, 10)  # 35
    msleep(100)
    u.move_servo(c.servoClaw, c.clawMid, 30)  # 50
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 30)  # 50
    msleep(100)
    x.drive_speed(-0.5, 75)  # -25
    msleep(100)
    x.rotate(3, 5)
    msleep(100)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)  # 40
    msleep(100)
    x.rotate(3, -5)
    msleep(100)
    x.drive_speed(2.11, 80)  # 60
    u.move_servo(c.servoClaw, c.clawClose, 30)  # 50
    msleep(100)
    x.drive_speed(2.7, -100)  # -50
    if c.isClone:
        u.move_servo(c.servoArm, c.armUp, 15)  # 50
    else:
        u.move_servo(c.servoArm, c.armUp, 30)  # 50


def square_up_and_drop():
    x.drive_speed(15, 75)

def deliverPoms():
    x.drive_speed(-.5, 50)
    x.armDown()
    msleep(100)
    # x.drop_poms()
    u.move_servo(c.servoGrabber, c.grabberPomDrop, 15)
    msleep(500)
    x.armUp()
    x.drive_speed(3,30)


# def turnToThirdHay():
#     x.drive_speed(-9, 75)
#     x.pivot_right(-110, 50)
#     if c.isClone:
#         x.drive_speed(.75, -100)
#     else:
#         x.drive_speed(.5, -100)  # -75
#     if c.isClone:
#         x.pivot_left(-116, 50)
#     else:
#         x.pivot_left(-112, 50)
#     x.drive_condition(100, 100, seeHay)
#     center()
#     x.drive_speed(-2.4, 75)  # 50
#     msleep(500)

def goToThirdHay():
    x.drive_speed(-13,100)
    x.rotate(-89.5,50)
    x.drive_speed(14,60)
    x.pivot_right(6,50)
    x.drive_speed(-18,70)
    x.rotate(96,50)
    x.drive_speed(-2,50)
    x.drive_condition(38, 38, seeHay)
    center()
    if c.isClone:
        x.drive_speed(-2.4, 75)
    else:
        x.drive_speed(-1.5, 75)
    msleep(500)


def stackThirdHay():
    u.move_servo(c.servoArm, c.armCube, 10)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawMid, 30)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 30)
    msleep(100)
    x.drive_speed(-0.5, 75)
    msleep(100)
    x.rotate(3, 5)
    msleep(100)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)
    msleep(100)
    x.rotate(3, -5)
    msleep(100)
    x.drive_speed(2.11, 80)
    u.move_servo(c.servoClaw, c.clawClose, 30)
    msleep(100)
    x.drive_speed(2.7, -100)
    if c.isClone:
        u.move_servo(c.servoArm, c.armUp, 15)
    else:
        u.move_servo(c.servoArm, c.armUp, 30)


def hayToBarn():
    x.rotate(180, 30)
    x.drive_condition(100, 100, seeLine)
    x.drive_speed(4, 100)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 20)
    u.move_servo(c.servoClaw, c.clawEnd, 10)
    '''
    x.rotate(-84,50)
    x.drive_speed(1,50)
    u.move_servo(c.servoArm, c.armJustOffTheGround, 10)
    msleep(250)
    u.move_servo(c.servoClaw,c.clawEnd,10)
    
    if c.isClone:
        x.rotate(3, 5)
    else:
        x.rotate(7, 5)
    x.drive_speed(5, -90)
    u.move_servo(c.servoArm, c.armDownFurrow, 10)
    x.drive_speed(7, -100)
    '''

def goToBin():
    x.rotate(-90,50)
    x.drive_speed(28,75)
    x.rotate(90,50)
    u.move_servo(c.servoArm,c.armJustOffTheGround)
    x.armDown()
    u.move_servo(c.servoGrabber,c.grabberBinApproach)
    x.drive_speed(8,50)
    u.waitForButton()
    u.move_servo(c.servoGrabber,c.grabberBinTake)
    x.drive_speed(-10,30)
    x.armUp()


# TEST FUNCTIONS!


def test1():
    x.drive_speed(50,100)
    exit(0)

def test():
    print('testing')
    motor_power(c.ARMMOTOR, 44)
    msleep(3500)
    u.DEBUGwithWait()


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
    x.pivot_right(10, 30)
    msleep(1000)
    u.move_servo(c.servoArm, c.armDown, 40)
    msleep(300)
    x.drive_speed(1.5, 40)
    u.move_servo(c.servoClaw, c.clawClose, 50)
    msleep(300)
    u.move_servo(c.servoArm, c.armUp, 50)
    msleep(1500)


def pomGrabberTest():
    enable_servos()
    x.armUp()
    msleep(3000)
    u.move_servo(c.servoGrabber, c.grabberClose, 50)
    msleep(1000)
    u.move_servo(c.servoGrabber, c.grabberWide, 50)
    x.armDown()
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
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 50)
    x.armUp()
    u.move_servo(c.servoGrabber, c.grabberClose, 50)
    msleep(100)
    u.move_servo(c.servoGrabber, c.grabberWide, 50)
    u.move_servo(c.servoGrabber,c.grabberClose,50)
    u.move_servo(c.servoGrabber, c.grabberWide, 50)
    while seeHay():
        pass
    x.drive_condition(100, 100, seeLine)
    x.rotate(20, 75)
    msleep(100)
    x.rotate (-20, 75)
    u.move_servo(c.servoArm, c.armDown, 50)
    x.armDown()






def testCode():
    set_servo_position(c.servoArm, c.armUp) #TEMPORARY
    x.drive_speed(50, 100)
    u.move_servo(c.servoGrabber, c.grabberClose, 20)
    u.DEBUGwithWait()


print "Seconds elapsed: " + str(seconds() - c.startTime)
