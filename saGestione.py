import gestione.gui

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEventLoop

def ExeGPO(): #main():
    global siGSA

    #app = QtWidgets.QApplication([])
    try:
        siGSA = Gpo.Sigsa()
    except:
        siGSA = False

    if siGPO:
        formGSA = Ui_Dialog()
        formGSA.loop = QEventLoop()

        siGSA = formGSA.siGSA

        formGSA.loop.exec()

        #screen_shot.widget_closed.connect(loop.quit)

        #sys.exit(app.exec_())

