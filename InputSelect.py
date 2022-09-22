from PySide2 import QtCore, QtWidgets, QtGui

from InputSelectLayout import Ui_InputSelectDialog

class InputSelectDialog (QtWidgets.QDialog):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_InputSelectDialog()
        self.ui.setupUi(self)
        #Hide label when no file is selected
        self.ui.filename_display.setText('')
        self.ui.buttonBox.accepted.connect(self.send_input)
        self.ui.buttonBox.rejected.connect(self.close_dialog)
        
        self.ui.browsefiles_button.released.connect(self.get_filename)
    
    def get_filename (self):
        """Allow user to select file through QFileDialog"""
        self.selected_filename, _ = QtWidgets.QFileDialog.getOpenFileName(caption='Open text file')
        self.ui.filename_display.setText(self.selected_filename)
    
    def send_input (self):
        self.accept()
    
    def close_dialog (self):
        self.reject()