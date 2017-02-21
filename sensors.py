#!/usr/bin/python
from wallaby import *
from drive import *

def lookForCow():
    while():
        camera_update()
        if(get_object_count(0)>0 and get_object_area(0,0)>400):
            if(get_object_center(0,0).x > get_camera_width()/2):
                print "Moving Right"
                driveTimed(-30,-40,5)
            elif(get_object_center(0,0).x > get_camera_width()/2):
                print "moving left"
                driveTimed(-40,-30,5)
            else:
                print "Moving Dumb"
                driveTimed(-35,-35,5)
        else:
            driveTimed(-30,30,5)


def DEBUG():
    ao()
    exit(0)