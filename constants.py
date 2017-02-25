'''
Created on Jan 3, 2016
@author: graysonelias
'''

import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)


# Servos
servoClaw = 0
servoArm = 3


armUp = 1500
armCube = 1200
armDown = 500

clawClose = 600
clawMid = 1200
clawOpen = 1900

#Tophat values
FRONT_TOPHAT = 0
frontLineFollowerGrey = 1300