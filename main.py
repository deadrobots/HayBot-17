#!/usr/bin/python

import actions as act
import utils as u

def main():
    print "running"
    act.init()

    #act.test()
    act.getFirstHay()
    act.goToFarWall()
    act.turnToHay()
    act.stackHay()
    act.turnToSecondHay()
    act.stackSecondHay()
    act.turnToSecondHay()
    act.stackSecondHay()
    act.hayToBarn()
    act.goToFurrow()
    act.putPomsInFurrow()
    u.DEBUGwithWait()
    act.getToCenter()
    u.DEBUGwithWait()

if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()