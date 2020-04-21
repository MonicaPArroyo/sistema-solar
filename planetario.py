import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtMultimedia #, phonon
import ventanas



style_button = '.QPushButton{ border-color: black; border-style: solid; border-radius: 3px; border-width: 2px; background-color: #101010; color: white }.QPushButton:hover{ background-color: #505050; color: black }' #Estilos CSS para el botón

bg_color = QtGui.QPalette()
bg_color.setColor(QtGui.QPalette.Background, QtCore.Qt.black)


class SolarSystem(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SolarSystem, self).__init__()

        uic.loadUi('GUI/_planetsGUI.ui', self)
        self.setWindowTitle('Sistema Solar')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/_icon.png'))

        self.button_sun.setStyleSheet(style_button)
        self.button_moon.setStyleSheet(style_button)

        self.button_mercury.setStyleSheet(style_button)
        self.button_venus.setStyleSheet(style_button)
        self.button_earth.setStyleSheet(style_button)
        self.button_mars.setStyleSheet(style_button)
        self.button_jupiter.setStyleSheet(style_button)
        self.button_saturn.setStyleSheet(style_button)
        self.button_uranus.setStyleSheet(style_button)
        self.button_neptune.setStyleSheet(style_button)

        #Eventos
        self.button_sun.clicked.connect(self.click_button_sun)
        self.button_moon.clicked.connect(self.click_button_moon)

        self.button_mercury.clicked.connect(self.click_button_mercury)
        self.button_venus.clicked.connect(self.click_button_venus)
        self.button_earth.clicked.connect(self.click_button_earth)
        self.button_mars.clicked.connect(self.click_button_mars)
        self.button_jupiter.clicked.connect(self.click_button_jupiter)
        self.button_saturn.clicked.connect(self.click_button_saturn)
        self.button_uranus.clicked.connect(self.click_button_uranus)
        self.button_neptune.clicked.connect(self.click_button_neptune)

        self.play_chorus()

        self.show()

    def play_chorus(self):
        chorus=QtMultimedia.QSound
        chorus.play('GUI/Audio/chorus.wav')

    def click_button_sun(self):
        self.sun = ventanas.WinSun()
        self.sun.setPalette(bg_color)
        self.sun.show()

    def click_button_moon(self):
        self.moon = ventanas.WinMoon()
        self.moon.setPalette(bg_color)
        self.moon.show()

    def click_button_mercury(self):
        self.mercury = ventanas.WinMercury()
        self.mercury.setPalette(bg_color)
        self.mercury.show()

    def click_button_venus(self):
        self.venus = ventanas.WinVenus()
        self.venus.setPalette(bg_color)
        self.venus.show()

    def click_button_earth(self):
        self.earth = ventanas.WinEarth()
        self.earth.setPalette(bg_color)
        self.earth.show()

    def click_button_mars(self):
        self.mars = ventanas.WinMars()
        self.mars.setPalette(bg_color)
        self.mars.show()

    def click_button_jupiter(self):
        self.jupiter = ventanas.WinJupiter()
        self.jupiter.setPalette(bg_color)
        self.jupiter.show()

    def click_button_saturn(self):
        self.saturn = ventanas.WinSaturn()
        self.saturn.setPalette(bg_color)
        self.saturn.show()

    def click_button_uranus(self):
        self.uranus = ventanas.WinUranus()
        self.uranus.setPalette(bg_color)
        self.uranus.show()

    def click_button_neptune(self):
        self.neptune = ventanas.WinNeptune()
        self.neptune.setPalette(bg_color)
        self.neptune.show()
