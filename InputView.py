from PySide2 import QtCore, QtWidgets, QtGui

from InputDisplayLayout import Ui_InputDisplayWindow

class InputDisplayWindow (QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_InputDisplayWindow()
        self.ui.setupUi(self)
        
    def update_display (self, filename):
        self.ui.input_display.clear()
        with open(filename, encoding='utf-8') as file:
            self.ui.input_display.append(file.read())