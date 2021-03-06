#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from board import Board

class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        """
        获得显示器分辨率，将本应用移动到桌面中央
        """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move( (screen.width() - size.width()) / 2,
                   (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    import sys
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
