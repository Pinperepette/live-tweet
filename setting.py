# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sun Mar  9 15:07:45 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.setWindowModality(QtCore.Qt.NonModal)
        Settings.resize(500, 400)
        Settings.setMinimumSize(QtCore.QSize(500, 400))
        Settings.setMaximumSize(QtCore.QSize(500, 400))
        self.pushButton = QtGui.QPushButton(Settings)
        self.pushButton.setGeometry(QtCore.QRect(370, 350, 114, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget = QtGui.QWidget(Settings)
        self.widget.setGeometry(QtCore.QRect(20, 30, 461, 291))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label1 = QtGui.QLabel(self.widget)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.lineEdit1 = QtGui.QLineEdit(self.widget)
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.gridLayout.addWidget(self.lineEdit1, 0, 1, 1, 1)
        self.label2 = QtGui.QLabel(self.widget)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        self.lineEdit2 = QtGui.QLineEdit(self.widget)
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.gridLayout.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.label3 = QtGui.QLabel(self.widget)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)
        self.lineEdit3 = QtGui.QLineEdit(self.widget)
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit3"))
        self.gridLayout.addWidget(self.lineEdit3, 2, 1, 1, 1)
        self.label4 = QtGui.QLabel(self.widget)
        self.label4.setObjectName(_fromUtf8("label4"))
        self.gridLayout.addWidget(self.label4, 3, 0, 1, 1)
        self.lineEdit4 = QtGui.QLineEdit(self.widget)
        self.lineEdit4.setObjectName(_fromUtf8("lineEdit4"))
        self.gridLayout.addWidget(self.lineEdit4, 3, 1, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Settings", None))
        self.pushButton.setText(_translate("Settings", "SAVE", None))
        self.label1.setText(_translate("Settings", "OAUTH_TOKEN", None))
        self.label2.setText(_translate("Settings", "OAUTH_SECRET", None))
        self.label3.setText(_translate("Settings", "APP_KEY", None))
        self.label4.setText(_translate("Settings", "APP_SECRET", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Settings = QtGui.QWidget()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

