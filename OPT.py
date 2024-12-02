from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem
import random
import string
from OPTui import Ui_SS

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QFile, QObject
from PySide6.QtUiTools import QUiLoader
from matplotlib.backends.backend_qt5agg import (  # 注意：这里实际上应该使用backend_qt6agg，但PySide6的对应后端可能未直接提供
    FigureCanvasQTAgg as FigureCanvas,  # 如果遇到问题，请查找PySide6的官方Matplotlib后端
)
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
     fig = Figure(figsize=(width, height), dpi=dpi)
     self.axes = fig.add_subplot(111)
     super().__init__(fig)
user_pages=''
user_frame_size=0
number=-1
frame = []
remaining_pages=[]
# 在QApplication之前先实例化

class Stats(QMainWindow,Ui_SS):
    def __init__(self, parent=None):
        super(Stats, self).__init__(parent)  # 正确传递 parent 参数
        self.setupUi(self)
        # 再加载界面
        self.pushButton.clicked.connect(self.close)
        self.lineEdit.returnPressed.connect(self.edit)
        self.lineEdit_2.returnPressed.connect(self.edit_2)
        self.pushButton_2.clicked.connect(self.l_pushButton_2)
        self.pushButton_3.clicked.connect(self.l_pushButton_3)
        self.pushButton_4.clicked.connect(self.l_pushButton_4)
        self.pushButton_5.clicked.connect(self.l_pushButton_5)
        self.pushButton_6.clicked.connect(self.l_pushButton_6)
        self.pushButton_7.clicked.connect(self.l_pushButton_7)
        table=self.tableWidget
        table1=self.tableWidget_2
        self.mpl_canvas = MplCanvas(self.widget, width=5, height=4, dpi=100)
        layout = QVBoxLayout(self.widget)  # 假设central_widget是一个QWidget，并且你希望在其上添加布局
        layout.addWidget(self.mpl_canvas)
        # 示例绘图
        t = [0, 1, 2, 3, 4]
        s = [0, 1, 4, 9, 16]
        self.mpl_canvas.axes.plot(t, s)
        self.mpl_canvas.draw()

    def edit(self):
        table = self.tableWidget
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
        table1 = self.tableWidget_2
        global number
        number = 0
        table1.setRowCount(0)
        global user_frame_size
        user_frame_size_str = self.lineEdit_2.text()
        user_frame_size = int(user_frame_size_str)
        for i in range(user_frame_size):
            table1.insertRow(0)


    def l_pushButton_2(self):
        table = self.tableWidget
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
        table = self.tableWidget
        global user_pages
        pages1 = user_pages
        table.setRowCount(0)
        self.lineEdit.clear()
        user_pages=[]

    def l_pushButton_4(self):
        table1 = self.tableWidget_2
        global number
        number = 0
        table1.setRowCount(0)
        global user_frame_size
        user_frame_size_str = str(random.randint(5, 15))
        user_frame_size = int(user_frame_size_str)
        for i in range(user_frame_size):
            table1.insertRow(0)
    def l_pushButton_5(self):
        table1 = self.tableWidget_2
        global user_frame_size
        table1.setRowCount(0)
        self.lineEdit_2.clear()
        user_frame_size=0

    def l_pushButton_6(self):
            global remaining_pages
            global frame
            global number
            number+=1
            table = self.tableWidget
            table1 = self.tableWidget_2
            replacements = []  # 页面置换序列
            pages = user_pages
            frame_size = user_frame_size
            page_faults = 0  # 缺页次数
            verbose = True
            page=pages[number-1]
            remaining_pages = pages[number:]  # 剩余页面访问序列
            if page in frame:
                print()
            else:
                    # 页面不在内存中，发生缺页
                    page_faults += 1
                    # 如果内存未满，直接添加页面
                    if len(frame) < frame_size:
                        frame.append(page)
                    else:
                        # 内存已满，选择未来最长时间不被使用的页面进行置换
                        furthest_use = {}
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
                frame1 = frame
                for i, frame1 in enumerate(frame):
                    item = QTableWidgetItem(frame1)  # 直接在创建项时设置文本
                    table1.setItem(i, 0, item)  # 将项放置在正确的行（i）和列（0）
                table.removeRow(0)


    def l_pushButton_7(self):
        table = self.tableWidget
        table1 = self.tableWidget_2
        frame = [] # 当前内存中的页面
        replacements = []  # 页面置换序列
        print(user_pages)
        pages=user_pages
        frame_size=user_frame_size
        page_faults = 0  # 缺页次数
        verbose = True
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
                else:
                    # 内存已满，选择未来最长时间不被使用的页面进行置换
                    furthest_use = {}
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
            frame1=frame
            for i, frame1 in enumerate(frame):
                table.setRowCount(0)
                item = QTableWidgetItem(frame1)  # 直接在创建项时设置文本
                table1.setItem(i, 0, item)  # 将项放置在正确的行（i）和列（0）中
        return replacements, page_faults
def OPT_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = Stats(parent)  # 传递 parent 参数
    win.show()