from PySide2 import QtCore, QtWidgets, QtGui

from InputDisplayLayout import Ui_InputDisplayWindow

class InputDisplayWindow (QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_InputDisplayWindow()
        self.ui.setupUi(self)