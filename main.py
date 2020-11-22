import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def drawCircle(self, qp):
        qp.setPen(QColor(255, 255, 0))
        n = randint(1, 4)
        for _ in range(n):
            rad = randint(5, 200)
            qp.drawEllipse(randint(10, 800), randint(10, 600), rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
