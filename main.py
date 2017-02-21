#!/usr/bin/python
import os, sys
from wallaby import *
from actions import *
from sensors import *

def main():
    print "Hello Lego"
    #startup()
    #goToBot()
    #grabBotGuy()
    #turnToCow()
    #lookForCow()
    driveToBlackLine()



if __name__== "__main__":
    sys.stdout =\
        os.fdopen(sys.stdout.fileno(),"w",0)
    main()