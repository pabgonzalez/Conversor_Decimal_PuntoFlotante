# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#_MyCode
from PyQt5.QtWidgets import QMessageBox
from backend import binf2dec, dec2binf, isBinary
import numpy as np
import locale
#_

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 348)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 830, 168))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.buttonConvertirDec = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.buttonConvertirDec.setFont(font)
        self.buttonConvertirDec.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(221, 221, 221);\n"
"color: black;")
        self.buttonConvertirDec.setObjectName("buttonConvertirDec")
        self.gridLayout.addWidget(self.buttonConvertirDec, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttonConvertirHexa = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.buttonConvertirHexa.setFont(font)
        self.buttonConvertirHexa.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(221, 221, 221);\n"
"color: black;\n")
        self.buttonConvertirHexa.setObjectName("buttonConvertirHexa")
        self.gridLayout.addWidget(self.buttonConvertirHexa, 1, 2, 1, 1)
        self.ioDecimal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.ioDecimal.setFont(font)
        self.ioDecimal.setStyleSheet("border: 1px solid black;")
        self.ioDecimal.setObjectName("ioDecimal")
        self.gridLayout.addWidget(self.ioDecimal, 2, 1, 1, 1)
        self.ioHexa = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.ioHexa.setFont(font)
        self.ioHexa.setStyleSheet("border: 1px solid black;\n"
"")
        self.ioHexa.setObjectName("ioHexa")
        self.gridLayout.addWidget(self.ioHexa, 1, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.ioBinario = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.ioBinario.setFont(font)
        self.ioBinario.setStyleSheet("border: 1px solid black;")
        self.ioBinario.setObjectName("ioBinario")
        self.gridLayout.addWidget(self.ioBinario, 0, 1, 1, 1)
        self.buttonConvertirFP = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.buttonConvertirFP.setFont(font)
        self.buttonConvertirFP.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(221, 221, 221);\n"
"color: black;")
        self.buttonConvertirFP.setObjectName("buttonConvertirFP")
        self.gridLayout.addWidget(self.buttonConvertirFP, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 190, 101, 111))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 91, 86))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b16 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.b16.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        self.b16.setFont(font)
        self.b16.setStyleSheet("")
        self.b16.setChecked(True)
        self.b16.setObjectName("b16")
        self.verticalLayout.addWidget(self.b16)
        self.b32 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        self.b32.setFont(font)
        self.b32.setObjectName("b32")
        self.verticalLayout.addWidget(self.b32)
        self.b64 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        self.b64.setFont(font)
        self.b64.setObjectName("b64")
        self.verticalLayout.addWidget(self.b64)
        self.buttonInstrucciones = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInstrucciones.setGeometry(QtCore.QRect(690, 260, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonInstrucciones.setFont(font)
        self.buttonInstrucciones.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"background-color: black;\n"
"border: 2px solid black;")
        self.buttonInstrucciones.setObjectName("buttonInstrucciones")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #_MyCode
        self.buttonConvertirFP.clicked.connect(self.calc2Decimal)
        self.buttonConvertirDec.clicked.connect(self.calc2FP)  
        self.buttonConvertirHexa.clicked.connect(self.calcHexa2Dec)
        self.buttonInstrucciones.clicked.connect(self.mostrarInstrucciones)
        #_

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Conversor Decimal <-> Punto Flotante IEEE 754", "Conversor Decimal <-> Punto Flotante IEEE 754"))
        self.label_3.setText(_translate("MainWindow", "Decimal"))
        self.buttonConvertirDec.setText(_translate("MainWindow", "Convertir"))
        self.label_2.setText(_translate("MainWindow", "Hexadecimal"))
        self.buttonConvertirHexa.setText(_translate("MainWindow", "Convertir"))
        self.label_1.setText(_translate("MainWindow", "Binario"))
        self.buttonConvertirFP.setText(_translate("MainWindow", "Convertir"))
        self.groupBox.setTitle(_translate("MainWindow", "#Bits"))
        self.b16.setText(_translate("MainWindow", "16 bits"))
        self.b32.setText(_translate("MainWindow", "32 bits"))
        self.b64.setText(_translate("MainWindow", "64 bits"))
        self.buttonInstrucciones.setText(_translate("MainWindow", "Instrucciones"))

    #_MyCode
    def calc2Decimal(self):
        fp = self.ioBinario.text()
        if not isBinary(fp):
            self.ioDecimal.setText('Error: debe ingresa un número binario.')
            return
        if len(fp)!=16 and len(fp)!=32 and len(fp)!=64:
            self.ioDecimal.setText('Error: la cantidad de bits debe ser 16, 32 o 64.')
            return

        fp_array = np.array( list(fp) )
        output = binf2dec(fp_array)

        if output == 'error':
            self.ioDecimal.setText('Error inesperado')
        else:
            self.ioHexa.setText(hex(int(fp,2))[2:].zfill(int(self.nBits()/4)).upper()) #entrada en hexa
            self.ioDecimal.setText(str(output)) #resultado decimal
            if len(fp) == 16: self.b16.setChecked(True)
            elif len(fp) == 32: self.b32.setChecked(True)
            elif len(fp) == 64: self.b64.setChecked(True)

    def calcHexa2Dec(self):
        try:
            bits = self.nBits()
            self.ioBinario.setText(bin(int(self.ioHexa.text(), 16))[2:].zfill(bits))
            self.calc2Decimal()
        except:
            self.ioHexa.setText('Ingrese un número hexadecimal válido')


    def calc2FP(self):
        b = self.nBits()
        if b != -1:
            d = self.ioDecimal.text()
            try:
                dec = locale.atof(d)
                output = ''.join( dec2binf(dec,b).tolist() )
            except:
                output = 'error'
            
            if output == 'error':
                self.ioBinario.setText('Error: debe ingresar un número decimal válido')
            elif output.isnumeric():
                self.ioBinario.setText(output)
                self.ioHexa.setText(hex(int(output,2))[2:].zfill(int(self.nBits()/4)).upper()) 
            else:
                self.ioBinario.setText(output)
                self.ioHexa.setText('')
        else:
            self.ioBinario.setText('Error: debe seleccionar la cantidad de bits para punto flotante')
	
    def mostrarInstrucciones(self):
        instrucciones = QMessageBox()
        instrucciones.setWindowTitle('Instrucciones')
        instrucciones.setText('Conversión Decimal a Punto Flotante:\n 1) Elija el número de bits que desea para la representación en punto flotante (por defecto 16 bits).\n 2) Ingrese el número decimal (ejemplos: 6932, -3.643E-7, \'-inf\', \'NaN\', \'8e-5\').\n 3) Presione el botón \'Convertir\' a la derecha del número decimal.\n\n Conversión Punto Flotante a Decimal:\n 1) Ingrese el número en representación de punto flotante (puede hacerlo en binario o en hexadecimal).\n 2) Presione el botón \'Convertir\' ubicado a la derecha de su entrada.')
        instrucciones.setIcon(QMessageBox.Information)
        instrucciones.setStandardButtons(QMessageBox.Close)
        #instrucciones.setInformativeText('informative')

        instrucciones.exec_()

    def nBits(self):
        if self.b16.isChecked():
            return 16
        elif self.b32.isChecked():
            return 32
        elif self.b64.isChecked():
            return 64
        else:
            return -1
#_

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
