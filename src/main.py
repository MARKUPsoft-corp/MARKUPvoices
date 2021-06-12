##########################  importing of graphical tools ###########################

from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget
from PyQt5.uic import loadUi

########################## importing of voice recognition librairie #######################

import speech_recognition as sr

################################### main class #########################################

class mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        loadUi("ui/reconnaissance.ui", self)
        self.browse.clicked.connect(self.browsefile)        #event about pushbuton "browser": let's call "browserfile" method
        self.appliquer.clicked.connect(self.recognize)      #idem

    #method about geting path of audio file to be recognize

    def browsefile(self):
        fname = QFileDialog.getOpenFileName(self, 'OUVRIR LE FICHIER', '/')
        self.filename.setText(fname[0]) 
        
        ligne = self.filename.text()

        if ligne == " ":
            pass
    
    #recognizer method using googles services

    def recognize(self):
        rec_vocale = sr.Recognizer()
        path = self.filename.text()
        with sr.AudioFile(path) as src:
            audio = rec_vocale.record(src)
            texter = rec_vocale.recognize_google(audio, language="fr-FR")
            self.texte.insertPlainText(texter)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = mainwin()
    windows.show()
    sys.exit(app.exec_())