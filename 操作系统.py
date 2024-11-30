from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem
import random
import string
user_pages=''
user_frame_size=0
number=-1
frame = []
remaining_pages=[]
# 在QApplication之前先实例化
uiLoader = QUiLoader()
class Stats:
    def __init__(self):
        # 再加载界面
        self.ui = uiLoader.load('untitled.ui')
        self.ui.pushButton.clicked.connect(self.pushButton)
        self.ui.lineEdit.returnPressed.connect(self.edit)
        self.ui.lineEdit_2.returnPressed.connect(self.edit_2)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3)
        self.ui.pushButton_4.clicked.connect(self.pushButton_4)
        self.ui.pushButton_5.clicked.connect(self.pushButton_5)
        self.ui.pushButton_6.clicked.connect(self.pushButton_6)
        self.ui.pushButton_7.clicked.connect(self.pushButton_7)
        table=self.ui.tableWidget
        table1=self.ui.tableWidget_2

    def edit(self):
        table = self.ui.tableWidget
        global number
        number = 0
        global user_pages
        raw_text = self.ui.lineEdit.text()
        user_pages = raw_text.strip().replace(" ", "")
        pages1 = user_pages
        # 首先，根据 pages1 列表的长度插入相应数量的行
        table.setRowCount(len(pages1))
        # 然后，遍历 pages1 列表，并将每个页面作为文本设置到相应的表格项中
        for i, page1 in enumerate(pages1):
            item = QTableWidgetItem(page1)  # 直接在创建项时设置文本
            table.setItem(i, 0, item)  # 将项放置在正确的行（i）和列（0）中

    def edit_2(self):
        table1 = self.ui.tableWidget_2
        global number
        number = 0
        table1.setRowCount(0)
        global user_frame_size
        user_frame_size_str = self.ui.lineEdit_2.text()
        user_frame_size = int(user_frame_size_str)
        for i in range(user_frame_size):
            table1.insertRow(0)

    def pushButton(self):
        app.quit()

    def pushButton_2(self):
        table = self.ui.tableWidget
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

    def pushButton_3(self):
        table = self.ui.tableWidget
        global user_pages
        pages1 = user_pages
        table.setRowCount(0)
        self.ui.lineEdit.clear()
        user_pages=[]

    def pushButton_4(self):
        table1 = self.ui.tableWidget_2
        global number
        number = 0
        table1.setRowCount(0)
        global user_frame_size
        user_frame_size_str = str(random.randint(5, 15))
        user_frame_size = int(user_frame_size_str)
        for i in range(user_frame_size):
            table1.insertRow(0)
    def pushButton_5(self):
        table1 = self.ui.tableWidget_2
        global user_frame_size
        table1.setRowCount(0)
        self.ui.lineEdit_2.clear()
        user_frame_size=0

    def pushButton_6(self):
            global remaining_pages
            global frame
            global number
            number+=1
            table = self.ui.tableWidget
            table1 = self.ui.tableWidget_2
            replacements = []  # 页面置换序列
            pages = user_pages
            frame_size = user_frame_size
            page_faults = 0  # 缺页次数
            verbose = True
            page=pages[number-1]
            print(page)
            remaining_pages = pages[number:]  # 剩余页面访问序列
            if verbose:
                    print(f"步骤 {number }: 访问页面 {page}, 当前内存: {frame}, 剩余页面: {remaining_pages}")
            if page in frame:
                    # 页面已在内存中，无需置换
                    if verbose:
                        print(f"  页面 {page} 已在内存中，无需置换。")
            else:
                    # 页面不在内存中，发生缺页
                    page_faults += 1
                    # 如果内存未满，直接添加页面
                    if len(frame) < frame_size:
                        frame.append(page)
                        if verbose:
                            print(f"  内存未满，添加页面 {page} 到内存。")
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
                print(frame)
                print(remaining_pages)
                frame1 = frame
                for i, frame1 in enumerate(frame):
                    item = QTableWidgetItem(frame1)  # 直接在创建项时设置文本
                    table1.setItem(i, 0, item)  # 将项放置在正确的行（i）和列（0）
                table.removeRow(0)


    def pushButton_7(self):
        table = self.ui.tableWidget
        table1 = self.ui.tableWidget_2
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
app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec()