# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Dec 12 22:02:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuProjet = QtGui.QMenu(self.menubar)
        self.menuProjet.setObjectName("menuProjet")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreer = QtGui.QAction(MainWindow)
        self.actionCreer.setObjectName("actionCreer")
        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.menuProjet.addAction(self.actionCreer)
        self.menuProjet.addAction(self.actionOuvrir)
        self.menubar.addAction(self.menuProjet.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Black Pony Company // ProjetX // Deploy Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProjet.setTitle(QtGui.QApplication.translate("MainWindow", "Projet", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreer.setText(QtGui.QApplication.translate("MainWindow", "Creer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuvrir.setText(QtGui.QApplication.translate("MainWindow", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))

