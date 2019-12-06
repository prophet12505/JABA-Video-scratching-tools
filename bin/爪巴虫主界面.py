# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '爪巴虫主界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from QT设计.bin import 爪巴虫主界面
from QT设计.bin import 爪巴虫传输队列
from QT设计.bin import 爪巴虫收藏夹
from QT设计.bin import 爪巴虫视频索引
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1113, 607)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(780, 280, 91, 61))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 290, 551, 41))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 230, 381, 41))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(170, 380, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 410, 191, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(360, 560, 321, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 560, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 560, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(160, 30, 711, 192))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 30, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 80, 101, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 30, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(940, 130, 101, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(870, 390, 222, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 560, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(870, 430, 222, 48))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(870, 470, 222, 48))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.open)
        self.pushButton_3.clicked.connect(Dialog.open)
        self.pushButton_4.clicked.connect(Dialog.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "爪巴虫"))
        self.pushButton.setText(_translate("Dialog", "Go！"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "输入网页解析视频"))
        self.radioButton.setText(_translate("Dialog", "自动播放"))
        self.radioButton_2.setText(_translate("Dialog", "自动下载（默认格式）"))
        self.label_2.setText(_translate("Dialog", "当前进度"))
        self.pushButton_2.setText(_translate("Dialog", "传输列表"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "资源列表"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "https://www.bilibili.com/video/av53058902/?spm_id_from=333.788.videocard.2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "https://www.bilibili.com/video/av64782935?from=search&seid=18248374077827849254"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("Dialog", "加入收藏夹"))
        self.pushButton_4.setText(_translate("Dialog", "索引"))
        self.pushButton_5.setText(_translate("Dialog", "打开收藏夹"))
        self.pushButton_6.setText(_translate("Dialog", "删除"))
        self.commandLinkButton.setText(_translate("Dialog", "帮助"))
        self.pushButton_7.setText(_translate("Dialog", "下载器设置"))
        self.commandLinkButton_2.setText(_translate("Dialog", "联系我们"))
        self.commandLinkButton_3.setText(_translate("Dialog", "MOOC资源库"))



