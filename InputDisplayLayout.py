# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputDisplayLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_InputDisplayWindow(object):
    def setupUi(self, InputDisplayWindow):
        InputDisplayWindow.setObjectName("InputDisplayWindow")
        InputDisplayWindow.resize(561, 536)
        self.input_display = QtWidgets.QTextBrowser(InputDisplayWindow)
        self.input_display.setGeometry(QtCore.QRect(10, 10, 361, 511))
        self.input_display.setObjectName("input_display")

        self.retranslateUi(InputDisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(InputDisplayWindow)

    def retranslateUi(self, InputDisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        InputDisplayWindow.setWindowTitle(_translate("InputDisplayWindow", "Input display"))
