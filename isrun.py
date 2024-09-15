#!/usr/bin/python3
import os
import subprocess

def isrun(prg): #-flatpack etc- funziona con snap, flatpak etc
#-- gia run
    res = os.popen('pgrep -af ' +prg+ ' | grep -v grep| grep -v task_manager| grep -v defunct').read()

    n = res.count('\n')
    print ('ci sono ' + str(n)  +' istanze attive')

    attivi = res.split('\n')
    idp = attivi[0]
    idp, p = idp.split(' ', 1)

    '''
    s = "notify-send --icon=" + "keyboard" + " -t 5000 'Istanze attive di \n" +\
        idp +' '+ prg +": "+ \
        str(n) +"'"
    os.system(s)
    '''

    if n==1 or (n==2 and 'debugpy' in p):
        return False, idp

    else:

        if prg in p :
            return True, idp
        else:
            return False, idp

def controlla_Single(prg):
    """Use pgrep to check if protonvpn-applet is already running
    """
    p = 'pgrep -af ' + prg
    pid = None

    try:
        pid = subprocess.run(p.split(), check=True, capture_output=True)

    except subprocess.CalledProcessError:
        try:
            pid = subprocess.run(p.split(), check=True, capture_output=True)

        except subprocess.CalledProcessError:
            pass

    if pid is not None:
        #print('There is an instance already running.')
        return True, pid.stdout.decode().split()
    else:
        return False, False
        #sys.exit(1)

'''
#https://github.com/seadanda/protonvpn-applet/blob/master/protonvpn-applet.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSystemTrayIcon, QMenu, QAction, qApp, QMessageBox
from PyQt5.QtCore import QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon

    tray_icon = None

    # Init QSystemTrayIcon
    tray_icon = QSystemTrayIcon(self)
    tray_icon.setIcon(QIcon('icons/16x16/protonvpn-disconnected.png'))

if __name__ == '__main__':
    #isrun('galculator') isrun
    ab, idPrg = controlla_Single('schermoAttivo1.1.py')
    if ab:
        os.system('pkill -9 -f ' + idPrg)
    else:
        os.system('/home/rosa/bin/Py/schermoAttivo/schermoAttivo1.1.py &')
'''

