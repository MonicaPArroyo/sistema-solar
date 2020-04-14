import sys
from PyQt5 import QtGui, QtWidgets
import planetario as planets


def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = planets.SolarSystem()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
