'''
Created on Jan 3, 2016
@author: graysonelias
'''

import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 0
RMOTOR = 3
ARMMOTOR = 1

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)

# Servos
servoClaw = 0
servoArm = 3
servoGrabber = 1

#Servo values for hay stacking arm
armUpPom = 390
armUp = 1700
armCube = 1050#1400
armUnderHandle = 700
armJustOffTheGround = 400 #550
armDown = 500
armDownFurrow= 1000

#Values for hay claw
clawClose = 600
clawMid = 900
clawOpen = 1900 #1400
clawHayGrab = 1500

#Servo values for pom grabber
grabberOpen = 750
grabberClose = 1640
grabberStraight = 1380

#Tophat values
FRONT_TOPHAT = 0
frontLineFollowerGrey = 1300
LINE_FOLLOW_TOPHAT = 5


if isClone:
 # Servos
    servoClaw = 0
    servoArm = 3
    servoGrabber = 1

    armUpPom = 640#390
    armUp = 2000#1700
    armCube = 1100#950#1400
    armJustOffTheGround = 500#400
    armDown = 420#500
    armDownFurrow = 1000

    grabberWide = 0
    grabberOpen = 1500
    grabberClose = 2047

    clawClose = 850
    clawMid = 1350
    clawOpen = 1900
    clawHayGrab = 1500



    #Tophat values
    FRONT_TOPHAT = 0
    frontLineFollowerGrey = 1300