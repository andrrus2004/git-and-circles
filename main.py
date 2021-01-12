import sys
from UI import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.create_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_square(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_square(self, qp):
        x, y = randint(10, 490), randint(10, 490)
        radius = randint(5, min(495 - x, 495 - y))
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
