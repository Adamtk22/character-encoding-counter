import sys
from collections import Counter

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
        
        self.inputselect_dialog = InputSelectDialog()
        self.inputdisplay_window = InputDisplayWindow()
        
        self.ui.inputfile_button.released.connect(self.open_inputfile)
        self.ui.inputview_button.released.connect(self.open_inputdisplay)
    
    def closeEvent (self, event):
        self.inputdisplay_window.close()
    
    def open_inputfile (self):
        """open text file and produce output"""
        #self.inputselect_dialog = InputSelectDialog()
        self.inputselect_dialog.exec_()
        self.active_file = self.inputselect_dialog.selected_filename
        self.active_encoding = self.inputselect_dialog.selected_encoding
        if self.active_file and self.active_encoding:
            self.ui.filename_display.setText(self.active_file)
            self.ui.output_display.clear()
            self.inputdisplay_window.ui.input_display.clear()
            self.ui.output_display.append(f'Encoding: {self.active_encoding}')
            char_count = Counter()
            for line in open(self.active_file, 'r', encoding=self.active_encoding):
                self.inputdisplay_window.ui.input_display.insertPlainText(line)
                char_count += count_char(line)
            self.ui.inputview_button.setEnabled(True)
            if char_count:
                self.ui.output_display.append('Character occurences')
                for key, num in char_count.most_common():
                    self.ui.output_display.append(f'{key} : {num}')
                self.ui.output_display.append(f'Total number of characters: {char_count.total()}')
    
    def open_inputdisplay (self):
        """show input display window"""
        self.inputdisplay_window.show()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()