# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/Pinguino/pinguino-ide/qtgui/gide/bloques/nested/nested.ui'
#
# Created: Sun Dec 22 10:37:14 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(94, 84)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(38, 46))
        self.frame.setMaximumSize(QtCore.QSize(38, 46))
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 46))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setMinimumSize(QtCore.QSize(6, 46))
        self.frame_3.setMaximumSize(QtCore.QSize(6, 46))
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)
        self.frame_4 = QtGui.QFrame(Form)
        self.frame_4.setMinimumSize(QtCore.QSize(11, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(11, 16777215))
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_5 = QtGui.QFrame(Form)
        self.frame_5.setMinimumSize(QtCore.QSize(42, 16))
        self.frame_5.setMaximumSize(QtCore.QSize(42, 16))
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtGui.QLabel(self.frame_5)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

