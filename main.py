#!/usr/bin/python
import os, sys
from wallaby import *


def main():
    print "Hello World"
    print "we've successfully updated via pycharm"
    create_connect()
    create_full()
    camera_open()
    camera_update()
    drive (100,100,15000)
    drive (-70,70,2500)
    drive (100,100,1000)
    yellow = 0
    lookingForYellow = True
    while (lookingForYellow):
        camera_update()
        if (get_object_count(yellow) > 0):
            if (get_object_area(yellow, 0) > 1000):
                area = get_object_area(yellow, 0)
                x = get_object_center(yellow, 0).x;
                y = get_object_center(yellow, 0).y;
                print "Hay bale " + str(area)
                lookingForYellow = False
            else:
                print "Too small"
                drive(-100, 100, 100)
        else:
            print "No hay bale"
            drive(-100, 100, 100)

    print "All done!"
    # while get_create_lbump() == 0:
    # drive (100,100,100)
    # drive(-100, -100, 3000)create
    # while :
    # drive(-100, 100, 1750)
        camera_update()


def drive(left, right, time):
    """

    :rtype: object
    """
    create_drive_direct(left, right)
    msleep(time)
    create_drive_direct(0, 0)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();

