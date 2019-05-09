# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_item.ui',
# licensing of 'list_item.ui' applies.
#
# Created: Thu May  9 22:26:51 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ListItem(object):
    def setupUi(self, ListItem):
        ListItem.setObjectName("ListItem")
        ListItem.resize(400, 124)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ListItem)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lInterval = QtWidgets.QLabel(ListItem)
        self.lInterval.setObjectName("lInterval")
        self.gridLayout_2.addWidget(self.lInterval, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lAddress = QtWidgets.QLabel(ListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lAddress.sizePolicy().hasHeightForWidth())
        self.lAddress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lAddress.setFont(font)
        self.lAddress.setObjectName("lAddress")
        self.horizontalLayout.addWidget(self.lAddress)
        self.lProto = QtWidgets.QLabel(ListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lProto.sizePolicy().hasHeightForWidth())
        self.lProto.setSizePolicy(sizePolicy)
        self.lProto.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lProto.setFont(font)
        self.lProto.setObjectName("lProto")
        self.horizontalLayout.addWidget(self.lProto)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.lMessage = QtWidgets.QLabel(ListItem)
        self.lMessage.setObjectName("lMessage")
        self.gridLayout_2.addWidget(self.lMessage, 2, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pbStop = QtWidgets.QPushButton(ListItem)
        self.pbStop.setObjectName("pbStop")
        self.verticalLayout_5.addWidget(self.pbStop)
        self.pbDelete = QtWidgets.QPushButton(ListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbDelete.sizePolicy().hasHeightForWidth())
        self.pbDelete.setSizePolicy(sizePolicy)
        self.pbDelete.setObjectName("pbDelete")
        self.verticalLayout_5.addWidget(self.pbDelete)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ListItem)
        QtCore.QMetaObject.connectSlotsByName(ListItem)

    def retranslateUi(self, ListItem):
        ListItem.setWindowTitle(QtWidgets.QApplication.translate("ListItem", "Form", None, -1))
        self.lInterval.setText(QtWidgets.QApplication.translate("ListItem", "lInterval", None, -1))
        self.lAddress.setText(QtWidgets.QApplication.translate("ListItem", "lAddress", None, -1))
        self.lProto.setText(QtWidgets.QApplication.translate("ListItem", "lProto", None, -1))
        self.lMessage.setText(QtWidgets.QApplication.translate("ListItem", "lMessage", None, -1))
        self.pbStop.setText(QtWidgets.QApplication.translate("ListItem", "Stop", None, -1))
        self.pbDelete.setText(QtWidgets.QApplication.translate("ListItem", "Delete", None, -1))

