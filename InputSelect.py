from PySide2 import QtCore, QtWidgets, QtGui

from InputSelectLayout import Ui_InputSelectDialog
from countunicode import detect_encoding

class InputSelectDialog (QtWidgets.QDialog):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_InputSelectDialog()
        self.ui.setupUi(self)
        #Hide label when no file is selected
        self.ui.filename_display.setText('')
        
        self.ui.browsefiles_button.released.connect(self.get_filename)
        
        available_encoding = [
            'utf-8',
            'utf-16',
            'utf-32',
            'ascii',
            'latin-1',
            'iso-8858-1',
            'use chardet',
        ]
        self.ui.encoding_combobox.addItems(available_encoding)
        
        self.ui.buttonBox.accepted.connect(self.send_input)
        self.ui.buttonBox.rejected.connect(self.close_dialog)

    def get_filename (self):
        """Allow user to select file through QFileDialog"""
        self.selected_filename, _ = QtWidgets.QFileDialog.getOpenFileName(caption='Open text file')
        self.ui.filename_display.setText(self.selected_filename)
    
    def send_input (self):
        self.selected_encoding = self.ui.encoding_combobox.currentText()
        #use a dictionary in __init__ instead if more special cases are needed
        if self.selected_encoding == 'use chardet':
            self.selected_encoding = detect_encoding(self.selected_filename)
        self.accept()
    
    def close_dialog (self):
        self.reject()