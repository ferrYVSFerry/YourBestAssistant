import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def schermo():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 300, 300)
    win.setWindowTitle("Ciao!")
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    schermo()
