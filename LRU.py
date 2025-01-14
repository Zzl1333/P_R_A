import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from LRU_ui import Ui_Form  # 确保这里正确地导入了Ui_Form类
import random
import time

class LRU_Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(LRU_Window, self).__init__(parent)
        self.setupUi(self)
        self.init_connections()
        self.usage_count = {}  # 用于跟踪每个页面的最后访问时间戳
        self.hit_count = 0  # 页面命中次数
        self.miss_count = 0  # 页面置换次数
        self.total_accesses = 0

    def init_connections(self):
        self.Back_L_S_P_Button.clicked.connect(self.close)
        self.Sequence_cllear_button.clicked.connect(self.clear_sequence)
        self.Sequence_generation_line.returnPressed.connect(self.generate_sequence_from_line)
        self.Sequence_generation_Button.clicked.connect(self.generate_sequence_randomly)
        self.Physical_block_clear.clicked.connect(self.clear_physical_blocks)
        self.Physical_block_generation_line.returnPressed.connect(self.generate_physical_blocks_from_line)
        self.Physical_block_generation_Button.clicked.connect(self.generate_physical_blocks_randomly)
        self.continue_button.clicked.connect(self.continue_read)
        self.fill_blocks_button.clicked.connect(self.fill_physical_blocks)

    def add_item_to_table(self, table, value, column=0):
        table.insertRow(table.rowCount())
        item = QTableWidgetItem(str(value))
        table.setItem(table.rowCount() - 1, column, item)

    def generate_sequence(self, sequence):
        for code in sequence:
            self.add_item_to_table(self.Page_Visit_Sequence_table, code)

    def clear_table(self, table):
        table.clearContents()
        table.setRowCount(0)

    def clear_sequence(self):
        self.clear_table(self.Page_Visit_Sequence_table)

    def generate_sequence_from_line(self):
        sequence = self.Sequence_generation_line.text()
        for digit in sequence:
            if digit.isdigit():  # 确保只处理数字字符
                self.add_item_to_table(self.Page_Visit_Sequence_table, int(digit))
        self.Sequence_generation_line.clear()

    def generate_sequence_randomly(self):
        self.generate_sequence(str(random.randint(10**19, 10**20 - 1)))

    def generate_physical_blocks(self, count):
        for _ in range(count):
            self.add_items_to_table(self.Physical_block_generation_table, ['', '0'])

    def generate_physical_blocks_from_line(self):
        count = int(self.Physical_block_generation_line.text())
        self.generate_physical_blocks(count)
        self.Physical_block_generation_line.clear()

    def generate_physical_blocks_randomly(self):
        count = random.randint(5, 10)
        self.generate_physical_blocks(count)

    def clear_physical_blocks(self):
        self.clear_table(self.Physical_block_generation_table)

    def add_items_to_table(self, table, values):
        table.insertRow(table.rowCount())
        for i, value in enumerate(values):
            item = QTableWidgetItem(str(value))
            table.setItem(table.rowCount() - 1, i, item)

    def find_least_recently_used(self):
        min_time = float('inf')
        lru_index = -1
        for i in range(self.Physical_block_generation_table.rowCount()):
            page_item = self.Physical_block_generation_table.item(i, 0)
            if page_item:
                last_used_time = self.usage_count.get(page_item.text(), 0)
                if last_used_time < min_time:
                    min_time = last_used_time
                    lru_index = i
        return lru_index

    def update_hit_miss_display(self):
        self.total_accesses = self.hit_count + self.miss_count
        if self.total_accesses == 0:
            page_fault_rate = 0.0
            hit_rate = 0.0
        else:
            page_fault_rate = (self.miss_count / self.total_accesses) * 100
            hit_rate = (self.hit_count / self.total_accesses) * 100

        # 使用 HTML 格式设置文本，使得缺页率、页面命中率和命中次数加粗并换行显示
        self.Hit_Miss_Display.setHtml(
            f"缺页率: <b>{page_fault_rate:.2f}%</b><br>"
            f"页面命中率: <b>{hit_rate:.2f}%</b><br>"
            f"置换次数: <b>{self.miss_count}</b>"
        )


    def continue_read(self):
        page_to_access_item = self.Page_Visit_Sequence_table.item(0, 0)
        if not page_to_access_item:
            return  # 如果没有页面访问序列，直接返回

        page_to_access = page_to_access_item.text()
        max_row = self.Physical_block_generation_table.rowCount()

        # 检查数据是否已经存在于物理块中
        for i in range(max_row):
            current_item = self.Physical_block_generation_table.item(i, 0)
            if current_item and current_item.text() == page_to_access:
                usage_item = self.Physical_block_generation_table.item(i, 1)
                current_usage = int(usage_item.text())
                self.Physical_block_generation_table.setItem(i, 1, QTableWidgetItem(str(current_usage + 1)))
                self.usage_count[page_to_access] = time.time()  # 更新最后使用时间为当前时间戳
                self.hit_count += 1  # 页面命中
                self.Page_Visit_Sequence_table.removeRow(0)
                self.update_hit_miss_display()
                return

        # 如果数据不在物理块中，找到第一个空的物理块或进行LRU页面置换
        for i in range(max_row):
            current_item = self.Physical_block_generation_table.item(i, 0)
            if current_item is None or current_item.text() == "":
                # 找到空的物理块，直接放入
                self.Physical_block_generation_table.setItem(i, 0, QTableWidgetItem(page_to_access))
                self.Physical_block_generation_table.setItem(i, 1, QTableWidgetItem("1"))
                self.usage_count[page_to_access] = time.time()  # 更新最后使用时间为当前时间戳
                self.miss_count += 1  # 页面置换
                self.Page_Visit_Sequence_table.removeRow(0)
                self.update_hit_miss_display()
                return

        # 如果所有物理块都不为空，则进行LRU页面置换
        lru_index = self.find_least_recently_used()
        self.Physical_block_generation_table.setItem(lru_index, 0, QTableWidgetItem(page_to_access))
        self.Physical_block_generation_table.setItem(lru_index, 1, QTableWidgetItem("1"))
        self.usage_count[page_to_access] = time.time()  # 更新最后使用时间为当前时间戳
        self.miss_count += 1  # 页面置换
        self.Page_Visit_Sequence_table.removeRow(0)
        self.update_hit_miss_display()

    def clear_physical_blocks(self):
        self.clear_table(self.Physical_block_generation_table)
        self.hit_count = 0
        self.miss_count = 0
        self.update_hit_miss_display()

    def fill_physical_blocks(self):
        # 遍历页面访问序列表中的所有项
        while self.Page_Visit_Sequence_table.rowCount() > 0:
            page_to_access_item = self.Page_Visit_Sequence_table.item(0, 0)
            if not page_to_access_item:
                break  # 如果没有页面访问序列，直接返回

            page_to_access = page_to_access_item.text()
            max_row = self.Physical_block_generation_table.rowCount()

            # 检查数据是否已经存在于物理块中
            for i in range(max_row):
                current_item = self.Physical_block_generation_table.item(i, 0)
                if current_item and current_item.text() == page_to_access:
                    usage_item = self.Physical_block_generation_table.item(i, 1)
                    current_usage = int(usage_item.text())
                    self.Physical_block_generation_table.setItem(i, 1, QTableWidgetItem(str(current_usage + 1)))
                    self.usage_count[page_to_access] = time.time()  # 更新最后使用时间为当前时间戳
                    self.hit_count += 1  # 页面命中
                    break
                elif current_item is None or current_item.text() == "":
                    # 找到空的物理块，直接放入
                    self.Physical_block_generation_table.setItem(i, 0, QTableWidgetItem(page_to_access))
                    self.Physical_block_generation_table.setItem(i, 1, QTableWidgetItem("1"))
                    self.usage_count[page_to_access] = time.time()  # 更新最后使用时间为当前时间戳
                    self.miss_count += 1  # 页面置换
                    break
            else:
                # 如果所有物理块都不为空，则进行LRU页面置换
                lru_index = self.find_least_recently_used()
                self.Physical_block_generation_table.setItem(lru_index, 0, QTableWidgetItem(page_to_access))
                self.Physical_block_generation_table.setItem(lru_index, 1, QTableWidgetItem("1"))
                self.usage_count[page_to_access] = time.time()  # 更新最后使用时间为当前时间戳
                self.miss_count += 1  # 页面置换

            self.Page_Visit_Sequence_table.removeRow(0)  # 移除已处理的页面
            self.update_hit_miss_display()  # 更新显示

        # 处理完毕后，更新显示
        self.update_hit_miss_display()

        # 清空页面访问序列
        self.clear_sequence()
        self.update_hit_miss_display()

def LRU_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = LRU_Window(parent)  # 传递 parent 参数
    win.show()