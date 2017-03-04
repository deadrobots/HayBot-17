#!/usr/bin/python
from wallaby import *
from drive import *

def lookForCow():
    camera_open()
    blobSize = 0
    while(blobSize < 6600):
        camera_update()
        # print get_object_area(0,0)
        # print get_object_count(0)
        blobSize = get_object_area(0,0)
        if(get_object_count(0)>0 and get_object_area(0,0)>200):
            print "I see a cow"
            print get_object_area(0,0)
            if(get_object_center(0,0).x > get_camera_width()/2):
                print "Moving Right"
                driveTimed(-30,-40,5)
            elif(get_object_center(0,0).x > get_camera_width()/2):
                print "moving left"
                driveTimed(-40,-30,5)
            else:
                print "Moving Dumb"
                driveTimed(-45,-35,5)
        else:
            # print "this is for grayson " + str(get_object_area(0,0)) + " " + str(get_object_count(0))
            # print "this is also for grayson " + str(get_object_area(1, 0)) + " " + str(get_object_count(1))
            print "I dont see a cow"
            driveTimed(-30,30,5)


def DEBUG():
    ao()
    exit(0)

def driveToBlackLine():
    driveTimed(-100,-100,1000)
    while True:
        if(analog(0) < 1000):
            drive(-100,-100)
        else:
            driveTimed(0,0,1000)