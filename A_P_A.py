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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QWidget)

class Ui_A_P_A(object):
    def setupUi(self, A_P_A):
        if not A_P_A.objectName():
            A_P_A.setObjectName(u"A_P_A")
        A_P_A.resize(1600, 900)
        self.frame = QFrame(A_P_A)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1600, 900))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 70, 161, 101))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 460, 411, 51))
        self.Sequence_generation_Button = QPushButton(self.frame)
        self.Sequence_generation_Button.setObjectName(u"Sequence_generation_Button")
        self.Sequence_generation_Button.setGeometry(QRect(60, 550, 81, 51))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.Sequence_generation_Button.setIcon(icon)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 550, 91, 51))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 660, 411, 51))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 770, 81, 51))
        self.pushButton_4.setIcon(icon)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(190, 770, 91, 51))
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(660, 40, 211, 51))
        self.Create_page_missing_Image_button = QPushButton(self.frame)
        self.Create_page_missing_Image_button.setObjectName(u"Create_page_missing_Image_button")
        self.Create_page_missing_Image_button.setGeometry(QRect(1120, 650, 151, 81))
        self.clear_page_missing_image_button = QPushButton(self.frame)
        self.clear_page_missing_image_button.setObjectName(u"clear_page_missing_image_button")
        self.clear_page_missing_image_button.setGeometry(QRect(1120, 770, 151, 81))
        self.Page_Visit_Sequence_table = QTableWidget(self.frame)
        if (self.Page_Visit_Sequence_table.columnCount() < 1):
            self.Page_Visit_Sequence_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.Page_Visit_Sequence_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.Page_Visit_Sequence_table.setObjectName(u"Page_Visit_Sequence_table")
        self.Page_Visit_Sequence_table.setGeometry(QRect(490, 300, 121, 521))
        self.Page_Visit_Sequence_table.setLineWidth(0)
        self.Page_Visit_Sequence_table.setRowCount(0)
        self.Page_Visit_Sequence_table.setColumnCount(1)
        self.Create_change_number_Image_button = QPushButton(self.frame)
        self.Create_change_number_Image_button.setObjectName(u"Create_change_number_Image_button")
        self.Create_change_number_Image_button.setGeometry(QRect(1320, 650, 151, 81))
        self.clear_change_number_image_button = QPushButton(self.frame)
        self.clear_change_number_image_button.setObjectName(u"clear_change_number_image_button")
        self.clear_change_number_image_button.setGeometry(QRect(1320, 770, 151, 81))
        self.textBrowser_2 = QTextBrowser(self.frame)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(850, 550, 101, 31))
        self.textBrowser_3 = QTextBrowser(self.frame)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(1390, 550, 101, 31))

        self.retranslateUi(A_P_A)

        QMetaObject.connectSlotsByName(A_P_A)
    # setupUi

    def retranslateUi(self, A_P_A):
        A_P_A.setWindowTitle(QCoreApplication.translate("A_P_A", u"性能分析比较页面", None))
        self.pushButton.setText(QCoreApplication.translate("A_P_A", u"\u8fd4\u56de\u4e3b\u754c\u9762", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("A_P_A", u"\u8bf7\u8f93\u5165\u9875\u9762\u8bbf\u95ee\u5e8f\u5217\uff08\u652f\u6301\u4e00\u952e\u751f\u621020\u4f4d\u5f85\u6d4b\u5e8f\u5217,\u56de\u8f66\u505c\u6b62\u8f93\u5165\uff09", None))
        self.Sequence_generation_Button.setText(QCoreApplication.translate("A_P_A", u"\u4e00\u952e\u751f\u6210", None))
        self.pushButton_3.setText(QCoreApplication.translate("A_P_A", u"\u6e05\u7a7a\u5e8f\u5217", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("A_P_A", u"\u8bf7\u8f93\u5165\u6700\u5927\u7269\u7406\u5757\u6570(\u652f\u6301\u4e00\u952e\u751f\u62105-15\u4ee5\u5185\u7684\u968f\u673a\u5757\u6570\uff0c\u56de\u8f66\u505c\u6b62\u8f93\u5165)", None))
        self.pushButton_4.setText(QCoreApplication.translate("A_P_A", u"\u4e00\u952e\u751f\u6210", None))
        self.pushButton_5.setText(QCoreApplication.translate("A_P_A", u"\u6e05\u7a7a\u7269\u7406\u5757", None))
        self.textBrowser.setHtml(QCoreApplication.translate("A_P_A", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">\u6027\u80fd\u5206\u6790\u6bd4\u8f83</span></p></body></html>", None))
        self.Create_page_missing_Image_button.setText(QCoreApplication.translate("A_P_A", u"\u751f\u6210\u547d\u4e2d\u7387\u56fe\u50cf", None))
        self.clear_page_missing_image_button.setText(QCoreApplication.translate("A_P_A", u"\u6e05\u7a7a\u547d\u4e2d\u7387\u56fe\u50cf", None))
        ___qtablewidgetitem = self.Page_Visit_Sequence_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("A_P_A", u"\u9875\u9762\u8bbf\u95ee\u5e8f\u5217", None));
#if QT_CONFIG(accessibility)
        self.Page_Visit_Sequence_table.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.Create_change_number_Image_button.setText(QCoreApplication.translate("A_P_A", u"\u751f\u6210\u7f6e\u6362\u6b21\u6570\u56fe\u50cf", None))
        self.clear_change_number_image_button.setText(QCoreApplication.translate("A_P_A", u"\u6e05\u7a7a\u7f6e\u6362\u6b21\u6570\u56fe\u50cf", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("A_P_A", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     \u547d\u4e2d\u7387</p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("A_P_A", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     \u7f6e\u6362\u6b21\u6570</p></body></html>", None))
    # retranslateUi

