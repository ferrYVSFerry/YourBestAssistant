import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QApplication, QLineEdit, \
    QPushButton,QMessageBox
from PyQt5.QtCore import Qt


class SpecialBG(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.setStyleSheet("""
                color: rgba(237,174,28,100%);
                background-color: rgba(0,0,0,100%);
                text-align: center;
                border-radius: 150px;
                border: 1px solid rgba(237,174,28,100%);
                padding: 0px;
                """)




class RoundedCorners(QWidget):
    def __init__(self):
        super(RoundedCorners, self).__init__()
        self.initUI()

    def initUI(self):
        winwidth = 320
        winheight = 320
        VBox = QVBoxLayout()
        roundyround = SpecialBG(self)
        VBox.addWidget(roundyround)
        self.setLayout(VBox)

        # self.setWindowOpacity(0.9) #opacità

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.SplashScreen
        )

        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setGeometry(30, 30, winwidth, winheight)
        self.setWindowTitle('Werisme')

        self.textbox = QLineEdit(self)
        self.textbox.move(0, 20)
        self.textbox.resize(320, 30)

        self.button = QPushButton('read', self)
        self.button.move(100, 70)
        self.button.clicked.connect(self.on_click)

        self.show()


    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self,
                             'Message - pythonspot.com',
                             "You typed: " + textboxValue
                             )
        self.textbox.setText("")

def main():
    app = QApplication(sys.argv)
    alldone = RoundedCorners()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()