from A_S_P_ui import Ui_Page_Replacement_Algorithm
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
# 按间距中的绿色按钮以运行脚本。
class MainWindow(QMainWindow, Ui_Page_Replacement_Algorithm):
   def __init__(self):
       super(MainWindow, self).__init__()
       self.setupUi(self)  # 加载 UI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
