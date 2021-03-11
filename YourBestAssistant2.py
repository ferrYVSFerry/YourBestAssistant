"""
File contente le informazioni prime che inizializzano una prima versione dell'assistente virtuale/vocale

by Ferrara Lorenzo
please don't modify this files unless you are sure of what you are doing :(((((((
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 335)
        MainWindow.setMinimumSize(381, 335)
        MainWindow.setMaximumSize(381, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Testo_Inviato = QtWidgets.QTextEdit(self.centralwidget)
        self.Testo_Inviato.setGeometry(QtCore.QRect(10, 220, 361, 31))
        self.Testo_Inviato.setObjectName("Testo_Inviato")

        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(10, 260, 121, 31))
        self.Submit.setObjectName("Submit")
        self.Submit.clicked.connect(self.submit)

        self.Restart = QtWidgets.QPushButton(self.centralwidget)
        self.Restart.setGeometry(QtCore.QRect(250, 260, 121, 31))
        self.Restart.setObjectName("Restart")
        self.Restart.clicked.connect(self.restart)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 190, 121, 17))
        self.checkBox.setObjectName("checkBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(149, 10, 221, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSubmit = QtWidgets.QAction(MainWindow)
        self.actionSubmit.setObjectName("actionSubmit")
        self.actionSubmit.triggered.connect(self.submit)

        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionRestart.triggered.connect(self.restart)

        self.menuMenu.addAction(self.actionSubmit)
        self.menuMenu.addAction(self.actionRestart)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YourBestAssistant"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.Restart.setText(_translate("MainWindow", "Restart"))
        self.checkBox.setText(_translate("MainWindow", "For Testing Purposes"))
        self.label.setText(_translate("MainWindow", "Write \"Hello!\" for getting an answer."))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSubmit.setText(_translate("MainWindow", "Submit"))
        self.actionSubmit.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionRestart.setShortcut(_translate("MainWindow", "Ctrl+R"))

    def submit(self):
        if self.checkBox.isChecked():
            print("Test")
        elif self.Testo_Inviato.toPlainText() == "Hello!":
            print("Hello, I'm your personal assistant!")
        else:
            print("No answers allowed, sorry...")

    def restart(self):
        self.Testo_Inviato.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
