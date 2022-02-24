import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Data about earthquake')
        self.resize(300, 200)
        self.setp

        self.lblStarttime = QLabel('Start time', self)
        self.lblStarttime.setFont(QFont('Cali', 10))
        self.lblStarttime.move(10, 25)

        self.dStarttime = QDateTimeEdit(QDate().currentDate(), self)
        self.dStarttime.move(50, 50)
        self.dStarttime.setCalendarPopup(True)

        self.dEndtime = QDateTimeEdit(QDate().currentDate(), self)
        self.dEndtime.move(50, 150)
        self.dEndtime.setCalendarPopup(True)



if __name__ == '__main__':
    app_main = QApplication(sys.argv)
    mainform = MainForm()
    mainform.show()
    sys.exit(app_main.exec_())
