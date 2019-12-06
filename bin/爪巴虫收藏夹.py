# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '爪巴虫收藏夹.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from QT设计.bin import 爪巴虫主界面
from QT设计.bin import 爪巴虫传输队列
from QT设计.bin import 爪巴虫收藏夹
from QT设计.bin import 爪巴虫视频索引

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(dialog)
        self.listWidget.setGeometry(QtCore.QRect(80, 60, 256, 192))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(252, 260, 121, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "收藏夹"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("dialog", "https://www.bilibili.com/video/av53058902/?spm_id_from=333.788.videocard.2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("dialog", "加入解析队列"))
