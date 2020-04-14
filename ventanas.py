import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

style_text_edit = '.QTextEdit{ border-color: black; border-style: solid; background-color: black; color: white; }'

style_button = '.QPushButton{ border-color: white; border-style: solid; border-radius: 3px; border-width: 2px;' \
               ' background-color: #D0D0D0; color: black }' \
               '.QPushButton:hover{ background-color: #505050; color: white }'


class WinSun(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinSun, self).__init__()
        uic.loadUi('GUI/sunGUI.ui', self)
        self.setWindowTitle('El Sol')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/sun.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinMoon(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinMoon, self).__init__()
        uic.loadUi('GUI/moonGUI.ui', self)
        self.setWindowTitle('La Luna')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/moon.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinMercury(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinMercury, self).__init__()
        uic.loadUi('GUI/mercuryGUI.ui', self)
        self.setWindowTitle('Mercurio')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/mercury.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinVenus(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinVenus, self).__init__()
        uic.loadUi('GUI/venusGUI.ui', self)
        self.setWindowTitle('Venus')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/venus.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinEarth(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinEarth, self).__init__()
        uic.loadUi('GUI/earthGUI.ui', self)
        self.setWindowTitle('Tierra')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/earth.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinMars(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinMars, self).__init__()
        uic.loadUi('GUI/marsGUI.ui', self)
        self.setWindowTitle('Marte')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/mars.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinJupiter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinJupiter, self).__init__()
        uic.loadUi('GUI/jupiterGUI.ui', self)
        self.setWindowTitle('Jupiter')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/jupiter.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinSaturn(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinSaturn, self).__init__()
        uic.loadUi('GUI/saturnGUI.ui', self)
        self.setWindowTitle('Saturno')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/saturn.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinUranus(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinUranus, self).__init__()
        uic.loadUi('GUI/uranusGUI.ui', self)
        self.setWindowTitle('Urano')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/uranus.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()


class WinNeptune(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WinNeptune, self).__init__()
        uic.loadUi('GUI/neptuneGUI.ui', self)
        self.setWindowTitle('Neptuno')
        self.setWindowIcon(QtGui.QIcon('GUI/Iconos/neptune.png'))

        self.text_info.setStyleSheet(style_text_edit)
        self.text_facts.setStyleSheet(style_text_edit)

        self.button_close.setStyleSheet(style_button)

        self.button_close.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.close()
