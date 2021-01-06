import sys

import random as r
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.do_paint = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_ell(qp)
        qp.end()
        self.do_paint = False

    def draw_ell(self, qp):
        qp.setBrush(QColor('yellow'))
        rad = r.randrange(self.geometry().x())
        qp.drawEllipse(r.randrange(self.geometry().x()), r.randrange(self.geometry().y()), rad, rad)

    def draw(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
