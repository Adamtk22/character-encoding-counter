from PySide2 import QtCore, QtWidgets, QtGui

from InputSelectLayout import Ui_InputSelectDialog

class InputSelectDialog (QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_InputSelectDialog()
        self.ui.setupUi(self)
        #Hide label when no file is selected
        self.ui.filename_display.setText('')
        
    def reject (self):
        pass
    
    def open (self):
        pass