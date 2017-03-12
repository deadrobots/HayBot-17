#!/usr/bin/python

import actions as act
import utils as u

def main():
    print "running"
    print "testing"
    act.init()

    #act.test()
    act.getFirstHay()
    #act.goToFarWall()
    act.goToFarWall2()
    act.turnToHay()
    act.stackHay()
    act.turnToSecondHay()
    act.stackSecondHay()
    act.turnToSecondHay()
    act.stackSecondHay()
    act.hayToBarn()
    act.goToFurrow()
    #act.putPomsInFurrow()
    act.putPomsInFurrow2()
    act.getToRamp()
    act.getToCenter()



if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()