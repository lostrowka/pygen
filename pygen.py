import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication

from gui import *
from utils import gui_print

if __name__ == '__main__':
    gui_print("pygen starting")

    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    gui = PyGenMainUi()

    app.exec_()
