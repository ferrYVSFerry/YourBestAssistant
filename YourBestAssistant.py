from tkinter import END

from PyQt5 import QtCore, QtWidgets
from datetime import datetime
import subprocess
import webbrowser
import TTS
import urllib.request
import re
from googleapiclient.discovery import build
import time
from pynput import keyboard


def close():
    sys.exit()


def assistance():
    subprocess.check_call([sys.executable, 'ReportABug.py'])


def tts(text):
    TTS.tts_it(text)


def ScrapingRequest(self, text, current_time):
    my_api_key = "asdasds"
    my_cse_id = "asdasdasd"
    text = ""
    query = text.replace("Cerca ", "")
    self.AssistantAnswers.append("[" + current_time + "] Scegli tra:\n"
                                                      "1) Google Search Results ""\n"
                                                      "2) Youtube Links""\n"
                                 )

    if text == "1":
        def google_search(search_term, api_key, cse_id, **kwargs):
            service = build("customsearch", "v1", developerKey=api_key)
            res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
            return res

        results = google_search(query, my_api_key, my_cse_id)

        print(self.AssistantAnswers.append("[" + current_time + "]"
                                                                "\n GoogleSearchResults \n"
                                           ))
        print(self.AssistantAnswers.append("[" + current_time + "]"
                                                                "Title == " +
                                           results['items'][0]['title']
                                           ))
        print(self.AssistantAnswers.append("[" + current_time + "]Link ==" +
                                           results['items'][0]['link']
                                           ))
        snippet = results['items'][0]['snippet'].replace("\n", "")
        html_snippet = results['items'][0]['htmlSnippet'].replace("\n", "")
        html_snippet = html_snippet.replace("<b>", "")
        html_snippet = html_snippet.replace("</b>", "")
        html_snippet = html_snippet.replace("<br>", "")
        html_snippet = html_snippet.replace("&nbsp;…", ".")
        print(self.AssistantAnswers.append("[" + current_time + "]"
                                                                "Description == " +
                                           snippet +
                                           html_snippet
                                           ))
        print("\n\n")


class Ui_Assistant(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(Assistant)
        self.AssistantAnswers = QtWidgets.QTextEdit(self.centralwidget)
        self.Questions = QtWidgets.QTextEdit(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.Richiesta = QtWidgets.QLineEdit(self.centralwidget)
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Assistant)
        self.statusbar = QtWidgets.QStatusBar(Assistant)

    def setupUi(self, Assistant):
        Assistant.setObjectName("Assistant")
        Assistant.setDocumentMode(False)
        Assistant.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        Assistant.resize(550, 465)
        Assistant.setMaximumSize(550, 465)
        Assistant.setMinimumSize(550, 465)
        self.centralwidget.setObjectName("centralwidget")

        self.AssistantAnswers.setGeometry(QtCore.QRect(10, 10, 261, 301))

        self.AssistantAnswers.setObjectName("AssistantAnswers")
        self.AssistantAnswers.setReadOnly(True)
        self.AssistantAnswers.setText("Answers: \n")

        self.Questions.setGeometry(QtCore.QRect(280, 10, 261, 301))
        self.Questions.setObjectName("Questions")
        self.Questions.setReadOnly(True)
        self.Questions.setText("Requests: \n")

        self.label.setGeometry(QtCore.QRect(10, 320, 131, 16))
        self.label.setObjectName("label")

        self.Richiesta.setGeometry(QtCore.QRect(10, 340, 371, 21))
        self.Richiesta.setText("")
        self.Richiesta.setObjectName("Richiesta")
        self.Richiesta.returnPressed.connect(lambda: self.richiesta(self.Richiesta.text()))

        self.Submit.setGeometry(QtCore.QRect(390, 340, 141, 23))
        self.Submit.setObjectName("Submit")
        self.Submit.clicked.connect(lambda: self.richiesta(self.Richiesta.text()))

        self.progressBar.setGeometry(QtCore.QRect(10, 370, 521, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.commandLinkButton.setGeometry(QtCore.QRect(10, 400, 131, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(assistance)

        self.commandLinkButton_2.setGeometry(QtCore.QRect(400, 400, 141, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(close)

        Assistant.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")

        Assistant.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        Assistant.setStatusBar(self.statusbar)

        self.retranslateUi(Assistant)
        QtCore.QMetaObject.connectSlotsByName(Assistant)

    def retranslateUi(self, Assistant):
        _translate = QtCore.QCoreApplication.translate
        Assistant.setWindowTitle(_translate("Assistant", "YourBestAssistant"))
        self.label.setText(_translate("Assistant", "Submit your command here"))
        self.Submit.setText(_translate("Assistant", "Submit"))
        self.commandLinkButton.setText(_translate("Assistant", "Report a bug"))
        self.commandLinkButton_2.setText(_translate("Assistant", "Close the app"))

    def richiesta(self, text):
        now = datetime.now()
        search = "Cerca "
        open = "Apri "
        if text == "":
            return
        else:
            current_time = now.strftime("%H:%M:%S")
            self.Questions.append("[" + current_time + "] " + text)
            self.Richiesta.clear()
            if text == "Ciao" or text == "ciao":
                self.AssistantAnswers.append("[" + current_time + "] Ciao! Sono il tuo assistente personale. Scrivi "
                                                                  "\"Help\" per una serie di aiuti.")
                tts("Ciao! Sono il tuo assistente personale. Scrivi help per una serie di aiuti.")
                self.Richiesta.clear()
            elif search in text:

                ScrapingRequest(self, text, current_time)

            elif text == "Help" or text == "help":
                self.AssistantAnswers.append("[" + current_time + "] Per la funzione ricerca digitare: Cerca (es: "
                                                                  "Cerca Casa)")
            elif text == "Exit" or text == "exit":
                close()
            else:
                self.AssistantAnswers.append("[" + current_time + "] Scusa, ma non ho capito bene, potresti ripetere?")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Assistant = QtWidgets.QMainWindow()
    ui = Ui_Assistant()
    ui.setupUi(Assistant)
    Assistant.show()
    sys.exit(app.exec_())
