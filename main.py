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
    u.DEBUGwithWait()

if __name__ == "__main__":
    main()