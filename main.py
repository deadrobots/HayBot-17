#!/usr/bin/python
import os, sys
from wallaby import *
from actions import *

def main():
    startup()
    goToBot()
    grabBotGuy()
    turnToCow()
    cowSpot()
    print "Hello Lego"




if __name__== "__main__":
    sys.stdout =\
        os.fdopen(sys.stdout.fileno(),"w",0)
    main()