# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'A_P_A.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)
from PySide6 import QtWidgets
import pyqtgraph as pg

class Ui_A_P_A(object):
    def A_P_A_setupUi(self, A_P_A):
        if not A_P_A.objectName():
            A_P_A.setObjectName(u"A_P_A")
        A_P_A.resize(1600, 900)
        self.frame = QFrame(A_P_A)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 1600, 921))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 70, 161, 101))
        self.Sequence_generation_line = QLineEdit(self.frame)
        self.Sequence_generation_line.setObjectName(u"Sequence_generation_line")
        self.Sequence_generation_line.setGeometry(QRect(60, 460, 411, 51))
        self.Sequence_generation_Button = QPushButton(self.frame)
        self.Sequence_generation_Button.setObjectName(u"Sequence_generation_Button")
        self.Sequence_generation_Button.setGeometry(QRect(60, 550, 81, 51))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.Sequence_generation_Button.setIcon(icon)
        self.Sequence_cllear_button = QPushButton(self.frame)
        self.Sequence_cllear_button.setObjectName(u"Sequence_cllear_button")
        self.Sequence_cllear_button.setGeometry(QRect(180, 550, 91, 51))
        self.Physical_block_generation_line = QLineEdit(self.frame)
        self.Physical_block_generation_line.setObjectName(u"Physical_block_generation_line")
        self.Physical_block_generation_line.setGeometry(QRect(60, 660, 411, 51))
        self.Physical_block_generation_Button = QPushButton(self.frame)
        self.Physical_block_generation_Button.setObjectName(u"Physical_block_generation_Button")
        self.Physical_block_generation_Button.setGeometry(QRect(60, 770, 81, 51))
        self.Physical_block_generation_Button.setIcon(icon)
        self.Physical_block_clear = QPushButton(self.frame)
        self.Physical_block_clear.setObjectName(u"Physical_block_clear")
        self.Physical_block_clear.setGeometry(QRect(190, 770, 91, 51))
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(660, 40, 211, 51))

        self.retranslateUi(A_P_A)




        QMetaObject.connectSlotsByName(A_P_A)
    # setupUi

    def retranslateUi(self, A_P_A):
        A_P_A.setWindowTitle(QCoreApplication.translate("A_P_A", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("A_P_A", u"\u8fd4\u56de\u4e3b\u754c\u9762", None))
        self.Sequence_generation_line.setText("")
        self.Sequence_generation_line.setPlaceholderText(QCoreApplication.translate("A_P_A", u"\u8bf7\u8f93\u5165\u9875\u9762\u8bbf\u95ee\u5e8f\u5217\uff08\u652f\u6301\u4e00\u952e\u751f\u621020\u4f4d\u5f85\u6d4b\u5e8f\u5217,\u56de\u8f66\u505c\u6b62\u8f93\u5165\uff09", None))
        self.Sequence_generation_Button.setText(QCoreApplication.translate("A_P_A", u"\u4e00\u952e\u751f\u6210", None))
        self.Sequence_cllear_button.setText(QCoreApplication.translate("A_P_A", u"\u6e05\u7a7a\u5e8f\u5217", None))
        self.Physical_block_generation_line.setText("")
        self.Physical_block_generation_line.setPlaceholderText(QCoreApplication.translate("A_P_A", u"\u8bf7\u8f93\u5165\u6700\u5927\u7269\u7406\u5757\u6570(\u652f\u6301\u4e00\u952e\u751f\u62105-15\u4ee5\u5185\u7684\u968f\u673a\u5757\u6570\uff0c\u56de\u8f66\u505c\u6b62\u8f93\u5165)", None))
        self.Physical_block_generation_Button.setText(QCoreApplication.translate("A_P_A", u"\u4e00\u952e\u751f\u6210", None))
        self.Physical_block_clear.setText(QCoreApplication.translate("A_P_A", u"\u6e05\u7a7a\u7269\u7406\u5757", None))
        self.textBrowser.setHtml(QCoreApplication.translate("A_P_A", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">\u6027\u80fd\u5206\u6790\u6bd4\u8f83</span></p></body></html>", None))
    # retranslateUi

