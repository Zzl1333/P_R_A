import sys
from A_S_P_ui import Ui_Page_Replacement_Algorithm
from PySide6.QtWidgets import QApplication, QMainWindow
from LFU import LFU_control
from FIFO import FIFO_control
from OPT import OPT_control
from LRU import LRU_control
# 按间距中的绿色按钮以运行脚本。
class MainWindow(QMainWindow, Ui_Page_Replacement_Algorithm):
   def __init__(self):
       super(MainWindow, self).__init__()
       self.ASP_setupUi(self)
       self.init_slots()

   def init_slots(self):
       self.LFU.clicked.connect(self.LFU_bulid)
       self.FIFO.clicked.connect(self.FIFO_bulid)
       self.OPT.clicked.connect(self.OPT_bulid)
       self.LRU.clicked.connect(self.LRU_bulid)
       """# 绑定 FIFO 按钮的点击事件
       self.FIFO.clicked.connect(self.open_LFU)
       # 绑定 LRU 按钮的点击事件
       self.LRU.clicked.connect(self.open_LFU)
       # 绑定 LFU 按钮的点击事件
       self.LFU.clicked.connect(self.open_LFU)
       # 绑定 OPT 按钮的点击事件
       self.OPT.clicked.connect(self.open_LFU)"""


   def LFU_bulid(self) :
        LFU_control(self)
   def FIFO_bulid(self) :
        FIFO_control(self)

   def LRU_bulid(self):
       LRU_control(self)
   def OPT_bulid(self):
       OPT_control(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
