#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from recorddialog.ui on Fri Mar  2 09:11:59 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.recKeyboardButton = QtGui.QCheckBox(Form)
        self.recKeyboardButton.setObjectName(_fromUtf8("recKeyboardButton"))
        self.verticalLayout.addWidget(self.recKeyboardButton)
        self.recMouseButton = QtGui.QCheckBox(Form)
        self.recMouseButton.setObjectName(_fromUtf8("recMouseButton"))
        self.verticalLayout.addWidget(self.recMouseButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.secondsSpinBox = KIntSpinBox(Form)
        self.secondsSpinBox.setProperty("value", 5)
        self.secondsSpinBox.setObjectName(_fromUtf8("secondsSpinBox"))
        self.horizontalLayout.addWidget(self.secondsSpinBox)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.label.setText(kdecore.i18n(_fromUtf8("Record a keyboard/mouse macro")))
        self.recKeyboardButton.setText(kdecore.i18n(_fromUtf8("Record keyboard events")))
        self.recMouseButton.setText(kdecore.i18n(_fromUtf8("Record mouse events (experimental)")))
        self.label_2.setText(kdecore.i18n(_fromUtf8("Start recording after")))
        self.label_3.setText(kdecore.i18n(_fromUtf8("seconds")))

from PyKDE4.kdeui import KIntSpinBox
