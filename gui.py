from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QColor
from PySide2.QtWidgets import *

from utils import gui_print, get_supported_protocols
from list_item import Ui_ListItem
from main import Ui_Main
from net import PktFlow


class PyGenMainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.cbProtocols = self.ui.cbProtocols
        self.pbAddConn = self.ui.pbAddConn
        self.statusBar = self.ui.statusBar
        self.destAddress = self.ui.leDestAddress
        self.destPort = self.ui.leDestPort
        self.listWidget = self.ui.pktFlowView
        self.message = self.ui.teMessage
        self.interval = self.ui.leInterval

        self.render()

        QtCore.QObject.connect(self.pbAddConn, QtCore.SIGNAL('clicked()'), self.add_pkt_flow)

    def render(self):
        for proto in get_supported_protocols():
            self.cbProtocols.addItem(proto)

    def add_pkt_flow(self):
        gui_print("addPktFlow()")

        listWidgetItem = QListWidgetItem(self.listWidget)
        listWidgetItem.setBackgroundColor(QColor(240, 240, 240))
        self.listWidget.addItem(listWidgetItem)
        pktFlow = PktFlow(self.destAddress.text(), self.destPort.text(), self.cbProtocols.currentText(), self.message.toPlainText(), self.interval.text())
        listItem = ListItem(listWidgetItem, self.listWidget, pktFlow)
        listWidgetItem.setSizeHint(listItem.sizeHint())
        self.listWidget.setItemWidget(listWidgetItem, listItem)


class ListItem(QWidget):
    def __init__(self, listWidgetItem: QListWidgetItem, parentList: QListWidget, pktFlow: PktFlow):
        super().__init__()
        self.ui = Ui_ListItem()
        self.ui.setupUi(self)
        gui_print("ListItem __init__()")
        self.listWidgetItem = listWidgetItem
        self.parentList = parentList
        self.pktFlow = pktFlow
        self.render_view()

    def render_view(self):
        gui_print("render()")
        QtCore.QObject.connect(self.ui.pbStop, QtCore.SIGNAL('clicked()'), self.stop_item)
        QtCore.QObject.connect(self.ui.pbDelete, QtCore.SIGNAL('clicked()'), self.remove_item)
        self.ui.lAddress.setText(self.pktFlow.dest)
        if self.pktFlow.dest_port != "":
            self.ui.lAddress.setText(self.pktFlow.dest + ":" + self.pktFlow.dest_port)
        self.ui.lProto.setText(self.pktFlow.proto.name)
        if self.pktFlow.data == "":
            self.ui.lMessage.setText("No message specified")
        else:
            self.ui.lMessage.setText(self.pktFlow.data)
        self.ui.lInterval.setText(self.pktFlow.freq)

    def stop_item(self):
        # TODO: Implement
        pass

    def remove_item(self):
        # TODO: Finish implementation
        self.listWidgetItem.setSizeHint(QSize(0,0))
        self.parentList.removeItemWidget(self.listWidgetItem)
