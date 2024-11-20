import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from LFU_ui import Ui_Form
import random

class LFU_Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(LFU_Window, self).__init__(parent)  # 正确传递 parent 参数
        self.LFU_setupUi(self)  # 加载 UI
        self.code_number = 0
        self.Sequence_clear_button.clicked.connect(self.Sequence_cllear_button_makeup)
        self.Sequence_generation_line.returnPressed.connect(self.Sequence_generation_line_makeup);
        self.Sequence_generation_Button.clicked.connect(self.Sequence_generation_Button_makeup)

        self.Physical_block_clear.clicked.connect(self.Physical_block_clear_makeup)
        self.Physical_block_generation_line.returnPressed.connect(self.Physical_block_generation_line_makeup)
        self.Physical_block_generation_Button.clicked.connect(self.Physical_block_generation_Button_makeup)

        self.continue_button.clicked.connect(self.continue_read)
        self.Back_L_S_P_Button.clicked.connect(self.close)

    def Sequence_generation_line_makeup(self):
        """输入完成序列回车"""
        self.sequence = self.Sequence_generation_line.text()
        i=0
        for code in self.sequence:
            self.Page_Visit_Sequence_table.insertRow(self.Page_Visit_Sequence_table.rowCount())
            self.item = QTableWidgetItem()
            self.item.setText(code)
            self.Page_Visit_Sequence_table.setItem(0, self.code_number, self.item)
            self.code_number += 1

    def Sequence_generation_Button_makeup(self):
        """点击一件生成序列按钮"""
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
        for code in range (0,self.block):
            self.Physical_block_generation_table.insertRow(self.Physical_block_generation_table.rowCount())

    def Physical_block_generation_Button_makeup(self):
        """点击一件生成序列按钮"""
        self.block_random_number = random.randint(5,10)
        self.block_random_number = int(self.block_random_number)
        for num in range (0,self.block_random_number):
            self.Physical_block_generation_table.insertRow(self.Physical_block_generation_table.rowCount())

    def Physical_block_clear_makeup(self):
        """点击清空物理块按钮"""
        self.Physical_block_generation_table.clearContents()
        self.Physical_block_generation_table.setRowCount(0)

    def continue_read(self):
        """点击读取一次按钮"""


def mian_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = LFU_Window(parent)  # 传递 parent 参数
    win.show()