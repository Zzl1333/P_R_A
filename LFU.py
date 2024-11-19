import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from LFU_ui import Ui_Form

class LFU_Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(LFU_Window, self).__init__(parent)  # 正确传递 parent 参数
        self.LFU_setupUi(self)  # 加载 UI

def mian_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
    win = LFU_Window(parent)  # 传递 parent 参数
    win.show()