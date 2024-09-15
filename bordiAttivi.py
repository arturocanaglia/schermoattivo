#!/usr/bin/env python
#
# hotcorners:
# A script for adding hot corners to Openbox.
# Repackaged for BunsenLabs by John Crawley.
# Originally written for CrunchBang Linux <http://crunchbang.org/>
# by Philip Newborough <corenominal@corenominal.org>
#
# BordiAttivi:
# by Arturo Canaglia modificato con ativazione metà schermo e menu popup
# per gestione attivazioni e ini file
# ----------------------------------------------------------------------


import sys, time, os  #, re
import configparser
import tkinter as tk
import mouse
import pyConfigParser

#from Xlib import display  # type: ignore
#from Xlib.ext.xtest import fake_input # type: ignore
#from Xlib import X  # type: ignore
#from subprocess import Popen, PIPE, STDOUT

bounce = 80
scarto = 80
check_intervall = 0.7

Config = configparser.ConfigParser()
cfgdir = os.getenv("HOME")+"/.config/hotcorners2024"
rcfile = cfgdir+"/hotcornersrc"

##-
def setCorners(set):
    if set:
        #Config = configparser.ConfigParser()

        cfgfile = open(rcfile,'w+') #-- a x aggiungere

        Config.add_section('Hot Corners')
        Config.set('Hot Corners','top_left_corner_command', '')  #--skippy-xd
        Config.set('Hot Corners','top_right_corner_command', '')
        Config.set('Hot Corners','bottom_left_corner_command', '')
        Config.set('Hot Corners','bottom_right_corner_command', '')

        Config.set('Hot Corners','middle_right_corner_command', '')
        Config.set('Hot Corners','middle_left_corner_command', '')
        Config.set('Hot Corners','middle_top_corner_command', '')
        Config.set('Hot Corners','middle_bottom_corner_command', '')

        Config.add_section('Enable Corners')
        Config.set('Enable Corners','top_left', 'true')
        Config.set('Enable Corners','top_right', 'true')
        Config.set('Enable Corners','bottom_left', 'true')
        Config.set('Enable Corners','bottom_right', 'true')

        Config.set('Enable Corners','top_middle', 'true')
        Config.set('Enable Corners','bottom_middle', 'true')
        Config.set('Enable Corners','right_middle', 'true')
        Config.set('Enable Corners','left_middle', 'true')

        Config.write(cfgfile)
        cfgfile.close()


def getOS():
    return sys.platform

def popUpMenu():
    pippo=0

def isrun(prg): #-flatpack etc- funziona con snap, flatpak etc
#-- gia run
    res = os.popen('pgrep -af ' + prg +'|head -n 1 ').read()
    res1 = res.split(' ', 1)
    res = res1[1]
    res = res.split("/")[-1]
    res = res.split("\n")
    if res[0] == prg:
        return res1[0]
    else:
        return False


class BordiAttivi(tk.Tk):

    def __init__(self, idPrg):
        super().__init__()

        #self.title('Image Labels')
        self.idPrg = idPrg
        if self.idPrg:
            return None

        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        hw = width / 2
        vw = height / 2
        rt = width - 1
        bt = height - 1

        def print_usage():
            print("Hotcorners 2024 Debian: usage:")
            print("  --help          show this message and exit")
            print("  --kill          attempt to kill any running instances")
            print("  --daemon        run daemon and listen for cursor triggers")
            print("")
            exit()

        if len(sys.argv) < 2 or sys.argv[1] == "--help":
            print_usage()

        elif sys.argv[1] == "--kill":
            print("Attenzione ogni hotcorners2024 in esecuzione verrà chiuso...")
            os.system('pkill -9 -f hotcorners2024')
            exit()

        elif sys.argv[1] == "--daemon":
            #disp = display.Display()
            #root = display.Display().screen().root

            ######## setCorners (True)

            def mousepos():
                data = mouse.get_position()
                return data[0], data[1]

            def mousemove(x, y):
                mouse.move(x, y, absolute=False, duration=0.2)

            '''def mousegetclick(tasto):
                mouse.get
                if tasto == "right":
                   print("tasto right")'''
                   #data = mouse.on_right_click(lambda: popUpMenu(), args=())

            try:
                cfgfile = open(rcfile)
            except IOError as e:
                if not os.path.exists(cfgdir):
                    os.makedirs(cfgdir)
                    setCorners (True)

            while True:
                Config.read(rcfile)
                time.sleep(0.2)
                pos = mousepos()
                '''
                if mouse.is_pressed("right"):
                    data = mouse.on_right_click(lambda: popUpMenu(), args=())
                    #mousegetclick("right")
                '''
                mouse.on_click(lambda: print("Left Button clicked."))
                mouse.on_right_click(lambda: print("Right Button clicked."))

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

                elif (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1] == 0:
                    if Config.get('Enable Corners','top_middle') != 'false':
                        if Config.get('Hot Corners','top_middle_corner_command') != '':
                            time.sleep(check_intervall)
                            pos = mousepos()
                            if (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1]>=0:
                                mousemove(pos[0] - bounce, pos[1] - bounce)
                                os.system('(' + Config.get('Hot Corners','top_middle_corner_command') + ') &')
                                mousemove(pos[0] - bounce, pos[1] - bounce)
                                time.sleep(2)

                elif (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[0] == bt:
                    if Config.get('Enable Corners','bottom_middle') != 'false':
                        if Config.get('Hot Corners','bottom_middle_corner_command') != '':
                            time.sleep(check_intervall)
                            pos = mousepos()
                            if (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1]>=0:
                                mousemove(pos[0] - bounce, pos[1] - bounce)
                                os.system('(' + Config.get('Hot Corners','bottom_middle_corner_command') + ') &')
                                mousemove(pos[0] - bounce, pos[1] - bounce)
                                time.sleep(2)

        else:
            print_usage()

if __name__ == '__main__':
    nomePrg = sys.argv[0]
    nomePrg = nomePrg.split("/")[-1]
    idPrg = isrun('nomePrg')
    root = BordiAttivi(idPrg)
    #root.mainloop()
