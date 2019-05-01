#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 18:33
# @Author  : duwenzhi
# @Site    :
# @File    : UI_AttendanceSystem_Main.py
# @Software: PyCharm

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):

    def __init__(self):
        self.name_list = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.setGeometry(50, 50, 575, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCamera.setGeometry(QtCore.QRect(220, 540, 93, 28))
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(10, 10, 550, 450))
        self.labelCamera.setObjectName("labelCamera")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别考勤录入界面"))
        self.btnOpenCamera.setText(_translate("MainWindow", "打开摄像头"))


