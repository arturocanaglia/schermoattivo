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

from pynput import mouse as mouseL
from pynput.mouse import Button, Controller

from pyConfigParser import ConfigIni

AreaNord = 0
AreaNordEst =1
AreaEst = 2
AreaSudEst = 3
AreaSud = 4
AreaSudOvest = 5
AreaOvest = 6
AreaNordOvest = 7

zona = ['ComandoAreaNord','ComandoAreaNordEst','ComandoAreaEst',\
        'ComandoAreaSudEst', 'ComandoAreaSud','ComandoAreaSudOvest',\
        'ComandoAreaOvest','ComandoAreaNordOvest']

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
        self.abilita = eval(c[0][2])
        self.singolo = eval(c[0][3])
        '''
        self.scarto = c[0][4]
        self.aspetta = c[0][5]
        '''

mouse = Controller()

def on_move(x, y):
    pass

def on_scroll(x, y, dx, dy):
    pass

def isrun(prg): #-flatpack etc- funziona con snap, flatpak etc
#-- gia run
    p = ''; idp = ''
    res = os.popen( 'pgrep -af ' +\
                    prg +\
                    '| grep -v grep| grep -v task_manager| grep -v defunct').read()
    if res != '':
        idp, p = res.split(' ', 1)
        p, fuffa = p.split('\n', 1)

    if prg == p:
        return idp
    else:
        return False

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
            zz = AreaNordOvest

    elif pos[0] == rt and pos[1] == 0:
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == rt and pos[1] == 0 :
            zz = AreaNordEst

    elif pos[0] == 0 and pos[1] == bt:
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == 0 and pos[1] == bt:
            zz = AreaSudOvest

    elif pos[0] == rt and pos[1] == bt:
        time.sleep(check_intervall)
        pos = mouse.position
        if pos[0] == rt and pos[1] == bt :
            zz = AreaSudEst

    #- punti cardinali
    elif (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1] == 0:
        time.sleep(check_intervall)
        pos = mouse.position
        if (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1]>=0:
            zz = AreaNord

    elif (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[0] == bt:
        time.sleep(check_intervall)
        pos = mouse.position
        if (pos[0] >= hw-bounce and pos[0] <= hw+bounce) and pos[1]>=0:
            zz = AreaSud

    return zz, pos
    #return zona[zz]

def gestioneSA(saRC):
    saRC.sezione(sez, param='', valore='')

def caricaSA(idPrg, nomePrg):
    n = nomePrg.split('.py')
    n = os.getenv('HOME') +'/.config/'+ n[0]
    saRC = ConfigIni(n, 'elementiattivi.ini')

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
            Abilita = eval(zAttive[sezioneSA][2])
            Singolo = eval(zAttive[sezioneSA][3])

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

if __name__ == '__main__':
    nomePrg = __file__   #con pathidPrg, nomePrg
    nomePrg = nomePrg.split("/")[-1]
    idPrg = isrun(nomePrg)
    saRC, zAttive = caricaSA(idPrg, nomePrg)

    if idPrg:
        if len(sys.argv) == 2:
            match (sys.argv[1]):
            # comment:
                case ("--GESTIONE"):
                    gestioneSA(_)

                case ("--UCCIDI"):
                    print(f"Attenzione ogni istanza di {nomePrg} in esecuzione verrà chiusa...")
                        os.system('pkill -9 -f ' + nomePrg)
                        exit()

                case ("--ANGOLI"):
                    pass
                case ("--CARDINALI"):
                    pass
                case ("--POLI"):
                    pass
                case ("--TUTTI"):
                    pass

                # comment:
                case (_):
                    pass
            # end match
    else:
        root = SchermoAttivo(zAttive)
