from PySide6.QtWidgets import (QApplication, QWidget, QTextBrowser, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QHeaderView, QPlainTextEdit)
from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtWidgets import (QApplication, QWidget, QTextBrowser, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QHeaderView, QPlainTextEdit)
from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QIcon, QFont

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1600, 900)
        Form.setWindowTitle("LRU")  # 设置窗口标题为 "LRU"

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QRect(600, 30, 321, 61))
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "Form",
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">"
                "p, li { white-space: pre-wrap; }<hr { height: 1px; border-width: 0; }li.unchecked::marker { content: \"\\2610\"; }"
                "li.checked::marker { content: \"\\2612\"; }</style></head><body style=\" font-family:'Microsoft YaHei UI'; "
                "font-size:9pt; font-weight:400; font-style:normal;\">"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                "text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">LRU(最近最少使用)</span></p></body></html>",
                None))

        self.Sequence_generation_line = QLineEdit(Form)
        self.Sequence_generation_line.setGeometry(QRect(30, 370, 411, 51))
        self.Sequence_generation_line.setObjectName("Sequence_generation_line")
        self.Sequence_generation_line.setPlaceholderText(
            QCoreApplication.translate("Form", "请输入页面访问序列（支持一键生成20位待测序列,回车停止输入）", None))

        self.Sequence_generation_Button = QPushButton(Form)
        self.Sequence_generation_Button.setGeometry(QRect(30, 440, 81, 51))
        self.Sequence_generation_Button.setObjectName("Sequence_generation_Button")
        self.Sequence_generation_Button.setText(QCoreApplication.translate("Form", "一键生成", None))
        self.Sequence_generation_Button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))

        self.Page_Visit_Sequence_table = QTableWidget(Form)
        self.Page_Visit_Sequence_table.setGeometry(QRect(810, 140, 135, 661))
        self.Page_Visit_Sequence_table.setObjectName("Page_Visit_Sequence_table")
        self.Page_Visit_Sequence_table.setLineWidth(0)
        self.Page_Visit_Sequence_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(QCoreApplication.translate("Form", "页面访问序列", None))
        self.Page_Visit_Sequence_table.setHorizontalHeaderItem(0, __qtablewidgetitem)

        self.Physical_block_generation_line = QLineEdit(Form)
        self.Physical_block_generation_line.setGeometry(QRect(30, 560, 411, 51))
        self.Physical_block_generation_line.setObjectName("Physical_block_generation_line")
        self.Physical_block_generation_line.setPlaceholderText(
            QCoreApplication.translate("Form", "请输入最大物理块数(支持一键生成5-15以内的随机块数，回车停止输入)", None))

        self.Physical_block_generation_table = QTableWidget(Form)
        self.Physical_block_generation_table.setGeometry(QRect(1230, 140, 230, 661))
        self.Physical_block_generation_table.setObjectName("Physical_block_generation_table")
        self.Physical_block_generation_table.setRowCount(0)
        self.Physical_block_generation_table.setColumnCount(2)
        self.Physical_block_generation_table.setHorizontalHeaderLabels(["物理块", "访问次数"])

        self.Physical_block_generation_Button = QPushButton(Form)
        self.Physical_block_generation_Button.setGeometry(QRect(30, 630, 81, 51))
        self.Physical_block_generation_Button.setObjectName("Physical_block_generation_Button")
        self.Physical_block_generation_Button.setText(QCoreApplication.translate("Form", "一键生成", None))
        self.Physical_block_generation_Button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))

        self.Back_L_S_P_Button = QPushButton(Form)
        self.Back_L_S_P_Button.setGeometry(QRect(40, 80, 211, 91))
        self.Back_L_S_P_Button.setObjectName("Back_L_S_P_Button")
        font = QFont()
        font.setFamilies(["Microsoft JhengHei UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.Back_L_S_P_Button.setFont(font)
        self.Back_L_S_P_Button.setText(QCoreApplication.translate("Form", "退回初始选择界面", None))

        self.Sequence_cllear_button = QPushButton(Form)
        self.Sequence_cllear_button.setGeometry(QRect(170, 440, 91, 51))
        self.Sequence_cllear_button.setObjectName("Sequence_cllear_button")
        self.Sequence_cllear_button.setText(QCoreApplication.translate("Form", "清空序列", None))

        self.Physical_block_clear = QPushButton(Form)
        self.Physical_block_clear.setGeometry(QRect(170, 630, 91, 51))
        self.Physical_block_clear.setObjectName("Physical_block_clear")
        self.Physical_block_clear.setText(QCoreApplication.translate("Form", "清空物理块", None))

        self.continue_button = QPushButton(Form)
        self.continue_button.setGeometry(QRect(1020, 720, 141, 71))
        self.continue_button.setObjectName("continue_button")
        font1 = QFont()  # 定义 font1 变量
        font1.setPointSize(14)
        self.continue_button.setFont(font1)
        self.continue_button.setText(QCoreApplication.translate("Form", "读取一次页面", None))

        self.fill_blocks_button = QPushButton(Form)  # 新增的按钮
        self.fill_blocks_button.setObjectName("fill_blocks_button")
        self.fill_blocks_button.setGeometry(QRect(1020, 800, 141, 71))
        self.fill_blocks_button.setFont(font1)  # 使用 font1 变量
        self.fill_blocks_button.setText(QCoreApplication.translate("Form", "一键填充物理块", None))