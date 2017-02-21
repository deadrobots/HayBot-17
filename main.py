#!/usr/bin/python
import os, sys
from wallaby import *


def main():
    enable_servos()
    set_servo_position()

    create_disconnect()
    print "Hello my dear Create"
    print "Turn on the create you moron"
    create_connect()
    create_full()
    enable_servos()
    driveTimed(0, 0, 100)
    set_servo_position(3, 300)
    camera_open()
    camera_update()
    yellow = 0
    lookingforyellow = False
    # Drive back to opposite wall.
    # driveTimed(60,55, 1000)
    # driveTimed(100, 96, 1000)
    # driveTimed(200, 192, 1000)
    # driveTimed(300, 286, 1000)
    driveTimed(60, 50, 1000)
    driveTimed(400, 382, 5400)
    driveTimed(60, 55,3000)
    '''
    driveTimed(0,0,1000)
    driveTimed(-60,-55,1000)
    lookingforyellow = True
    driveTimed(60,-55,3000)
    while(lookingforyellow):
        camera_update()
        if get_object_count(yellow) > 0:
            area = get_object_area(yellow,0)
            x = get_object_center(yellow, 0).x
            y = get_object_center(yellow, 0).y
            if (get_object_area(yellow,0) > 1600 and get_object_area(yellow,0) < 4000):
                print "Hay Bale " + str(area)
                lookingforyellow = False
                driveTimed(-60,-55,1000)
            else:
                print  "Too small"
        else:
            print "No hay bale"
    driveTimed(0,0,500)
    driveTimed(-100,90,2000)
    driveTimed(50,50,2000)

    driveTimed(0,0,500)
    driveTimed(-60, -55, 2500)
    lookingforyellow = True
    driveTimed(60, -55, 2500)
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
'''

    #Deposits hay bale from grazing area into barn.

    #driveTimed(-53,-60,400)
    #driveTimed(50,-50,3000)
    #driveTimed(-55, -60, 2900)
    #driveTimed(0, 0, 2000) commented out 4 lines above
    #driveTimed(-50,50,1500)
    #driveTimed(75,75,500)
    # driveTimed(-55,-60,500)
    #driveTimed(-50,50,3000)
    #driveTimed(-96, -100, 3500)
    #driveTimed(0, 0, 2000)
    #driveTimed(50,-50,3000)




    # driveTimed(50,-50, 3200)
    # driveTimed(60,55, 400)
    #
    # driveTimed(50,-50,3200)

    # driveTimedStraight(400,4000)
    # Squares up with wall
    # driveTimed(-70,-70,3000)
    # driveTimed(70,70,700)
    # driveTimed(70,-70,2000)
    # driveTimed(100,100,1000)
    # yellow = 0
    # lookingForYellow = True
    # #Code to find the farthest hay bale and line up over it
    # while (lookingForYellow):
    #     camera_update()
    #     if get_object_count(yellow) > 0:
    #         area = get_object_area(yellow, 0)
    #         x = get_object_center(yellow, 0).x;
    #         y = get_object_center(yellow, 0).y;
    #         if (get_object_area(yellow, 0) > 1600):
    #             print "Hay bale " + str(area)
    #             lookingForYellow = False
    #         else:
    #             print "Too small"
    #             if (x>get_camera_width()/2):
    #                 create_drive_direct(40, 20)
    #             elif(x<get_camera_width()/2):
    #                 create_drive_direct(20, 40)
    #             else:
    #                 create_drive_direct(30, 30)
    #     else:
    #         print "No hay bale"
    #         driveTimed(-100, 100, 100)

    disable_servos()
    print "All done!"
    # while get_create_lbump() == 0:
    # drivTimede (100,100,100)
    # drive(-100, -100, 3000)create
    # while :
    # drive(-100, 100, 1750)
    create_safe()
    create_disconnect()


def driveTimed(left, right, time):
    """
create_drive_direct(left, right)
    :rtype: object
    """
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def driveTimedStraight(power, time):
    """
create_drive_straight(power)
    :rtype: object
    """
    create_drive_straight(power)
    msleep(time)
    create_drive_straight(0)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();