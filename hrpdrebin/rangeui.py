# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/range.ui'
#
# Created: Sun Nov 10 23:24:02 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

try:
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets
except:
    from PySide import QtCore, QtWidgets

class Ui_range_dialog(object):
    def setupUi(self, range_dialog):
        range_dialog.setObjectName("range_dialog")
        range_dialog.resize(531, 133)
        self.buttonBox = QtWidgets.QDialogButtonBox(range_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 80, 471, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(range_dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 66, 21))
        self.label.setObjectName("label")
        self.range_edit = QtWidgets.QLineEdit(range_dialog)
        self.range_edit.setGeometry(QtCore.QRect(110, 20, 391, 41))
        self.range_edit.setObjectName("range_edit")

        self.retranslateUi(range_dialog)
        self.buttonBox.accepted.connect(range_dialog.accept)
        self.buttonBox.rejected.connect(range_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(range_dialog)

    def retranslateUi(self, range_dialog):
        range_dialog.setWindowTitle(QtWidgets.QApplication.translate("range_dialog", "Add scans by numbers", None))
        self.label.setText(QtWidgets.QApplication.translate("range_dialog", "Scan list:", None))
        self.range_edit.setToolTip(QtWidgets.QApplication.translate("range_dialog", "<html><head/><body><p>Enter scan numbers as comma separated list. Ranges can be include using a dash (or minus symbol).</p><p><br/></p><p>The files will be found using the DLS info and the directories of any scan files already added</p><p><br/></p></body></html>", None))

