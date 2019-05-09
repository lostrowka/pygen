# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Thu May  9 22:26:52 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(845, 574)
        Main.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cbProtocols = QtWidgets.QComboBox(self.centralwidget)
        self.cbProtocols.setEnabled(True)
        self.cbProtocols.setObjectName("cbProtocols")
        self.gridLayout.addWidget(self.cbProtocols, 0, 1, 1, 1)
        self.leDestPort = QtWidgets.QLineEdit(self.centralwidget)
        self.leDestPort.setObjectName("leDestPort")
        self.gridLayout.addWidget(self.leDestPort, 2, 1, 1, 1)
        self.leInterval = QtWidgets.QLineEdit(self.centralwidget)
        self.leInterval.setObjectName("leInterval")
        self.gridLayout.addWidget(self.leInterval, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pbAddConn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAddConn.sizePolicy().hasHeightForWidth())
        self.pbAddConn.setSizePolicy(sizePolicy)
        self.pbAddConn.setMinimumSize(QtCore.QSize(200, 0))
        self.pbAddConn.setAutoFillBackground(False)
        self.pbAddConn.setObjectName("pbAddConn")
        self.gridLayout.addWidget(self.pbAddConn, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.leDestAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.leDestAddress.setObjectName("leDestAddress")
        self.gridLayout.addWidget(self.leDestAddress, 1, 1, 1, 1)
        self.teMessage = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teMessage.sizePolicy().hasHeightForWidth())
        self.teMessage.setSizePolicy(sizePolicy)
        self.teMessage.setMinimumSize(QtCore.QSize(0, 100))
        self.teMessage.setMaximumSize(QtCore.QSize(16777215, 100))
        self.teMessage.setObjectName("teMessage")
        self.gridLayout.addWidget(self.teMessage, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pktFlowView = QtWidgets.QListWidget(self.centralwidget)
        self.pktFlowView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.pktFlowView.setObjectName("pktFlowView")
        self.verticalLayout_2.addWidget(self.pktFlowView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        Main.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtWidgets.QApplication.translate("Main", "PyGen", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Main", "Interval", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Main", "Data message", None, -1))
        self.pbAddConn.setText(QtWidgets.QApplication.translate("Main", "Create Generator Task", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Main", "Destination address", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Main", "Destination port", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Main", "Protocol", None, -1))

