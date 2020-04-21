import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtMultimedia
import windows

style_button =  '.QPushButton{ border-color: black; border-style: solid; border-radius:'\
                '3px; border-width: 2px; background-color: #101010; color: white }'\
                '.QPushButton:hover{ background-color: #505050; color: black }' #CSS styles

bg_color = QtGui.QPalette()
bg_color.setColor(QtGui.QPalette.Background, QtCore.Qt.black)


class SolarSystem(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SolarSystem, self).__init__()

        uic.loadUi('GUI/_planetsGUI.ui', self)
        self.setWindowTitle('Sistema Solar')
        self.setWindowIcon(QtGui.QIcon('GUI/icons/_icon.png'))

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

        #Eventos. Al ser presionado el botón, se llama a la función correspondiente
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

    def play_chorus(self): #Reproduce el sonido de fondo
        chorus=QtMultimedia.QSound
        chorus.play('GUI/sound/chorus.wav')

    def click_button_sun(self): #Abre la ventana Sol
        self.sun = windows.WinSun()
        self.sun.setPalette(bg_color)
        self.sun.show()

    def click_button_moon(self): #Abre la ventana Luna
        self.moon = windows.WinMoon()
        self.moon.setPalette(bg_color)
        self.moon.show()

    def click_button_mercury(self): #Abre la ventana Mercurio
        self.mercury = windows.WinMercury()
        self.mercury.setPalette(bg_color)
        self.mercury.show()

    def click_button_venus(self): #Abre la ventana Venus
        self.venus = windows.WinVenus()
        self.venus.setPalette(bg_color)
        self.venus.show()

    def click_button_earth(self): #Abre la ventana Tierra
        self.earth = windows.WinEarth()
        self.earth.setPalette(bg_color)
        self.earth.show()

    def click_button_mars(self): #Abre la ventana
        self.mars = windows.WinMars()
        self.mars.setPalette(bg_color)
        self.mars.show()

    def click_button_jupiter(self):
        self.jupiter = windows.WinJupiter()
        self.jupiter.setPalette(bg_color)
        self.jupiter.show()

    def click_button_saturn(self):
        self.saturn = windows.WinSaturn()
        self.saturn.setPalette(bg_color)
        self.saturn.show()

    def click_button_uranus(self):
        self.uranus = windows.WinUranus()
        self.uranus.setPalette(bg_color)
        self.uranus.show()

    def click_button_neptune(self):
        self.neptune = windows.WinNeptune()
        self.neptune.setPalette(bg_color)
        self.neptune.show()
