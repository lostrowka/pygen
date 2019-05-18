from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QColor
from PySide2.QtWidgets import *

from utils import get_supported_protocols
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
        self.listItems = []

        self.render_view()

        QtCore.QObject.connect(self.pbAddConn, QtCore.SIGNAL('clicked()'), self.add_pkt_flow)

    def render_view(self):
        for proto in get_supported_protocols():
            self.cbProtocols.addItem(proto)

    def add_pkt_flow(self):
        listWidgetItem = QListWidgetItem(self.listWidget)
        listWidgetItem.setBackgroundColor(QColor(240, 240, 240))
        self.listWidget.addItem(listWidgetItem)
        pktFlow = PktFlow(self.destAddress.text(), self.destPort.text(), self.cbProtocols.currentText(), self.message.toPlainText(), self.interval.text())
        listItem = ListItem(listWidgetItem, self.listWidget, pktFlow)
        self.listItems.append(listItem)
        listWidgetItem.setSizeHint(listItem.sizeHint())
        self.listWidget.setItemWidget(listWidgetItem, listItem)

    def closeEvent(self, event):
        for item in self.listItems:
            item.pktFlow.keep_running = False
            item.pktFlow.exit_thread = True
        event.accept()


class ListItem(QWidget):
    def __init__(self, listWidgetItem: QListWidgetItem, parentList: QListWidget, pktFlow: PktFlow):
        super().__init__()
        self.ui = Ui_ListItem()
        self.ui.setupUi(self)
        self.listWidgetItem = listWidgetItem
        self.parentList = parentList
        self.pktFlow = pktFlow
        self.render_view()
        self.pktFlow.start()

    def render_view(self):
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
        self.ui.lInterval.setText("Every " + self.pktFlow.freq + " ms")

    def stop_item(self):
        self.pktFlow.flip_keep_sending()
        if self.pktFlow.keep_running:
            self.ui.pbStop.setText("Stop")
        else:
            self.ui.pbStop.setText("Start")
        pass

    def remove_item(self):
        self.pktFlow.keep_running = False
        self.pktFlow.exit_thread = True
        self.listWidgetItem.setSizeHint(QSize(0,0))
        self.parentList.removeItemWidget(self.listWidgetItem)
