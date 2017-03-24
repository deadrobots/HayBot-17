#!/usr/bin/python

import actions as act
import utils as u
import motorsPlusPlus as x

def main():
    print "running"
    act.init()
    act.getFirstHay()
    act.goToFarWall2()
    act.turnToHay()
    act.stackHay()
    act.turnToSecondHay()
    act.stackSecondHay()
    act.square_up_and_drop()
    act.deliverPoms()
    act.turnToThirdHay()
    act.stackThirdHay()
    act.hayToBarn()
    u.DEBUGwithWait()
    act.goToFurrow()
    act.smash()
    act.getToCenter()


if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()