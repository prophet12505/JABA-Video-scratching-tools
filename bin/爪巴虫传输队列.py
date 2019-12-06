# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '爪巴虫传输队列.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from QT设计.bin import 爪巴虫主界面
from QT设计.bin import 爪巴虫传输队列
from QT设计.bin import 爪巴虫收藏夹
from QT设计.bin import 爪巴虫视频索引

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(598, 329)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 431, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 120, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 170, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "爪巴虫传输队列"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", " "))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "传输项目"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "传输速度"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "传输进度"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "影流之主.mp4"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Dialog", "3.44Mb/s"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Dialog", "  86%"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog", "奥利给.mp4"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Dialog", "0Mb/s"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Dialog", "0%"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "取消任务"))
        self.pushButton_2.setText(_translate("Dialog", "暂停"))
        self.pushButton_3.setText(_translate("Dialog", "暂停全部"))
