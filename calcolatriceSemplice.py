"""
File contenente lo script per inizializzare un'applicazione virtuale funzionante da calcolatrice per l'assistente
virtuale/vocale

by Ferrara Lorenzo
please don't modify this files unless you are sure of what you are doing
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


def number_display():
    x = ""
    for i in range(len(number)):
        x = x + str(number[i])
    return x


def operazione():
    if stack[1] == "+":
        x = stack[0] + Ui_MainWindow.setupUi
    elif stack[1] == "+":
        print("pop")
    elif stack[1] == "+":
        print("pop")
    else:
        print("pop")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 300)
        MainWindow.setMinimumSize(220, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(201, 10, 30, 31))
        self.textEdit1.setObjectName("textEdit1")
        self.textEdit1.setReadOnly(True)

        self.Numero_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_1.setGeometry(QtCore.QRect(10, 50, 41, 41))
        self.Numero_1.setObjectName("Numero_1")
        self.Numero_1.clicked.connect(lambda: self.button_pressed(1))

        self.Numero_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_2.setGeometry(QtCore.QRect(60, 50, 41, 41))
        self.Numero_2.setObjectName("Numero_2")
        self.Numero_2.clicked.connect(lambda: self.button_pressed(2))

        self.Numero_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_3.setGeometry(QtCore.QRect(110, 50, 41, 41))
        self.Numero_3.setObjectName("Numero_3")
        self.Numero_3.clicked.connect(lambda: self.button_pressed(3))

        self.Numero_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_4.setGeometry(QtCore.QRect(10, 100, 41, 41))
        self.Numero_4.setObjectName("Numero_4")
        self.Numero_4.clicked.connect(lambda: self.button_pressed(4))

        self.Numero_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_5.setGeometry(QtCore.QRect(60, 100, 41, 41))
        self.Numero_5.setObjectName("Numero_5")
        self.Numero_5.clicked.connect(lambda: self.button_pressed(5))

        self.Numero_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_6.setGeometry(QtCore.QRect(110, 100, 41, 41))
        self.Numero_6.setObjectName("Numero_6")
        self.Numero_6.clicked.connect(lambda: self.button_pressed(6))

        self.Numero_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_7.setGeometry(QtCore.QRect(10, 150, 41, 41))
        self.Numero_7.setObjectName("Numero_7")
        self.Numero_7.clicked.connect(lambda: self.button_pressed(7))

        self.Numero_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_8.setGeometry(QtCore.QRect(60, 150, 41, 41))
        self.Numero_8.setObjectName("Numero_8")
        self.Numero_8.clicked.connect(lambda: self.button_pressed(8))

        self.Numero_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_9.setGeometry(QtCore.QRect(110, 150, 41, 41))
        self.Numero_9.setObjectName("Numero_9")
        self.Numero_9.clicked.connect(lambda: self.button_pressed(9))

        self.Numero_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Numero_0.setGeometry(QtCore.QRect(10, 200, 41, 41))
        self.Numero_0.setObjectName("Numero_0")
        self.Numero_0.clicked.connect(lambda: self.button_pressed(0))

        self.Funzione_piu = QtWidgets.QPushButton(self.centralwidget)
        self.Funzione_piu.setGeometry(QtCore.QRect(160, 50, 41, 41))
        self.Funzione_piu.setObjectName("Funzione_piu")
        self.Funzione_piu.clicked.connect(lambda: self.button_pressed("+"))

        self.Funzione_meno = QtWidgets.QPushButton(self.centralwidget)
        self.Funzione_meno.setGeometry(QtCore.QRect(160, 100, 41, 41))
        self.Funzione_meno.setObjectName("Funzione_meno")
        self.Funzione_meno.clicked.connect(lambda: self.button_pressed("-"))

        self.Funzione_diviso = QtWidgets.QPushButton(self.centralwidget)
        self.Funzione_diviso.setGeometry(QtCore.QRect(160, 150, 41, 41))
        self.Funzione_diviso.setObjectName("Funzione_diviso")
        self.Funzione_diviso.clicked.connect(lambda: self.button_pressed("/"))

        self.Funzione_per = QtWidgets.QPushButton(self.centralwidget)
        self.Funzione_per.setGeometry(QtCore.QRect(160, 200, 41, 41))
        self.Funzione_per.setObjectName("Funzione_per")
        self.Funzione_per.clicked.connect(lambda: self.button_pressed("x"))

        self.Funzione_uguale = QtWidgets.QPushButton(self.centralwidget)
        self.Funzione_uguale.setGeometry(QtCore.QRect(110, 200, 41, 41))
        self.Funzione_uguale.setObjectName("Funzione_uguale")
        self.Funzione_uguale.clicked.connect(lambda: self.button_pressed("="))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 216, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Numero_1.setText(_translate("MainWindow", "1"))
        self.Numero_2.setText(_translate("MainWindow", "2"))
        self.Numero_3.setText(_translate("MainWindow", "3"))
        self.Numero_4.setText(_translate("MainWindow", "4"))
        self.Numero_5.setText(_translate("MainWindow", "5"))
        self.Numero_6.setText(_translate("MainWindow", "6"))
        self.Numero_7.setText(_translate("MainWindow", "7"))
        self.Numero_8.setText(_translate("MainWindow", "8"))
        self.Numero_9.setText(_translate("MainWindow", "9"))
        self.Numero_0.setText(_translate("MainWindow", "0"))
        self.Funzione_piu.setText(_translate("MainWindow", "+"))
        self.Funzione_meno.setText(_translate("MainWindow", "-"))
        self.Funzione_diviso.setText(_translate("MainWindow", "/"))
        self.Funzione_per.setText(_translate("MainWindow", "x"))
        self.Funzione_uguale.setText(_translate("MainWindow", "="))

    def button_pressed(self, text):
        if not isinstance(text, int):
            if not self.textEdit.toPlainText():
                self.textEdit.setText("ERRORE")
            else:
                self.textEdit1.setText(text)
                stack.append(text)
        elif not stack:
            number.append(text)
            self.textEdit.setText(number_display())
        else:
            number.clear()
            stack.append(int(self.textEdit.toPlainText()))


if __name__ == "__main__":
    stack = []
    number = []
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
