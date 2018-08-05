#-*- coding:utf-8 -*-
from PyQt5.QtGui import QPainter, QColor, QFont,  QPolygon
from PyQt5.QtCore import Qt, QRect, QLine, QRectF,  QPoint
from PyQt5.QtWidgets import QApplication, QWidget

class PyQt5_Paint(QWidget):
    def __init__(self):
        super(PyQt5_Paint, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('PyQt5_Temp')

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setFont(QFont("Arial", 30))
        p.setPen(QColor(162, 39, 43))
        p.setBrush(QColor(88, 99, 100))
        p.drawLine(QLine(10, 10, 30, 30))

        p.drawPie(QRect(100, 150, 200, 200), 30*2, 120*16)
        p.end()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    ui = PyQt5_Paint()
    ui.show()
    sys.exit(app.exec_())
