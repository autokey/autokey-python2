#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from uic/folderpage.ui on Tue Jul 28 14:58:41 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_FolderPage(object):
    def setupUi(self, FolderPage):
        FolderPage.setObjectName("FolderPage")
        FolderPage.resize(568, 530)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FolderPage)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = QtGui.QLabel(FolderPage)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.titleLineEdit = KLineEdit(FolderPage)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.verticalLayout_2.addWidget(self.titleLineEdit)
        self.settingsGroupBox = QtGui.QGroupBox(FolderPage)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showInTrayCheckbox = QtGui.QCheckBox(self.settingsGroupBox)
        self.showInTrayCheckbox.setObjectName("showInTrayCheckbox")
        self.verticalLayout.addWidget(self.showInTrayCheckbox)
        self.kseparator = KSeparator(self.settingsGroupBox)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)
        self.settingsWidget = SettingsWidget(self.settingsGroupBox)
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout.addWidget(self.settingsWidget)
        self.verticalLayout_2.addWidget(self.settingsGroupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(FolderPage)
        QtCore.QMetaObject.connectSlotsByName(FolderPage)

    def retranslateUi(self, FolderPage):
        FolderPage.setWindowTitle(kdecore.i18n("Form"))
        self.titleLabel.setText(kdecore.i18n("Title"))
        self.settingsGroupBox.setTitle(kdecore.i18n("Settings"))
        self.showInTrayCheckbox.setText(kdecore.i18n("Show in tray menu"))

from PyKDE4.kdeui import KSeparator, KLineEdit
from configwindow import SettingsWidget
