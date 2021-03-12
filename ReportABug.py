from PyQt5 import QtCore, QtGui, QtWidgets


def close():
    sys.exit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 185)
        MainWindow.setMaximumSize(393, 185)
        MainWindow.setMinimumSize(393, 185)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 371, 121))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.button1 = QtWidgets.QPushButton(MainWindow)
        self.button1.setGeometry(QtCore.QRect(10, 140, 65, 25))
        self.button1.setObjectName("ok")
        self.button1.clicked.connect(close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report a Bug"))
        self.button1.setText(_translate("MainWindow", "OK"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n "
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                         "font-size:8.25pt; font-weight:400; font-style:normal;\">\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                         "font-size:16pt;\">E-mail: lorenzoferrara737@gmail.com</span></p>\n "
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                         "font-size:16pt;\"><br /></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                         "font-size:16pt;\">Discord: ferrYVSFerry#4109</span></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><span style=\" font-size:16pt;\">          "
                                         "  </span><span style=\" font-family:\'Whitney\',\'Helvetica "
                                         "Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; "
                                         "font-size:16pt; font-weight:600; "
                                         "color:#000000;\">𝖒𝖆𝖗𝖈𝖔</span><span style=\" "
                                         "font-family:\'Whitney\',\'Helvetica Neue\',\'Helvetica\',"
                                         "\'Arial\',\'sans-serif\'; font-size:16pt; "
                                         "color:#000000;\">#5306</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
