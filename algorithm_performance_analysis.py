import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget
import string
from PySide6.QtCore import Qt
from collections import OrderedDict
from PySide6 import QtWidgets
import pyqtgraph as pg
from LFU_ui import Ui_Form
from pyqtgraph import PlotWidget
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QRect
from A_P_A import Ui_A_P_A
from collections import OrderedDict
from collections import deque
import random
user_pages=''
user_frame_size=0
faultss=0
faultss1=0
faultss2=0
faultss3=0
number=-1
frame = []
remaining_pages=[]
rate=0.0
rate1=0.0
rate2=0.0
rate3=0.0
verbose = True
class A_P_A_Window(QMainWindow, Ui_A_P_A):
    def __init__(self, parent=None):
        super(A_P_A_Window, self).__init__(parent)  # 正确传递 parent 参数
        self.setupUi(self)  # 加载 UI
        """绑定接口"""
        self.clear_page_missing_image_button.clicked.connect(self.clearPlot)
        self.clear_change_number_image_button.clicked.connect(self.clearPlot1)
        self.Create_page_missing_Image_button.clicked.connect(self.Create_page_missing_Image)
        self.Create_change_number_Image_button.clicked.connect(self.Create_change_number_Image)
        # 初始化 PlotWidget
        self.plotWidget1 = self.createPlotWidget1()
        self.plotWidget2 = self.createPlotWidget2()  # 创建第二个 PlotWidget
        self.Sequence_generation_Button.clicked.connect(self.l_Sequence_generation_Button)
        self.Sequence_generation_Button.clicked.connect(self.l_Sequence_generation_Button)
        self.Sequence_generation_Button.clicked.connect(self.l_Sequence_generation_Button)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.l_pushButton_3)
        self.pushButton_4.clicked.connect(self.l_pushButton_4)
        self.pushButton_5.clicked.connect(self.l_pushButton_5)
        self.lineEdit.returnPressed.connect(self.edit)
        self.lineEdit_2.returnPressed.connect(self.edit_2)
        table = self.Page_Visit_Sequence_table

        # 获取 frame 的尺寸和位置
        self.frame_width = self.frame.width()
        self.frame_height = self.frame.height()
        self.frame_x = self.frame.x()
        # 设置 PlotWidget 的位置和大小
        self.addPlot1WidgetToFrame(self.plotWidget1, 0)  # 添加第一个 PlotWidget
        self.addPlot2WidgetToFrame(self.plotWidget2, 0)  # 添加第二个 PlotWidget

    def edit(self):
        table = self.Page_Visit_Sequence_table
        global number
        number = 0
        global user_pages
        raw_text = self.lineEdit.text()
        user_pages = raw_text.strip().replace(" ", "")
        pages1 = user_pages
        # 首先，根据 pages1 列表的长度插入相应数量的行
        table.setRowCount(len(pages1))
        # 然后，遍历 pages1 列表，并将每个页面作为文本设置到相应的表格项中
        for i, page1 in enumerate(pages1):
            item = QTableWidgetItem(page1)  # 直接在创建项时设置文本
            table.setItem(i, 0, item)  # 将项放置在正确的行（i）和列（0）中

    def edit_2(self):
        global number
        number = 0
        global user_frame_size
        user_frame_size_str = self.lineEdit_2.text()
        user_frame_size = int(user_frame_size_str)
        self.page_missing_show.setText(user_frame_size_str)

    def l_Sequence_generation_Button(self):
        table = self.Page_Visit_Sequence_table
        global number
        number = 0
        # 定义可选的字符集（0-9）
        digits = string.digits  # 这等同于 '0123456789'
        # 生成一个包含20个字符的随机字符串
        global user_pages
        user_pages = ''.join(random.choices(digits, k=20))
        pages1 = user_pages
        # 首先，根据 pages1 列表的长度插入相应数量的行
        table.setRowCount(len(pages1))
        # 然后，遍历 pages1 列表，并将每个页面作为文本设置到相应的表格项中
        for i, page2 in enumerate(pages1):
            item = QTableWidgetItem(page2)  # 直接在创建项时设置文本
            table.setItem(i, 0, item)  # 将项放置在正确的行（i）和列（0）中

    def l_pushButton_3(self):
        table = self.Page_Visit_Sequence_table
        global user_pages
        pages1 = user_pages
        table.setRowCount(0)
        self.lineEdit.clear()
        user_pages=[]

    def l_pushButton_4(self):
        global number
        number = 0
        global user_frame_size
        user_frame_size_str = str(random.randint(5, 15))
        user_frame_size = int(user_frame_size_str)
        self.page_missing_show.setText(user_frame_size_str)

    def l_pushButton_5(self):
        global user_frame_size
        self.lineEdit_2.clear()
        self.page_missing_show.clear()
        user_frame_size=0

    def Create_page_missing_Image(self):
        global number
        global faultss
        global faultss1
        global faultss2
        global faultss3
        global rate
        global rate1
        global rate2
        global rate3
        faultss = 0
        frame = []  # 当前内存中的页面
        replacements = []  # 页面置换序列
        pages = user_pages
        frame_size = user_frame_size
        page_faults = 0  # 缺页次数
        verbose = True
        number = len(user_pages)
        for i, page in enumerate(pages):
            remaining_pages = pages[i + 1:]  # 剩余页面访问序列
            if page in frame:
                # 页面已在内存中，无需置换
                continue
            else:
                # 页面不在内存中，发生缺页
                page_faults += 1
                # 如果内存未满，直接添加页面
                if len(frame) < frame_size:
                    frame.append(page)
                    faultss = faultss + 1
                else:
                    # 内存已满，选择未来最长时间不被使用的页面进行置换
                    furthest_use = {}
                    faultss = faultss + 1
                    for f in frame:
                        try:
                            furthest_use[f] = remaining_pages.index(f)  # 查找未来首次出现的位置
                        except ValueError:
                            furthest_use[f] = float('inf')  # 如果未来不再出现，则设为无穷大
                    # 选择未来最长时间不被使用的页面进行置换
                    replacement = max(furthest_use, key=furthest_use.get)
                    replacements.append(replacement)
                    frame.remove(replacement)
                    frame.append(page)
        if verbose:
            number2=number-faultss
            rate = number2 / number

        faultss1=0
        frames = deque(maxlen=user_frame_size)
        for page in user_pages:
            if page not in frames:
                # 如果页面不在帧中，发生缺页
                faultss1 += 1
                # 如果帧已满，移除最早的页面（FIFO）
                if len(frames) == user_frame_size:
                    frames.popleft()
                # 添加新页面到帧中
                frames.append(page)
        number2=number-faultss1
        rate1 = number2 / number


        faultss2 = 0
        use_fame = list()
        frames = []  # 用来存储页面的列表

        for page in user_pages:
            if page not in frames:
                # 如果页面不在帧中，则发生缺页
                faultss2 += 1
                # 如果帧已满，需要找到一个最不常使用的页面进行置换
                if len(frames) == user_frame_size:
                    # 找到访问次数最少的页面（即最不常使用的页面）
                    # 这里我们需要一个辅助的数据结构来存储每个页面的访问次数
                    page_count = {p: use_fame.count(p) for p in frames}
                    lfu_page = min(page_count, key=page_count.get)
                    # 将找到的页面位置置为空
                    frames[frames.index(lfu_page)] = None
                    frames[frames.index(None)] = page
                # 将新页面添加到帧中
                else : frames.append(page)
            else:
                # 如果页面已在帧中，则增加其访问次数
                # 这里我们需要更新辅助数据结构中的计数
                use_fame.append(page)

        # 清理列表中的空位置
        frames = [p for p in frames if p is not None]

        number2 = number - faultss2
        rate2 = number2 / number


        faultss3 = 0
        frames = OrderedDict()  # 用于存储当前在内存中的页面及其顺序
        for page in user_pages:
            if page not in frames:
                # 如果页面不在内存中，则发生缺页
                faultss3 += 1
                # 如果内存已满，需要移除最旧的页面（即最近最少使用的页面）
                if len(frames) == user_frame_size:
                    frames.popitem(last=False)  # 移除最旧的页面
                # 将新页面添加到内存中
                frames[page] = None  # 值可以是任意，因为我们只关心键（页面）的顺序
            else:
                # 如果页面已在内存中，则将其移动到末尾以表示最近访问
                frames.move_to_end(page)

        number2 = number - faultss3
        rate3 = number2 / number




        self.plot1()

    def Create_change_number_Image(self):
            self.plot2()

    def createPlotWidget1(self):
        # 创建一个新的 PlotWidget
        plotWidget = pg.PlotWidget()
        plotWidget.setWindowTitle('PyQtGraph Plot Example')
        plotWidget.setRange(xRange=[0, 3], yRange=[0, 1])
        plotWidget.setBackground('w')  # 设置背景颜色为白色
        return plotWidget
    def createPlotWidget2(self):
        # 创建一个新的 PlotWidget
        plotWidget = pg.PlotWidget()
        plotWidget.setWindowTitle('PyQtGraph Plot Example')
        plotWidget.setRange(xRange=[0, 3], yRange=[0, 15])
        plotWidget.setBackground('w')  # 设置背景颜色为白色
        return plotWidget
    def plot1(self):
        print(rate1)
        print(rate3)
        print(rate2)
        print(rate)
        # 生成一些随机数据
        x = list(range(4))
        y = [rate1,rate3,rate2,rate]
        # 绘制折线图
        self.plotWidget1.plot(x, y, pen=pg.mkPen(color=(0, 0, 255), width=3))
        self.setCustomXAxisLabels(self.plotWidget1)

    def plot2(self):
        # 绘制一些其他数据到第二个 PlotWidget
        x = list(range(4))
        y2 = [faultss,faultss1,faultss2,faultss3]
        self.plotWidget2.plot(x, y2, pen=pg.mkPen(color=(255, 0, 0), width=3))
        self.setCustomXAxisLabels(self.plotWidget2)

    def clearPlot(self):
        # 清空折线图
        self.plotWidget1.clear()
    def clearPlot1(self):
        # 清空折线图
        self.plotWidget2.clear()
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
        plotWidget.setGeometry(self.frame_x + x_offset + 1150, self.frame.y()+150, self.frame_width // 2 - 400, self.frame_height - 550)
        # 将 PlotWidget 添加到窗口
        plotWidget.setParent(self.frame)  # 设置父控件

def algorithm_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = A_P_A_Window(parent)  # 传递 parent 参数
    win.show()
