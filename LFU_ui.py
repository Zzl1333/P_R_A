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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"LFU 最近未使用算法")
        Form.resize(1600, 900)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(650, 30, 271, 61))
        self.Sequence_generation_line = QLineEdit(Form)
        self.Sequence_generation_line.setObjectName(u"Sequence_generation_line")
        self.Sequence_generation_line.setGeometry(QRect(30, 560, 411, 51))
        self.Sequence_generation_Button = QPushButton(Form)
        self.Sequence_generation_Button.setObjectName(u"Sequence_generation_Button")
        self.Sequence_generation_Button.setGeometry(QRect(30, 640, 81, 51))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.Sequence_generation_Button.setIcon(icon)
        self.Physical_block_generation_line = QLineEdit(Form)
        self.Physical_block_generation_line.setObjectName(u"Physical_block_generation_line")
        self.Physical_block_generation_line.setGeometry(QRect(30, 720, 411, 51))
        self.Physical_block_generation_Button = QPushButton(Form)
        self.Physical_block_generation_Button.setObjectName(u"Physical_block_generation_Button")
        self.Physical_block_generation_Button.setGeometry(QRect(30, 800, 81, 51))
        self.Physical_block_generation_Button.setIcon(icon)
        self.Back_L_S_P_Button = QPushButton(Form)
        self.Back_L_S_P_Button.setObjectName(u"Back_L_S_P_Button")
        self.Back_L_S_P_Button.setGeometry(QRect(40, 80, 211, 91))
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.Back_L_S_P_Button.setFont(font)
        self.Sequence_cllear_button = QPushButton(Form)
        self.Sequence_cllear_button.setObjectName(u"Sequence_cllear_button")
        self.Sequence_cllear_button.setGeometry(QRect(170, 640, 91, 51))
        self.Physical_block_clear = QPushButton(Form)
        self.Physical_block_clear.setObjectName(u"Physical_block_clear")
        self.Physical_block_clear.setGeometry(QRect(170, 800, 91, 51))
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(-7, -7, 1621, 921))
        self.textBrowser_2 = QTextBrowser(Form)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(30, 240, 381, 271))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(690, 120, 881, 711))
        self.widget.setAutoFillBackground(True)
        self.continue_button = QPushButton(self.widget)
        self.continue_button.setObjectName(u"continue_button")
        self.continue_button.setGeometry(QRect(100, 600, 141, 71))
        font1 = QFont()
        font1.setPointSize(14)
        self.continue_button.setFont(font1)
        self.continue_make_button = QPushButton(self.widget)
        self.continue_make_button.setObjectName(u"continue_make_button")
        self.continue_make_button.setGeometry(QRect(370, 600, 141, 71))
        self.continue_make_button.setFont(font1)
        self.Page_Visit_Sequence_table = QTableWidget(self.widget)
        if (self.Page_Visit_Sequence_table.columnCount() < 1):
            self.Page_Visit_Sequence_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.Page_Visit_Sequence_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.Page_Visit_Sequence_table.setObjectName(u"Page_Visit_Sequence_table")
        self.Page_Visit_Sequence_table.setGeometry(QRect(100, 20, 121, 521))
        self.Page_Visit_Sequence_table.setLineWidth(0)
        self.Page_Visit_Sequence_table.setRowCount(0)
        self.Page_Visit_Sequence_table.setColumnCount(1)
        self.Physical_block_generation_table = QTableWidget(self.widget)
        if (self.Physical_block_generation_table.columnCount() < 2):
            self.Physical_block_generation_table.setColumnCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Physical_block_generation_table.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Physical_block_generation_table.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        self.Physical_block_generation_table.setObjectName(u"Physical_block_generation_table")
        self.Physical_block_generation_table.setGeometry(QRect(360, 20, 221, 521))
        self.Physical_block_generation_table.setRowCount(0)
        self.Physical_block_generation_table.setColumnCount(2)
        self.page_missing_show = QLineEdit(self.widget)
        self.page_missing_show.setObjectName(u"page_missing_show")
        self.page_missing_show.setGeometry(QRect(710, 250, 151, 51))
        self.textBrowser_3 = QTextBrowser(self.widget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(600, 250, 81, 51))
        self.textBrowser_4 = QTextBrowser(self.widget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(600, 330, 81, 51))
        self.textBrowser_5 = QTextBrowser(self.widget)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(590, 410, 111, 51))
        self.page_shoting_show = QLineEdit(self.widget)
        self.page_shoting_show.setObjectName(u"page_shoting_show")
        self.page_shoting_show.setGeometry(QRect(710, 330, 151, 51))
        self.change_number_show = QLineEdit(self.widget)
        self.change_number_show.setObjectName(u"change_number_show")
        self.change_number_show.setGeometry(QRect(710, 410, 151, 51))
        self.plainTextEdit.raise_()
        self.textBrowser.raise_()
        self.Sequence_generation_line.raise_()
        self.Sequence_generation_Button.raise_()
        self.Physical_block_generation_line.raise_()
        self.Physical_block_generation_Button.raise_()
        self.Back_L_S_P_Button.raise_()
        self.Sequence_cllear_button.raise_()
        self.Physical_block_clear.raise_()
        self.textBrowser_2.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"LFU 最近未使用算法", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">LFU(\u6700\u5c11\u4f7f\u7528\u6b21\u6570)</span></p></body></html>", None))
        self.Sequence_generation_line.setText("")
        self.Sequence_generation_line.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u9875\u9762\u8bbf\u95ee\u5e8f\u5217\uff08\u652f\u6301\u4e00\u952e\u751f\u621020\u4f4d\u5f85\u6d4b\u5e8f\u5217,\u56de\u8f66\u505c\u6b62\u8f93\u5165\uff09", None))
        self.Sequence_generation_Button.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u751f\u6210", None))
        self.Physical_block_generation_line.setText("")
        self.Physical_block_generation_line.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u6700\u5927\u7269\u7406\u5757\u6570(\u652f\u6301\u4e00\u4ef6\u751f\u62105-15\u4ee5\u5185\u7684\u968f\u673a\u5757\u6570\uff0c\u56de\u8f66\u505c\u6b62\u8f93\u5165)", None))
        self.Physical_block_generation_Button.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u751f\u6210", None))
        self.Back_L_S_P_Button.setText(QCoreApplication.translate("Form", u"\u9000\u56de\u521d\u59cb\u9009\u62e9\u754c\u9762", None))
        self.Sequence_cllear_button.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u5e8f\u5217", None))
        self.Physical_block_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u7269\u7406\u5757", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'-apple-system','blinkmacsystemfont','Helvetica Neue','helvetica','segoe ui','arial','roboto','PingFang SC','miui','Hiragino Sans GB','Microsoft Yahei','sans-serif'; font-size:16pt; color:#060607; background-color:#ffffff;\">\u6700\u5c11\u4f7f\u7528\u7b97\u6cd5\uff08LFU\uff0cLeast Frequently Used\uff09\uff0c\u5176\u6838\u5fc3\u601d\u60f3\u662f\u5728\u53d1\u751f\u9875"
                        "\u9762\u7f6e\u6362\u65f6\uff0c\u9009\u62e9\u90a3\u4e9b\u5728\u6700\u8fd1\u4e00\u6bb5\u65f6\u95f4\u5185\u88ab\u8bbf\u95ee\u6b21\u6570\u6700\u5c11\u7684\u9875\u9762\u8fdb\u884c\u7f6e\u6362\u3002\u8fd9\u79cd\u7b97\u6cd5\u57fa\u4e8e\u4e00\u4e2a\u5047\u8bbe\uff1a\u5982\u679c\u4e00\u4e2a\u9875\u9762\u5728\u5f88\u957f\u4e00\u6bb5\u65f6\u95f4\u5185\u88ab\u8bbf\u95ee\u6b21\u6570\u5f88\u5c11\uff0c\u90a3\u4e48\u5728\u672a\u6765\u5b83\u88ab\u8bbf\u95ee\u7684\u53ef\u80fd\u6027\u4e5f\u4f1a\u76f8\u5bf9\u8f83\u4f4e\u3002\u56e0\u6b64\uff0c\u5f53\u9700\u8981\u4e3a\u65b0\u9875\u9762\u817e\u51fa\u7a7a\u95f4\u65f6\uff0cLFU\u7b97\u6cd5\u4f1a\u4f18\u5148\u6dd8\u6c70\u90a3\u4e9b\u8bbf\u95ee\u6b21\u6570\u6700\u5c11\u7684\u9875\u9762\u3002</span></p></body></html>", None))
        self.continue_button.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6\u4e00\u6b21\u9875\u9762", None))
        self.continue_make_button.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u751f\u6210", None))
        ___qtablewidgetitem = self.Page_Visit_Sequence_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u9875\u9762\u8bbf\u95ee\u5e8f\u5217", None));
#if QT_CONFIG(accessibility)
        self.Page_Visit_Sequence_table.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        ___qtablewidgetitem1 = self.Physical_block_generation_table.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u7269\u7406\u5757", None));
        ___qtablewidgetitem2 = self.Physical_block_generation_table.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u8bbf\u95ee\u6b21\u6570", None));
        self.textBrowser_3.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u7f3a\u9875\u7387</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u547d\u4e2d\u7387</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u7f6e\u6362\u6b21\u6570</span></p></body></html>", None))
    # retranslateUi

