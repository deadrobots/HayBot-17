#!/usr/bin/python
import os, sys
import actions as act

def main():
    act.init()

    act.waitForButton()
    act.grabHay()
    act.goToBackWall()
    act.turnToHay()

    act.shutdown()


















if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();