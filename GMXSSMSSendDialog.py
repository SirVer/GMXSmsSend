# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GMXSSMSSendDialog.ui'
#
# Created: Mon Sep 28 20:26:01 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GMXSMSSendDialog(object):
    def setupUi(self, GMXSMSSendDialog):
        GMXSMSSendDialog.setObjectName("GMXSMSSendDialog")
        GMXSMSSendDialog.resize(400, 543)
        self.centralwidget = QtGui.QWidget(GMXSMSSendDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberEdit = QtGui.QLineEdit(self.centralwidget)
        self.numberEdit.setObjectName("numberEdit")
        self.horizontalLayout.addWidget(self.numberEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.textEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nCharsLabel = QtGui.QLabel(self.centralwidget)
        self.nCharsLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.nCharsLabel.setObjectName("nCharsLabel")
        self.gridLayout.addWidget(self.nCharsLabel, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.nSmsLabel = QtGui.QLabel(self.centralwidget)
        self.nSmsLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.nSmsLabel.setObjectName("nSmsLabel")
        self.gridLayout.addWidget(self.nSmsLabel, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(250, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(369, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setMinimumSize(QtCore.QSize(250, 0))
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_2.addWidget(self.statusLabel, 0, 0, 1, 1)
        self.remainingSmsLabel = QtGui.QLabel(self.centralwidget)
        self.remainingSmsLabel.setObjectName("remainingSmsLabel")
        self.gridLayout_2.addWidget(self.remainingSmsLabel, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setEnabled(False)
        self.sendButton.setDefault(True)
        self.sendButton.setFlat(False)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_2.addWidget(self.sendButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        GMXSMSSendDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GMXSMSSendDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        self.menuGeneral = QtGui.QMenu(self.menubar)
        self.menuGeneral.setObjectName("menuGeneral")
        GMXSMSSendDialog.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GMXSMSSendDialog)
        self.statusbar.setObjectName("statusbar")
        GMXSMSSendDialog.setStatusBar(self.statusbar)
        self.menuClose = QtGui.QAction(GMXSMSSendDialog)
        self.menuClose.setObjectName("menuClose")
        self.menuGeneral.addAction(self.menuClose)
        self.menubar.addAction(self.menuGeneral.menuAction())
        self.label.setBuddy(self.numberEdit)
        self.label_2.setBuddy(self.textEdit)

        self.retranslateUi(GMXSMSSendDialog)
        QtCore.QMetaObject.connectSlotsByName(GMXSMSSendDialog)

    def retranslateUi(self, GMXSMSSendDialog):
        GMXSMSSendDialog.setWindowTitle(QtGui.QApplication.translate("GMXSMSSendDialog", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "Text:", None, QtGui.QApplication.UnicodeUTF8))
        self.nCharsLabel.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "Anzahl SMS:", None, QtGui.QApplication.UnicodeUTF8))
        self.nSmsLabel.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "Zeichen:", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "Senden", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGeneral.setTitle(QtGui.QApplication.translate("GMXSMSSendDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClose.setText(QtGui.QApplication.translate("GMXSMSSendDialog", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClose.setShortcut(QtGui.QApplication.translate("GMXSMSSendDialog", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))

