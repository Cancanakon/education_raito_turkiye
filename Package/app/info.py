from PyQt5.QtWidgets import *
from designInfo import Ui_Info
from PyQt5.QtCore import pyqtSignal


class infoPage(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.ui = Ui_Info()
        self.ui.setupUi(self)














