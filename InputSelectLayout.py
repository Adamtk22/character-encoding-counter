# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputSelectLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_InputSelectDialog(object):
    def setupUi(self, InputSelectDialog):
        InputSelectDialog.setObjectName("InputSelectDialog")
        InputSelectDialog.resize(429, 291)
        self.buttonBox = QtWidgets.QDialogButtonBox(InputSelectDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 361, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.selectfile_label = QtWidgets.QLabel(InputSelectDialog)
        self.selectfile_label.setGeometry(QtCore.QRect(30, 40, 47, 21))
        self.selectfile_label.setObjectName("selectfile_label")
        self.browsefiles_button = QtWidgets.QPushButton(InputSelectDialog)
        self.browsefiles_button.setGeometry(QtCore.QRect(110, 40, 75, 23))
        self.browsefiles_button.setObjectName("browsefiles_button")
        self.filename_display = QtWidgets.QLabel(InputSelectDialog)
        self.filename_display.setGeometry(QtCore.QRect(30, 80, 361, 16))
        self.filename_display.setObjectName("filename_display")
        self.encoding_label = QtWidgets.QLabel(InputSelectDialog)
        self.encoding_label.setGeometry(QtCore.QRect(30, 130, 47, 21))
        self.encoding_label.setObjectName("encoding_label")
        self.encoding_combobox = QtWidgets.QComboBox(InputSelectDialog)
        self.encoding_combobox.setGeometry(QtCore.QRect(110, 130, 131, 22))
        self.encoding_combobox.setObjectName("encoding_combobox")

        self.retranslateUi(InputSelectDialog)
        QtCore.QMetaObject.connectSlotsByName(InputSelectDialog)

    def retranslateUi(self, InputSelectDialog):
        _translate = QtCore.QCoreApplication.translate
        InputSelectDialog.setWindowTitle(_translate("InputSelectDialog", "Select file"))
        self.selectfile_label.setText(_translate("InputSelectDialog", "Select file"))
        self.browsefiles_button.setText(_translate("InputSelectDialog", "Browse files"))
        self.filename_display.setText(_translate("InputSelectDialog", "TextLabel"))
        self.encoding_label.setText(_translate("InputSelectDialog", "Encoding"))
