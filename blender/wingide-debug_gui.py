'''This is a gui launcher, with WingIDE debugging capabilities. Note that this
is basically the original blender debug file supplied by Wingware, with
a couple small filepath modifications to ease the transition to Git's
distributed development.
'''

# standard
import os
import sys
# related
import Blender
from Blender import Window
# local

# Edit your wingide path if needed
winghome = r'/usr/lib/wingide3.1'

scriptpath = os.path.abspath(os.path.curdir)
# Blender seems to initialize the module from an odd location,
# this is a temp hack.
scriptpath = r'/home/lee/Programming/bmrf/src/blender'
scriptfile = r'%s/gui.py' % scriptpath

print 'Test path: ' + scriptpath
print 'Test file: ' + scriptfile

os.environ['WINGHOME'] = winghome
if winghome not in sys.path:
    sys.path.append(winghome)
#os.environ['WINGDB_LOGFILE'] = r'%s/blender-debug.log' % scriptpath
import wingdbstub
wingdbstub.debugger.StartDebug()

def runfile(filename):
    execfile(filename)
runfile(scriptfile)


