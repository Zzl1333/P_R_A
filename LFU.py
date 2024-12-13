import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from LFU_ui import Ui_Form
import random


class LFU_Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(LFU_Window, self).__init__(parent)  # 正确传递 parent 参数
        self.setupUi(self)  # 加载 UI
        self.total_ask_number = 0.0;
        """总访问次数"""
        self.missing_number = 0.0;
        """缺页中断次数==置换次数"""
        self.shoting_number = 0.0;
        """命中次数"""
        self.now_row = 0
        self.now_col = 0
        self.now_insert = 0

        self.code_number = 0
        self.Sequence_cllear_button.clicked.connect(self.Sequence_cllear_button_makeup)
        self.Sequence_generation_line.returnPressed.connect(self.Sequence_generation_line_makeup);
        self.Sequence_generation_Button.clicked.connect(self.Sequence_generation_Button_makeup)

        self.Physical_block_clear.clicked.connect(self.Physical_block_clear_makeup)
        self.Physical_block_generation_line.returnPressed.connect(self.Physical_block_generation_line_makeup)
        self.Physical_block_generation_Button.clicked.connect(self.Physical_block_generation_Button_makeup)

        self.continue_button.clicked.connect(self.continue_read)
        self.continue_make_button.clicked.connect(self.continue_make_read)
        self.Back_L_S_P_Button.clicked.connect(self.close)

    def number_show(self):
        """缺页率"""
        number_show = self.missing_number / self.total_ask_number
        percentage = "{:.2%}".format(number_show)
        self.page_missing_show.setText(percentage)

        """命中率"""
        number_show = self.shoting_number / self.total_ask_number
        percentage = "{:.2%}".format(number_show)
        self.page_shoting_show.setText(percentage)

        """置换次数"""
        change_number = str(self.missing_number)
        self.change_number_show.setText(change_number)

    def Sequence_generation_line_makeup(self):
        """输入完成序列回车"""
        self.sequence = self.Sequence_generation_line.text()
        i = 0
        for code in self.sequence:
            self.Page_Visit_Sequence_table.insertRow(self.Page_Visit_Sequence_table.rowCount())
            self.item = QTableWidgetItem()
            self.item.setText(code)
            self.Page_Visit_Sequence_table.setItem(0, self.code_number, self.item)
            self.code_number += 1

    def Sequence_generation_Button_makeup(self):
        """点击一件生成序列按钮"""
        self.Page_Visit_Sequence_table.clearContents()
        self.Page_Visit_Sequence_table.setRowCount(0)
        self.code_number = 0
        self.random_number = random.randint(10 ** 19, 10 ** 20 - 1)
        self.random_number = str(self.random_number)
        for code in self.random_number:
            self.Page_Visit_Sequence_table.insertRow(self.Page_Visit_Sequence_table.rowCount())
            self.item = QTableWidgetItem()
            self.item.setText(code)
            self.Page_Visit_Sequence_table.setItem(0, self.code_number, self.item)
            self.code_number += 1

    def Sequence_cllear_button_makeup(self):
        """点击清空序列按钮"""
        self.code_number = 0
        self.Page_Visit_Sequence_table.clearContents()
        self.Page_Visit_Sequence_table.setRowCount(0)

    def Physical_block_generation_line_makeup(self):
        """输入完成物理块回车"""
        self.block = self.Physical_block_generation_line.text()
        self.block = int(self.block)
        i = 0
        for code in range(0, self.block):
            self.Physical_block_generation_table.insertRow(self.Physical_block_generation_table.rowCount())

    def Physical_block_generation_Button_makeup(self):
        """点击一件生成序列按钮"""
        self.block_random_number = random.randint(5, 10)
        self.block_random_number = int(self.block_random_number)
        for num in range(0, self.block_random_number):
            self.Physical_block_generation_table.insertRow(self.Physical_block_generation_table.rowCount())

    def Physical_block_clear_makeup(self):
        """点击清空物理块按钮"""
        self.Physical_block_generation_table.clearContents()
        self.Physical_block_generation_table.setRowCount(0)
        self.now_insert = 0
        self.page_missing_show.clear()
        self.page_shoting_show.clear()
        self.change_number_show.clear()
        self.total_ask_number = 0
        self.missing_number = 0
        self.shoting_number = 0

    def continue_read(self):
        self.total_ask_number += 1
        """点击读取一次按钮"""
        self.max_row = self.Physical_block_generation_table.rowCount()
        self.max_col = self.Physical_block_generation_table.columnCount()

        if self.now_insert < self.max_row:
            """物理块未放满"""
            for i in range(0, self.now_insert):
                if self.now_insert != 0:
                    if self.Page_Visit_Sequence_table.item(0, 0).text() == self.Physical_block_generation_table.item(i,
                                                                                                                     0).text():
                        """物理块中已存放当前页面"""
                        past_number = str(int(self.Physical_block_generation_table.item(i, 1).text()) + 1)
                        self.Physical_block_generation_table.item(i, 1).setText(past_number)
                        self.Page_Visit_Sequence_table.removeRow(0)
                        self.shoting_number += 1
                        self.number_show()
                        return 0

            self.Physical_block_generation_table.setItem(self.now_insert, 0, QTableWidgetItem(
                self.Page_Visit_Sequence_table.item(0, 0).text()))
            self.Physical_block_generation_table.setItem(self.now_insert, 1, QTableWidgetItem("1"))
            self.Page_Visit_Sequence_table.removeRow(0)
            self.now_insert += 1

            self.missing_number += 1
            self.number_show()


        elif self.now_insert == self.max_row:
            """物理块已满，需要进行页面置换"""
            for i in range(0, self.max_row):
                if self.Page_Visit_Sequence_table.item(0, 0).text() == self.Physical_block_generation_table.item(i,
                                                                                                                 0).text():
                    """物理块中已存放当前页面"""
                    past_number = str(int(self.Physical_block_generation_table.item(i, 1).text()) + 1)
                    self.Physical_block_generation_table.item(i, 1).setText(past_number)
                    self.Page_Visit_Sequence_table.removeRow(0)
                    self.shoting_number += 1
                    self.number_show()
                    return 0

            self.min_table_location = 0
            self.min_table_number = 0
            self.min_table_number = self.Physical_block_generation_table.item(0, 1).text()

            """寻找最小使用页表"""
            for i in range(0, self.max_row):
                if self.Physical_block_generation_table.item(i, 1).text() < self.min_table_number:
                    self.min_table_location = i
                    self.min_table_number = self.Physical_block_generation_table.item(i, 1).text()

            """更新物理块表"""
            self.item = QTableWidgetItem()
            pest_number = str(self.Page_Visit_Sequence_table.item(0, 0).text())
            self.item.setText(pest_number)
            self.Physical_block_generation_table.setItem(self.min_table_location, 0, self.item)
            self.Physical_block_generation_table.setItem(self.min_table_location, 1, QTableWidgetItem("1"))
            self.Page_Visit_Sequence_table.removeRow(0)
            self.missing_number += 1
            self.number_show()

        if self.Page_Visit_Sequence_table.rowCount() == 0:
            self.Sequence_cllear_button_makeup()

        """number_show = self.missing_number / self.total_ask_number
        percentage = "{:.2%}".format(number_show)
        self.page_missing_show.setText(percentage)"""

    def continue_make_read(self):
        """一键生成按钮，检测到待访问页面则持续执行"""
        while self.Page_Visit_Sequence_table.rowCount() != 0:
            self.continue_read()
        self.page_missing_show.setText()


def LFU_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = LFU_Window(parent)  # 传递 parent 参数
    win.show()