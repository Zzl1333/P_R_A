# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LFU_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextBrowser,
    QWidget)

class Ui_Form(object):
    def LFU_setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1600, 900)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(600, 30, 321, 61))
        self.Sequence_generation_line = QLineEdit(Form)
        self.Sequence_generation_line.setObjectName(u"Sequence_generation_line")
        self.Sequence_generation_line.setGeometry(QRect(50, 240, 311, 51))
        self.Sequence_generation_Button = QPushButton(Form)
        self.Sequence_generation_Button.setObjectName(u"Sequence_generation_Button")
        self.Sequence_generation_Button.setGeometry(QRect(390, 240, 81, 51))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.Sequence_generation_Button.setIcon(icon)
        self.Page_Visit_Sequence_table = QTableWidget(Form)
        if (self.Page_Visit_Sequence_table.columnCount() < 1):
            self.Page_Visit_Sequence_table.setColumnCount(1)
        if (self.Page_Visit_Sequence_table.rowCount() < 20):
            self.Page_Visit_Sequence_table.setRowCount(20)
        self.Page_Visit_Sequence_table.setObjectName(u"Page_Visit_Sequence_table")
        self.Page_Visit_Sequence_table.setGeometry(QRect(810, 140, 131, 661))
        self.Page_Visit_Sequence_table.setRowCount(20)
        self.Page_Visit_Sequence_table.setColumnCount(1)
        self.Physical_block_generation_line = QLineEdit(Form)
        self.Physical_block_generation_line.setObjectName(u"Physical_block_generation_line")
        self.Physical_block_generation_line.setGeometry(QRect(50, 580, 311, 51))
        self.Physical_block_generation_table = QTableWidget(Form)
        if (self.Physical_block_generation_table.columnCount() < 1):
            self.Physical_block_generation_table.setColumnCount(1)
        if (self.Physical_block_generation_table.rowCount() < 15):
            self.Physical_block_generation_table.setRowCount(15)
        self.Physical_block_generation_table.setObjectName(u"Physical_block_generation_table")
        self.Physical_block_generation_table.setGeometry(QRect(1230, 140, 221, 661))
        self.Physical_block_generation_table.setRowCount(15)
        self.Physical_block_generation_table.setColumnCount(1)
        self.Physical_block_generation_Button = QPushButton(Form)
        self.Physical_block_generation_Button.setObjectName(u"Physical_block_generation_Button")
        self.Physical_block_generation_Button.setGeometry(QRect(390, 580, 81, 51))
        self.Physical_block_generation_Button.setIcon(icon)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">LFU(\u6700\u5c11\u4f7f\u7528\u6b21\u6570)</span></p></body></html>", None))
        self.Sequence_generation_line.setText("")
        self.Sequence_generation_line.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u9875\u9762\u8bbf\u95ee\u5e8f\u5217\uff08\u652f\u6301\u4e00\u952e\u751f\u621020\u4f4d\u5f85\u6d4b\u5e8f\u5217\uff09", None))
        self.Sequence_generation_Button.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u751f\u6210", None))
        self.Physical_block_generation_line.setText("")
        self.Physical_block_generation_line.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u6700\u5927\u7269\u7406\u5757\u6570(\u652f\u6301\u4e00\u4ef6\u751f\u621015\u4ee5\u5185)", None))
        self.Physical_block_generation_Button.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u751f\u6210", None))
    # retranslateUi

