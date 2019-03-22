from PySide2.QtCore import QFile, QObject
from PySide2.QtUiTools import QUiLoader


class PyGenMainUi(QObject):
    def __init__(self):
        super(PyGenMainUi, self).__init__(None)

        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)

        self.mwPyGen = QUiLoader().load(ui_file)
        ui_file.close()
        self.mwPyGen.show()
