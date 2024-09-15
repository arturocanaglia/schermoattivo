#!/usr/bin/env python
# bl-hotcorners:
# A script for adding hot corners to Openbox.
# Repackaged for BunsenLabs by John Crawley.
# Originally written for CrunchBang Linux <http://crunchbang.org/>
# by Philip Newborough <corenominal@corenominal.org>
# ----------------------------------------------------------------------


from Xlib import display
from Xlib.ext.xtest import fake_input
from Xlib import X
from subprocess import Popen, PIPE, STDOUT
import tkinter as tk
import sys, time, os, re
import configparser

check_intervall = 0.7
#--
root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#--
#p = Popen(['xdotool','getdisplaygeometry'], stdout=PIPE, stderr=STDOUT)
#Dimensions = p.communicate()
#Dimensions = Dimensions[0].decode('utf_8')
#Dimensions = Dimensions.replace('\n', '')
#Dimensions = Dimensions.split(' ')
#width = int(Dimensions[0])
#height = int(Dimensions[1])
hw = width / 2
rt = width - 1
bt = height - 1

vw = height / 2

def isrun(prg):
#-- mktemp --suffix=hotcorners
#-- gia run
  esiste = os.system('ps ax | grep -v grep | grep ' + prg +' 1> /dev/null')
  esiste >>= 8  # The return code is specified in the second byte
  return not esiste

def print_usage():
    print("bl-hotcorners: usage:")
    print("  --help          show this message and exit")
    print("  --kill          attempt to kill any running instances")
    print("  --daemon        run daemon and listen for cursor triggers")
    print("")
    exit()

if len(sys.argv) < 2 or sys.argv[1] == "--help":
    print_usage()

elif sys.argv[1] == "--kill":
    print("Attempting to kill any running instances...")
    os.system('pkill -9 -f bl-hotcorners2')
    exit()

elif sys.argv[1] == "--daemon":
    Config = configparser.ConfigParser()
    cfgdir = os.getenv("HOME")+"/.config/bl-hotcorners"
    rcfile = cfgdir+"/bl-hotcornersrc"
    bounce = 40
    disp = display.Display()
    root = display.Display().screen().root

    def mousepos():
        data = root.query_pointer()._data
        return data["root_x"], data["root_y"], data["mask"]

    def mousemove(x, y):
        fake_input(disp, X.MotionNotify, x=x, y=y)
        disp.sync()

    try:
        cfgfile = open(rcfile)
    except IOError as e:
        if not os.path.exists(cfgdir):
            os.makedirs(cfgdir)
        cfgfile = open(rcfile,'w')
        Config.add_section('Hot Corners')
        Config.set('Hot Corners','top_left_corner_command', 'gmrun')
        Config.set('Hot Corners','top_right_corner_command', 'skippy-xd')
        Config.set('Hot Corners','bottom_left_corner_command', 'pulseeffect')
        Config.set('Hot Corners','bottom_right_corner_command', 'pavucontrol')

        Config.set('Hot Corners','middle_right_corner_command', '')
        Config.set('Hot Corners','middle_left_corner_command', '')
        Config.set('Hot Corners','top_middle_corner_command', '')
        Config.set('Hot Corners','bottom_middle_corner_command', '')

        Config.add_section('Enable Corners')
        Config.set('Enable Corners','top_left', 'true')
        Config.set('Enable Corners','top_right', 'true')
        Config.set('Enable Corners','bottom_left', 'true')
        Config.set('Enable Corners','bottom_right', 'true')

        Config.set('Enable Corners','top_middle', 'true')
        Config.set('Enable Corners','middle_right', 'true')
        Config.set('Enable Corners','middle_left', 'true')
        Config.set('Enable Corners','bottom_middle', 'true')

        Config.write(cfgfile)
        cfgfile.close()

    while True:
        Config.read(rcfile)
        time.sleep(0.2)
        pos = mousepos()

        if pos[0] == 0 and pos[1] == 0:
            if Config.get('Enable Corners','top_left') != 'false':
                if Config.get('Hot Corners','top_left_corner_command') != '':
                    time.sleep(check_intervall)
                    pos = mousepos()
                    if pos[0] == 0 and pos[1] == 0:
                        if not isrun(Config.get('Hot Corners','top_left_corner_command')):
                            mousemove(pos[0] + bounce, pos[1] + bounce)
                            os.system('(' + Config.get('Hot Corners','top_left_corner_command') + ') &')
                            mousemove(pos[0] + bounce, pos[1] + bounce)
                            time.sleep(2)

        elif pos[0] == rt and pos[1] == 0:
            if Config.get('Enable Corners','top_right') != 'false':
               if Config.get('Hot Corners','top_right_corner_command') != '':
                   time.sleep(check_intervall)
                   pos = mousepos()
                   if pos[0] == rt and pos[1] == 0 :
                       if not isrun(Config.get('Hot Corners','top_left_corner_command')):
                           mousemove(pos[0] - bounce, pos[1] + bounce)
                           os.system('(' + Config.get('Hot Corners','top_right_corner_command') + ') &')
                           mousemove(pos[0] - bounce, pos[1] + bounce)
                           time.sleep(2)

        elif pos[0] == 0 and pos[1] == bt:
            if Config.get('Enable Corners','bottom_left') != 'false':
                if Config.get('Hot Corners','bottom_left_corner_command') != '':
                    time.sleep(check_intervall)
                    pos = mousepos()
                    if pos[0] == 0 and pos[1] == bt:
                       mousemove(pos[0] + bounce, pos[1] - bounce)
                       os.system('(' + Config.get('Hot Corners','bottom_left_corner_command') + ') &')
                       mousemove(pos[0] + bounce, pos[1] - bounce)
                       time.sleep(2)

        elif pos[0] == rt and pos[1] == bt:
            if Config.get('Enable Corners','bottom_right') != 'false':
               if Config.get('Hot Corners','bottom_right_corner_command') != '':
                   time.sleep(check_intervall)
                   pos = mousepos()
                   if pos[0] == rt and pos[1] == bt :
                       mousemove(pos[0] - bounce, pos[1] + bounce)
                       os.system('(' + Config.get('Hot Corners','bottom_right_corner_command') + ') &')
                       mousemove(pos[0] - bounce, pos[1] + bounce)
                       time.sleep(2)

        elif (pos[0] >= hw-10 and pos[0] <= hw+10) and pos[1] == 0:
            if Config.get('Enable Corners','top_middle') != 'false':
                if Config.get('Hot Corners','top_middle_corner_command') != '':
                    time.sleep(check_intervall)
                    pos = mousepos()
                    if (pos[0] >= hw-10 and pos[0] <= hw+10) and pos[1]:
                        mousemove(pos[0] - bounce, pos[1] - bounce)
                        os.system('(' + Config.get('Hot Corners','top_middle_corner_command') + ') &')
                        mousemove(pos[0] - bounce, pos[1] - bounce)
                        time.sleep(2)

else:
    print_usage()
