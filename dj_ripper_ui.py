# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dj_ripper.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.filePathDisplay = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.filePathDisplay.setObjectName("filePathDisplay")
        self.horizontalLayout.addWidget(self.filePathDisplay)
        self.ripButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ripButton.setStyleSheet("")
        self.ripButton.setObjectName("ripButton")
        self.horizontalLayout.addWidget(self.ripButton)
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(20, 411, 761, 131))
        self.console.setObjectName("console")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 761, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.metaDataConfigArea = QtWidgets.QWidget()
        self.metaDataConfigArea.setGeometry(QtCore.QRect(0, 0, 759, 309))
        self.metaDataConfigArea.setObjectName("metaDataConfigArea")
        self.scrollArea.setWidget(self.metaDataConfigArea)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 421, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.destButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.destButton.setObjectName("destButton")
        self.horizontalLayout_2.addWidget(self.destButton)
        self.destPathDisplay = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.destPathDisplay.setObjectName("destPathDisplay")
        self.horizontalLayout_2.addWidget(self.destPathDisplay)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.browseButton.clicked.connect(MainWindow.browseButtonHandler) # type: ignore
        self.ripButton.clicked.connect(MainWindow.ripButtonHandler) # type: ignore
        self.destButton.clicked.connect(MainWindow.destButtonHandler) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.ripButton.setText(_translate("MainWindow", "Rip"))
        self.destButton.setText(_translate("MainWindow", "Dest"))
