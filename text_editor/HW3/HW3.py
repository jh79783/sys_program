import sys, datetime
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor, QTextCharFormat, QFont
from PyQt5.QtCore import Qt, QDate


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.ui = uic.loadUi("HW3.ui", self)
        self.setup_ui()

    def setup_ui(self):
        holidays = ['20200101', '20200124', '20200125', '20200127', '20200415', '20200430', '20200505', '20200606',
                    '20200815', '20200930', '20201001', '20201002', '20201003', '20201009', '20201225']
        box = QVBoxLayout()
        col = QTextCharFormat()
        col.setForeground(Qt.red)
        col.setBackground(Qt.yellow)
        for days in holidays:
            day = QDate.fromString(days, "yyyyMMdd")
            self.cw.setDateTextFormat(day, col)
        box.addWidget(self.cw)
        self.setLayout(box)
        now = datetime.datetime.now()
        self.timeEdit_1.setTime(now.time())
        self.timeEdit_2.setTime(now.time())
        self.timeEdit_3.setTime(now.time())
        self.timeEdit_4.setTime(now.time())
        self.timeEdit_5.setTime(now.time())
        self.checkBox_1.toggled.connect(self.set_gray_1)
        self.checkBox_2.toggled.connect(self.set_gray_2)
        self.checkBox_3.toggled.connect(self.set_gray_3)
        self.checkBox_4.toggled.connect(self.set_gray_4)
        self.checkBox_5.toggled.connect(self.set_gray_5)
        self.checkBox_6.toggled.connect(self.set_gray_6)
        self.checkBox_7.toggled.connect(self.set_gray_7)
        self.checkBox_8.toggled.connect(self.set_gray_8)
        self.checkBox_9.toggled.connect(self.set_gray_9)
        self.checkBox_10.toggled.connect(self.set_gray_10)
        self.checkBox_11.toggled.connect(self.set_gray_11)
        self.checkBox_12.toggled.connect(self.set_gray_12)
        self.btn_reset.clicked.connect(self.cleartext)
        self.btn_save.clicked.connect(self.memo_save)
        self.btn_open.clicked.connect(self.memo_open)
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))


    def memo_open(self):
        filename = QFileDialog.getOpenFileName(filter="Text files (*.txt)")
        filename = filename[0]
        if not filename:
            return
        with open(filename, "r", encoding="utf8") as f:
            text = f.read(10000)
            self.plainTextEdit_memo.setPlainText(text)

    def memo_save(self):
        filename = QFileDialog.getSaveFileName(filter="Text files (*.txt)")
        filename = filename[0]
        if not filename:
            return
        with open(filename, "w", encoding="utf8") as f:
            f.write(self.plainTextEdit_memo.toPlainText())

    def cleartext(self):
        self.textEdit_1.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.textEdit_6.clear()
        self.textEdit_7.clear()
        self.textEdit_8.clear()
        self.textEdit_9.clear()
        self.textEdit_10.clear()
        self.textEdit_11.clear()
        self.textEdit_12.clear()
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        now = datetime.datetime.now()
        self.timeEdit_1.setTime(now.time())
        self.timeEdit_2.setTime(now.time())
        self.timeEdit_3.setTime(now.time())
        self.timeEdit_4.setTime(now.time())
        self.timeEdit_5.setTime(now.time())

    def set_gray_1(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_1.setTextColor(fontcolor)
            text = self.textEdit_1.toPlainText()
            self.textEdit_1.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_1.setTextColor(oricolor)
            text = self.textEdit_1.toPlainText()
            self.textEdit_1.setText(text)

    def set_gray_2(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_2.setTextColor(fontcolor)
            text = self.textEdit_2.toPlainText()
            self.textEdit_2.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_2.setTextColor(oricolor)
            text = self.textEdit_2.toPlainText()
            self.textEdit_2.setText(text)

    def set_gray_3(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_3.setTextColor(fontcolor)
            text = self.textEdit_3.toPlainText()
            self.textEdit_3.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_3.setTextColor(oricolor)
            text = self.textEdit_3.toPlainText()
            self.textEdit_3.setText(text)

    def set_gray_4(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_4.setTextColor(fontcolor)
            text = self.textEdit_4.toPlainText()
            self.textEdit_4.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_4.setTextColor(oricolor)
            text = self.textEdit_4.toPlainText()
            self.textEdit_4.setText(text)

    def set_gray_5(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_5.setTextColor(fontcolor)
            text = self.textEdit_5.toPlainText()
            self.textEdit_5.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_5.setTextColor(oricolor)
            text = self.textEdit_5.toPlainText()
            self.textEdit_5.setText(text)

    def set_gray_6(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_6.setTextColor(fontcolor)
            text = self.textEdit_6.toPlainText()
            self.textEdit_6.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_6.setTextColor(oricolor)
            text = self.textEdit_6.toPlainText()
            self.textEdit_6.setText(text)

    def set_gray_7(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_7.setTextColor(fontcolor)
            text = self.textEdit_7.toPlainText()
            self.textEdit_7.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_7.setTextColor(oricolor)
            text = self.textEdit_7.toPlainText()
            self.textEdit_7.setText(text)

    def set_gray_8(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_8.setTextColor(fontcolor)
            text = self.textEdit_8.toPlainText()
            self.textEdit_8.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_8.setTextColor(oricolor)
            text = self.textEdit_8.toPlainText()
            self.textEdit_8.setText(text)

    def set_gray_9(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_9.setTextColor(fontcolor)
            text = self.textEdit_9.toPlainText()
            self.textEdit_9.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_9.setTextColor(oricolor)
            text = self.textEdit_9.toPlainText()
            self.textEdit_9.setText(text)

    def set_gray_10(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_10.setTextColor(fontcolor)
            text = self.textEdit_10.toPlainText()
            self.textEdit_10.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_10.setTextColor(oricolor)
            text = self.textEdit_10.toPlainText()
            self.textEdit_10.setText(text)

    def set_gray_11(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_11.setTextColor(fontcolor)
            text = self.textEdit_11.toPlainText()
            self.textEdit_11.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_11.setTextColor(oricolor)
            text = self.textEdit_11.toPlainText()
            self.textEdit_11.setText(text)

    def set_gray_12(self, checked):
        if checked:
            fontcolor = QColor(230, 230, 230)
            self.textEdit_12.setTextColor(fontcolor)
            text = self.textEdit_12.toPlainText()
            self.textEdit_12.setText(text)

        else:
            oricolor = QColor(0, 0, 0)
            self.textEdit_12.setTextColor(oricolor)
            text = self.textEdit_12.toPlainText()
            self.textEdit_12.setText(text)


def main():
    app = QApplication(sys.argv)
    editor = MyWindow()
    editor.show()
    app.exec_()


if __name__ == "__main__":
    main()