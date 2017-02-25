#!/usr/bin/python

import actions as act

def main():
    print "running"
    act.init()
    #act.test()
    act.getFirstHay()
    act.goToFarWall()
    act.turnToHay()
    act.stackHay()

if __name__ == "__main__":
    main()