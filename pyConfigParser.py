import os
import configparser
from   tkinter import filedialog, messagebox, Tk

class ConfigIni:
    def mess(self, Titolo='', Messaggio=''):
        ws = Tk()  #.withdraw()
        #ws.geometry('1x1') 
        #ws.wait_visibility(ws)
        #ws.wm_attributes('-alpha', 0.3)    
        messagebox.showwarning(Titolo, Messaggio)

    def __init__(self, Percorso='', nFile=''):
        #if os.path.isfile(pidfile):
        PercorsoIni = Percorso
        self.fileIni = nFile
        #self.Percorso = Percorso
        if not os.path.exists(PercorsoIni) and len(PercorsoIni):
            os.makedirs(PercorsoIni)

        self.fileIni = PercorsoIni +"/"+ self.fileIni
        if not os.path.exists(self.fileIni) and len(nFile):
            File = open(self.fileIni, 'w')
            File.close()

        if nFile == "":
            reso = tkinter.filedialog.askopenfiles(initialdir=gPercorsoIni, title="Scegli il File", filetypes=(("Files di impostazione", "*.*"), ("", "")))
            PercorsoIni = reso[0].name
            PercorsoIni = gPercorsoIni[:reso[0].name.rfind('/')]
            NomeIni = reso[0].name[reso[0].name.rfind('/')+1:]
            #gNomeIni = gNome[:gNomeIni.index('.')]
            self.fileIni = PercorsoIni +"/"+ NomeIni

        self.Config = configparser.ConfigParser()
        self.Config.read(self.fileIni)

    def leggiIni(self, primoVuoto=0):
        #self.Config.read(self.fileIni)
        idx = 0
        iniDati = []
        if primoVuoto:
            iniDati.append([])
            for idx in range(primoVuoto):              
                iniDati[0].append(' ')
            idx = 1
            
        for sez in self.Config.sections():
            iniDati.append([]) #-
            iniDati[idx].append(sez)
            optioni = self.Config.options(sez)
            for opt in optioni:
                valOpz = self.Config.get(sez,opt)
                if valOpz in 'True,False' and valOpz:
                    valOpz = eval(valOpz)

                iniDati[idx].append(valOpz)
            idx += 1
        
        return iniDati

    def sezione(self, sez, param='', valore=''):
        if sez in self.Config.sections():
            if param:
                if param in self.Config[sez]:
                    self.Config.remove_option(sez, param)
        else:
            self.Config.add_section(sez)

        if param:
            self.Config.set(sez, param, str(valore))

    def salva(self):
        with open(self.fileIni, 'w') as configfile:
            self.Config.write(configfile)
            configfile.close()

    def sezioni(self):
        return self.Config.sections()

    def opzioni(self, sezione):
        return self.Config.options(sezione)
        
    def lista(self, sezione):
        x = "" 
        try:
            for opt in self.Config.options(sezione):
                x = x + self.Config.get(sezione, opt) +","

            return x[:-1]
        except:
            self.mess("Errore","La sezione '"+sezione+"'\nnon esiste")

    def valori(self, sezione):
        return lista(self, sezione)

    def valore(self, sezione, param, isBool=False):
        if isBool:
            return self.Config.get(sezione, eval(param))
        else:      
            return self.Config.get(sezione, param)

        
    def cancella(self, sezione, optizione=''):
        pass

'''
sez = 'http.Vodafone.it'
uti = 'arturo.Canaglia'
pwd = 'Qksmxui11Zd<>'
arr = []
Configura = ConfigIni('/home/rosa/bin/Py', 'prova.ini')
arr = Configura.leggiIni(3)
print (arr[2][2])

Configura.sezione('ww.tim.com','Utente', uti)
Configura.sezione('ww.tim.com','Password', pwd)
Configura.salva()
'''
