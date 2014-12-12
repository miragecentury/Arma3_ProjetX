__author__ = 'victorien.vanroye@gmail.com'

import sys
from PySide import QtGui

from BPC.ProjetX.Service.Log import Logger
from BPC.ProjetX.DeployManager.MainWindow import Ui_MainWindow


class DeployManager():
    def __init__(self):
        self.logger = Logger()
        self.qtApp = QtGui.QApplication(sys.argv)
        self.mainWindow = QtGui.QMainWindow()
        Ui_MainWindow_inst = Ui_MainWindow()
        Ui_MainWindow_inst.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.qtApp.exec_()