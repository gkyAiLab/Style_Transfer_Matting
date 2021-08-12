# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\player_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtWidgetsApplication_hello_worldClass(object):
    def setupUi(self, QtWidgetsApplication_hello_worldClass):
        QtWidgetsApplication_hello_worldClass.setObjectName("QtWidgetsApplication_hello_worldClass")
        QtWidgetsApplication_hello_worldClass.resize(1307, 773)
        self.centralWidget = QtWidgets.QWidget(QtWidgetsApplication_hello_worldClass)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1070, 510, 221, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 510, 1061, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1281, 431))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        QtWidgetsApplication_hello_worldClass.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(QtWidgetsApplication_hello_worldClass)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1307, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuBegin = QtWidgets.QMenu(self.menuBar)
        self.menuBegin.setObjectName("menuBegin")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        QtWidgetsApplication_hello_worldClass.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(QtWidgetsApplication_hello_worldClass)
        self.mainToolBar.setObjectName("mainToolBar")
        QtWidgetsApplication_hello_worldClass.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(QtWidgetsApplication_hello_worldClass)
        self.statusBar.setObjectName("statusBar")
        QtWidgetsApplication_hello_worldClass.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuBegin.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.mainToolBar.addSeparator()

        self.retranslateUi(QtWidgetsApplication_hello_worldClass)
        QtCore.QMetaObject.connectSlotsByName(QtWidgetsApplication_hello_worldClass)

    def retranslateUi(self, QtWidgetsApplication_hello_worldClass):
        _translate = QtCore.QCoreApplication.translate
        QtWidgetsApplication_hello_worldClass.setWindowTitle(_translate("QtWidgetsApplication_hello_worldClass", "QtWidgetsApplication_hello_world"))
        self.label.setText(_translate("QtWidgetsApplication_hello_worldClass", "TextLabel"))
        self.label_2.setText(_translate("QtWidgetsApplication_hello_worldClass", "TextLabel"))
        self.menuBegin.setTitle(_translate("QtWidgetsApplication_hello_worldClass", "Begin"))
        self.menuHelp.setTitle(_translate("QtWidgetsApplication_hello_worldClass", "Help"))
# import QtWidgetsApplication_hello_world_rc
