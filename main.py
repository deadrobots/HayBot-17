#!/usr/bin/python

import actions as act
import utils as u


def main():
    print "running"
    act.init()
    act.getFirstHay()
    act.goToFarWall2()
    act.turnToHay()
    act.stackHay()
    act.GoToSecondHay()
    act.stackSecondHay()
    act.square_up_and_drop()
    act.deliverPoms()
    act.goToThirdHay()
    act.stackThirdHay()
    act.hayToBarn()
    u.DEBUGwithWait()



if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()