# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/anthony/repo/migrate2yt/resources/views/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.link_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.link_txt.setObjectName("link_txt")
        self.verticalLayout_2.addWidget(self.link_txt)
        self.link_btn = QtWidgets.QPushButton(self.centralwidget)
        self.link_btn.setObjectName("link_btn")
        self.verticalLayout_2.addWidget(self.link_btn)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.streaming_cb = QtWidgets.QComboBox(self.centralwidget)
        self.streaming_cb.setObjectName("streaming_cb")
        self.verticalLayout.addWidget(self.streaming_cb)
        self.streaming_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.streaming_login_btn.setObjectName("streaming_login_btn")
        self.verticalLayout.addWidget(self.streaming_login_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.link_result_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.link_result_tablewidget.setObjectName("link_result_tablewidget")
        self.link_result_tablewidget.setColumnCount(0)
        self.link_result_tablewidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.link_result_tablewidget)
        self.link_like_btn = QtWidgets.QPushButton(self.centralwidget)
        self.link_like_btn.setObjectName("link_like_btn")
        self.verticalLayout_3.addWidget(self.link_like_btn)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.link_btn.setText(_translate("MainWindow", "추가"))
        self.streaming_login_btn.setText(_translate("MainWindow", "로그인"))
        self.link_like_btn.setText(_translate("MainWindow", "go"))


from app import resources_rc
