from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titre = QtWidgets.QLabel(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(20, 30, 761, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(-1)
        self.titre.setFont(font)
        self.titre.setStyleSheet("font-size: 30px;")
        self.titre.setObjectName("titre")
        self.texte = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.texte.setGeometry(QtCore.QRect(10, 150, 781, 361))
        self.texte.setObjectName("texte")
        self.appliquer = QtWidgets.QPushButton(self.centralwidget)
        self.appliquer.setGeometry(QtCore.QRect(278, 530, 211, 41))
        self.appliquer.setObjectName("appliquer")
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(12, 110, 611, 25))
        self.filename.setObjectName("filename")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(650, 110, 141, 25))
        self.browse.setObjectName("browse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titre.setText(_translate("MainWindow", "MARKUPvoices Logiciel de reconaissance vocale"))
        self.appliquer.setText(_translate("MainWindow", "Appliquer"))
        self.browse.setText(_translate("MainWindow", "Parcourir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

