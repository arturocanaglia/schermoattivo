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

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEventLoop

from pynput import mouse as mouseL
from pynput.mouse import Button, Controller

from pyConfigParser import ConfigIni
from isrun import isrun, controlla_Single

AREANORD = 0
AREANORDEST =1
AREAEST = 2
AREASUDEST = 3
AREASUD = 4
AREASUDOVEST = 5
AREAOVEST = 6
AREANORDOVEST = 7

zona = ['ComandoAreaNord','ComandoAreaNordEst','ComandoAreaEst',\
        'ComandoAreaSudEst', 'ComandoAreaSud','ComandoAreaSudOvest',\
        'ComandoAreaOvest','ComandoAreaNordOvest']
nomePrg = 'schermoAttivo'
Ver = '1.1'

class Area_():
    nome: str
    app: str
    abilita: bool
    singolo: bool
    scarto: int
    aspetta: float
    def __init__(self, *c):
        self.nome = c[0][0]
        self.app = c[0][1]
        self.abilita = c[0][2]
        self.singolo = c[0][3]
        '''
        self.scarto = c[0][4]
        self.aspetta = c[0][5]
        '''

mouse = Controller()

def on_move(x, y):
    pass

def on_scroll(x, y, dx, dy):
    pass

def isrun1(prg, io=False): #-flatpack etc- funziona con snap, flatpak etc
#-- gia run
    p = 'pgrep -af ' +\
        prg +\
        ' | grep -v grep| grep -v task_manager| grep -v defunct'; idp = 0

    res = os.popen(p).read()
    n = res.count('\n')
    #print ('ci sono ' + str(n)  +' istanze attive')

    attivi = res.split('\n')
    idp = attivi[0]

    if n==1 or 'debugpy' in res: 
        return False, idp
    else:
        idp, p = idp.split(' ', 1) if len(idp) else " ", " "
        if prg in p :
            return True, idp
        else:      
            return False, idp

def creaIni(saRC):
    elem = 'abilita'
    for z in zona:
        saRC.sezione(z, 'app', '')
        saRC.sezione(z, elem, 'False')

    saRC.salva()

def mousemove(x, y):
    mouse.move(x, y)  #, absolute=False, duration=0.2

def on_click(x, y, button, pressed):
    if pressed:
        if button.name == 'right':
            print(f'button {button}')

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
hw = width / 2
vw = height / 2
rt = width - 1
bt = height - 1
bounce = 80

#AreaEst = 2
#AreaOvest = 6
def mouseInSA():
    global bounce, hw, vw, rt, bt


    scarto = 80
    check_intervall = 0.7
    zz = None

    time.sleep(0.2)
    pos = mouse.position
    if pos[0] == 0 and pos[1] == 0:
        #- angoli
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == 0 and pos[1] == 0:
            zz = AREANORDOVEST

    elif pos[0] == rt and pos[1] == 0:
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == rt and pos[1] == 0 :
            zz = AREANORDEST

    elif pos[0] == 0 and pos[1] == bt:
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == 0 and pos[1] == bt:
            zz = AREASUDOVEST

    elif pos[0] == rt and pos[1] == bt:
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == rt and pos[1] == bt :
            zz = AREASUDEST

    #- punti cardinali
    elif (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1] == 0:
        time.sleep(check_intervall)
        pos = mouse.position
        if (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1]>=0:
            zz = AREANORD

    elif (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[0] == bt:
        time.sleep(check_intervall)
        pos = mouse.position
        if (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1]>=0:
            zz = AREASUD

    return zz, pos
    #return zona[zz]

def gestioneSA(saRC, param):
    pass

def caricaSA(percorso):
    saRC = ConfigIni(percorso, 'elementiattivi.ini')

    '''
    zAttivi = (sezione, comando, abilita)
    zAttivi[0] [0]      [1]      [2]
    '''

    zAttive = saRC.leggiIni()
    if len(zAttive) == 0:
        creaIni(saRC)
        zAttive = saRC.leggiIni()

    '''
    i=0
    Area = []
    for z in zAttive:
        Area.append([])
        Area[i] = Area_(z)
        i += 1
    '''
    return saRC, zAttive

def SchermoAttivo(zAttive):
    global bounce

    while True:
        #sezioneSA = zona[0]
        sezioneSA, pos = mouseInSA()
        if sezioneSA is not None:
            App = zAttive[sezioneSA][1]
            Abilita = zAttive[sezioneSA][2]
            Singolo = zAttive[sezioneSA][3]

            #if Area[sezioneSA].abilita:
            if Abilita:
                exe = True
                #if Area[sezioneSA].singolo:
                if Singolo:
                    #if isrun(Area[sezioneSA].app):
                    if isrun(App):
                        #attiva app
                        exe = False

                if exe:
                    mousemove(pos[0] + bounce, pos[1] + bounce)
                    #os.system('(' + Area[sezioneSA].app + ') &')
                    os.system('(' + App + ') &')
                    mousemove(pos[0] + bounce, pos[1] + bounce)
                    time.sleep(2)

def abilitaArea(zz, t_f):
    stato = t_f
    if stato is None:
        old = zz[3]
        if old:
            stato = False
        else:
            stato = True

    zz[3] = str(stato)
    saRC.sezione(zz[0], 'abilita', stato)   

def gestioneSA():
    return 0

def sysTray_click(click):
    if click==3: #- sinistro --GESTIONE DX=1 MX=4
        gestioneSA()

if __name__ == '__main__':
    giaAttivo, idPrg = isrun(nomePrg+Ver+'.py')
    #giaAttivo, idPrg = controlla_Single(nomePrg+Ver+'.py')
    #abilitiato = eval(abilitiato)

    p = os.getenv('HOME') +'/.config/'
    saRC, zAttive = caricaSA(p + nomePrg)
    ricarica = True

    if len(sys.argv) == 2:
        #stato = 'False'
        p1, stato = sys.argv[1].split('=') \
                    if sys.argv[1].find('=') >0 \
                    else str(sys.argv[1]), None
                    
        '''if sys.argv[1].find('=') >0:
            p1, stato = sys.argv[1].split('=') 
        else:
            p1, stato = str(sys.argv[1]), 'False' '''

        match p1:
            case "--NOTIFICA": 
                s = "notify-send --icon=" + "keyboard" + \
                    " -t 5000 '" +\
                    idPrg +': '+ nomePrg+Ver+".py Attivo'"
                os.system(s)
                if giaAttivo: quit()

            case "--DEMONE":
                giaAttivo = False

            case "--TRY" | "--GESTIONE":
                icona = True
                if p1 == "--GESTIONE":
                    #- se non cambio qualcosa
                    #idPrg = False
                    ricarica = False

                    #- esco con icona = False
                    icona = False
                    pass

                if icona:
                    if not idPrg:
                        p = '$HOME/bin/Py/schermoAttivo/' + nomePrg+Ver +\
                            '.py --DEMONE &'
                        res = os.popen(p, 'r')   ##.read()
                        #os.system(p)

                    app = QApplication([])
                    app.setQuitOnLastWindowClosed(False)

                    icona = QIcon.fromTheme("/home/rosa/.config/schermoAttivo/zoom-original.svg")

                    tray = QSystemTrayIcon()
                    tray.activated.connect(sysTray_click)
                    tray.setIcon(icona)
                    tray.setVisible(True)
                    app.exec_()

            case ("--AIUTO"):
                #idPrg =True
                ricarica = False

            case ("--STATO"):
                #idPrg =True
                ricarica = False

            case ("--UCCIDI"):
                ricarica = False               
                print(f"Attenzione {nomePrg} in esecuzione verrà chiuso...")
                
            # comment:
            case ("--TUTTI"):
                for za in zAttive:
                    abilitaArea(za, stato)  
                
                saRC.salva()
            
            case ("--ANGOLI"):
                for za in  [AREANORDEST, AREASUDEST,\
                            AREASUDOVEST, AREANORDOVEST]:
                    abilitaArea(zAttive[za], stato)  
                
                saRC.salva()

            case ("--CARDINALI"):
                for za in [AREANORD, AREAEST, AREASUD, AREAOVEST]:
                    abilitaArea(zAttive[za], stato)  
                
                saRC.salva()

            #"--AREANORD","--AREANORDEST","--AREAEST",
            #"--AREASUDEST","--AREASUD","--AREASUDOVEST",
            #"--AREAOVEST","--AREANORDOVEST":
            case other:
                za = eval(p1[2:])
                abilitaArea(zAttive[za], stato)  
                saRC.salva()


        # end match
        #if idPrg == False: os.system('schermoAttivo1.1.py')
    #- end if len()
    elif giaAttivo:               
        print(f"Attenzione {nomePrg} già in esecuzione con ID {idPrg}")
        quit()

    if giaAttivo: os.system('kill -9 ' + idPrg)
    if ricarica:
        SchermoAttivo(zAttive)

