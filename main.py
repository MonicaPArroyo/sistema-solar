import sys
from PyQt5 import QtGui, QtWidgets
import planetario


def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = planetario.SolarSystem() #Clase creada en planetario.py

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
