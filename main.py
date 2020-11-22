import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from task2.task2.UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.can_draw = False

    def paintEvent(self, event):
        if self.can_draw:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def paint(self):
        self.can_draw = True
        self.repaint()

    def drawCircle(self, qp):
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        n = randint(1, 4)
        for _ in range(n):
            rad = randint(5, 200)
            qp.drawEllipse(randint(10, 800), randint(10, 600), rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
