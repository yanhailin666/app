


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(636, 267)
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.username.setObjectName("label")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(30, 80, 54, 12))
        self.password.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.login_Button = QtWidgets.QPushButton(Form)
        self.login_Button.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.login_Button.setObjectName("pushButton")
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.cancel_Button.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(270, 20, 271, 161))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setText(_translate("Form", "用户名"))
        self.password.setText(_translate("Form", "密码"))
        self.login_Button.setText(_translate("Form", "登录"))
        self.cancel_Button.setText(_translate("Form", "退出"))
