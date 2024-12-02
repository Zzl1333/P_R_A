import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
import pyqtgraph as pg
from LFU_ui import Ui_Form
from pyqtgraph import PlotWidget
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QRect
from A_P_A import Ui_A_P_A
import random


class A_P_A_Window(QMainWindow, Ui_A_P_A):
    def __init__(self, parent=None):
        super(A_P_A_Window, self).__init__(parent)  # 正确传递 parent 参数
        self.A_P_A_setupUi(self)  # 加载 UI

        # 初始化 PlotWidget
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setWindowTitle('PyQtGraph Plot Example')
        self.plotWidget.setRange(xRange=[0, 10], yRange=[-1, 1])

        # 将 PlotWidget 添加到 frame 的右侧
        self.addPlotWidgetToFrame()

        # 绘制折线图
        self.plot()

    def plot(self):
        # 生成一些随机数据
        x = list(range(10))
        y = [random.random() for _ in range(10)]

        # 绘制折线图
        self.plotWidget.plot(x, y, pen=pg.mkPen(color=(0, 0, 255), width=3))

    def addPlotWidgetToFrame(self):
        # 获取 frame 的尺寸和位置
        frame_width = self.frame.width()
        frame_height = self.frame.height()
        frame_x = self.frame.x()

        # 设置 PlotWidget 的位置和大小
        self.plotWidget.setGeometry(frame_x + frame_width // 2, self.frame.y(), frame_width // 2, frame_height)

        # 将 PlotWidget 添加到窗口
        self.plotWidget.setParent(self.frame)  # 设置父控件

def algorithm_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = A_P_A_Window(parent)  # 传递 parent 参数
    win.show()
