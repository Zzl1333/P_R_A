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

        """绑定接口"""
        self.clear_page_missing_image_button.clicked.connect(self.clearPlot)
        self.Create_page_missing_Image_button.clicked.connect(self.Create_page_missing_Image)




        # 初始化 PlotWidget
        self.plotWidget1 = self.createPlotWidget()
        self.plotWidget2 = self.createPlotWidget()  # 创建第二个 PlotWidget

        # 获取 frame 的尺寸和位置
        self.frame_width = self.frame.width()
        self.frame_height = self.frame.height()
        self.frame_x = self.frame.x()
        # 设置 PlotWidget 的位置和大小
        self.addPlot1WidgetToFrame(self.plotWidget1, 0)  # 添加第一个 PlotWidget
        self.addPlot2WidgetToFrame(self.plotWidget2, 0)  # 添加第二个 PlotWidget

    def Create_page_missing_Image(self):
        self.plot()
    def createPlotWidget(self):
        # 创建一个新的 PlotWidget
        plotWidget = pg.PlotWidget()
        plotWidget.setWindowTitle('PyQtGraph Plot Example')
        plotWidget.setRange(xRange=[0, 3], yRange=[-1, 1])
        plotWidget.setBackground('w')  # 设置背景颜色为白色
        return plotWidget
    def plot(self):
        # 生成一些随机数据
        x = list(range(4))
        y = [random.random() for _ in range(4)]
        # 绘制折线图
        self.plotWidget1.plot(x, y, pen=pg.mkPen(color=(0, 0, 255), width=3))
        self.setCustomXAxisLabels(self.plotWidget1)

        # 绘制一些其他数据到第二个 PlotWidget
        y2 = [random.random() for _ in range(4)]
        self.plotWidget2.plot(x, y2, pen=pg.mkPen(color=(255, 0, 0), width=3))
        self.setCustomXAxisLabels(self.plotWidget2)

    def clearPlot(self):
        # 清空折线图
        self.plotWidget1.clear()
    def setCustomXAxisLabels(self,plotWidget):
        # 设置x轴的刻度位置和标签
        x_ticks = [0, 1, 2, 3]  # 刻度位置
        x_labels = ['FIFO', 'LRU', 'LFU', 'OPT']  # 刻度标签
        # 获取PlotItem对象
        plot_item = plotWidget.getPlotItem()
        # 获取x轴的AxisItem对象
        x_axis = plot_item.getAxis('bottom')
        # 设置刻度和标签
        x_axis.setTicks([[(x, label) for x, label in zip(x_ticks, x_labels)]])

    def addPlot1WidgetToFrame(self, plotWidget, x_offset):
        # 设置 PlotWidget 的位置和大小
        plotWidget.setGeometry(self.frame_x + x_offset + 700, self.frame.y()+150, self.frame_width // 2 - 400, self.frame_height - 550)
        # 将 PlotWidget 添加到窗口
        plotWidget.setParent(self.frame)  # 设置父控件
    def addPlot2WidgetToFrame(self, plotWidget, x_offset):
        # 设置 PlotWidget 的位置和大小
        plotWidget.setGeometry(self.frame_x + x_offset + 1200, self.frame.y()+150, self.frame_width // 2 - 400, self.frame_height - 550)
        # 将 PlotWidget 添加到窗口
        plotWidget.setParent(self.frame)  # 设置父控件

def algorithm_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = A_P_A_Window(parent)  # 传递 parent 参数
    win.show()
