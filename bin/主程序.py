from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog
from QT设计.bin import 爪巴虫主界面
from QT设计.bin import 爪巴虫传输队列
from QT设计.bin import 爪巴虫收藏夹
from QT设计.bin import 爪巴虫视频索引
import sys
class mainPro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = 爪巴虫主界面.Ui_Dialog()
        self.ui.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=mainPro()
    w.show()
    sys.exit(app.exec_())