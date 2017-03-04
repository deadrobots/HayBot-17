#!/usr/bin/python

import actions as act
import utils as u

def main():
    print "running"
    act.init()
    # act.test()
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
    act.getToCenter()
    u.DEBUGwithWait()

if __name__ == "__main__":
    main()