import sys

#from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PySide2 import QtCore, QtGui, QtWidgets

from countunicode import count_char
from MainWindowLayout import Ui_MainWindow
from InputView import InputDisplayWindow
from InputSelect import InputSelectDialog

class MainWindow (QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        self.active_file = None
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        #Hide filename when no file is opened
        self.ui.filename_display.setText('')
        
        self.inputdisplay_window = InputDisplayWindow()
        
        self.ui.inputfile_button.released.connect(self.open_inputfile)
        self.ui.inputview_button.released.connect(self.open_inputdisplay)

    def open_inputfile (self):
        """open file as text and produce output"""
        self.inputselect_dialog = InputSelectDialog()
        self.inputselect_dialog.exec_()
        self.active_file = self.inputselect_dialog.selected_filename
        if self.active_file:
            self.inputdisplay_window.update_display(self.active_file)
            self.ui.inputview_button.setEnabled(True)
            self.ui.filename_display.setText(self.active_file)
            self.ui.output_display.clear()
            char_count = count_char(self.active_file)
            if char_count:
                self.ui.output_display.append('Character occurences')
                total_char = 0
                for key, num in char_count:
                    self.ui.output_display.append(f'{key} : {num}')
                    total_char += num
                self.ui.output_display.append(f'Total number of characters: {total_char}')

    def open_inputdisplay (self):
        """show input display window"""
        self.inputdisplay_window.show()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()