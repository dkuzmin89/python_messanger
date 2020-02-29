# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 100, 601, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 440, 301, 61))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 440, 251, 61))
        self.pushButton.setObjectName("pushButton")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(180, 70, 344, 21))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Messenger"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Password"))
