# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_del_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form_del_user(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 234)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 131, 21))
        self.label.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.pushButton_put = QtWidgets.QPushButton(Form)
        self.pushButton_put.setGeometry(QtCore.QRect(190, 180, 93, 28))
        self.pushButton_put.setObjectName("pushButton_put")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 50, 291, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_user.setEnabled(True)
        self.lineEdit_user.setFrame(True)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.gridLayout.addWidget(self.lineEdit_user, 0, 1, 1, 1)
        self.label_user = QtWidgets.QLabel(self.layoutWidget)
        self.label_user.setStyleSheet("font: 10pt \"Arial\";")
        self.label_user.setObjectName("label_user")
        self.gridLayout.addWidget(self.label_user, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "删除用户名"))
        self.pushButton_put.setText(_translate("Form", "提交"))
        self.label_user.setText(_translate("Form", "用户名"))
