# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '爪巴虫视频索引.ui'
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
        Dialog.resize(702, 466)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(60, 31, 531, 381))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(600, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 130, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "视频索引"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "视频索引"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "页面资源"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Dialog", "1"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Dialog", "2"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "页面链接"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Dialog", "1"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("Dialog", "页面资源"))
        self.treeWidget.topLevelItem(1).child(0).child(0).child(0).setText(0, _translate("Dialog", "1"))
        self.treeWidget.topLevelItem(1).child(0).child(0).child(1).setText(0, _translate("Dialog", "2"))
        self.treeWidget.topLevelItem(1).child(0).child(0).child(2).setText(0, _translate("Dialog", "3"))
        self.treeWidget.topLevelItem(1).child(0).child(1).setText(0, _translate("Dialog", "页面链接"))
        self.treeWidget.topLevelItem(1).child(0).child(1).child(0).setText(0, _translate("Dialog", "1"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Dialog", "2"))
        self.treeWidget.topLevelItem(1).child(1).child(0).setText(0, _translate("Dialog", "页面资源"))
        self.treeWidget.topLevelItem(1).child(1).child(1).setText(0, _translate("Dialog", "页面链接"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "播放"))
        self.pushButton_2.setText(_translate("Dialog", "下载"))
