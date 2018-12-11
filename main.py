# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtWidgets, QtCore
from Rental import Ui_MainWindow
import sys
import os
import time
from socket import *


class mydesignershow(QtWidgets.QMainWindow, QtWidgets.QListWidget):

    def __init__(self):
        super(mydesignershow, self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)

        # 给鼠标重写函数初始化一个参数self._move_drag
        self._move_drag = False

    # 重写鼠标事件
    def mousePressEvent(self, event):
        # 鼠标左键点击标题栏区域
        if (event.button() == QtCore.Qt.LeftButton) and \
                (event.y() < 35) and \
                (event.x() < 1064)and \
                (event.x() > 0):
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if QtCore.Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，扳机复位
        self._move_drag = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = mydesignershow()
    myshow.show()
    sys.exit(app.exec_())

    
