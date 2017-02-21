from wallaby import *

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