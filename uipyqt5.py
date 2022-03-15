import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window
        self.setWindowTitle('Data about earthquake')
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        self.setWindowIcon(QIcon('icon.jpg'))
        # Start time
        self.lblStarttime = QLabel('Start time', self)
        self.lblStarttime.setFont(QFont('Cali', 10))
        self.lblStarttime.move(10, 0)

        self.dStarttime = QDateEdit(QDate().currentDate(), self)
        self.dStarttime.move(20, 25)
        self.dStarttime.setCalendarPopup(True)

        self.dStarttime.dateChanged.connect(self.LimitStartTime)
        # End time
        self.lblEndtime = QLabel('End time', self)
        self.lblEndtime.setFont(QFont('Cali', 10))
        self.lblEndtime.move(10, 55)

        self.dEndtime = QDateEdit(QDate().currentDate(), self)
        self.dEndtime.move(20, 80)
        self.dEndtime.setCalendarPopup(True)

        self.dEndtime.dateChanged.connect(self.LimitEndTime)
        # Checkbox 'show results'
        self.cbShowres =QCheckBox('Snow results in window', self)
        self.cbShowres.toggle()
        self.cbShowres.move(140, 0)
        self.cbShowres.setMinimumWidth(150)

        #self.cbShowres.stateChanged.connect()
        # Get data button
        self.btnGet = QPushButton('Get data', self)
        self.btnGet.move(140, 150)

        #self.getBtn.clicked.connect(self.setColor)
        # Min magnitude
        self.lblMinMag = QLabel('Min magnitude = 0', self)
        self.lblMinMag.setFont(QFont('Cali', 10))
        self.lblMinMag.setMinimumWidth(120)
        self.lblMinMag.move(10, 110)

        self.cldMinMag = QSlider(Qt.Horizontal, self)
        self.cldMinMag.setMaximum(90)
        self.cldMinMag.move(20, 130)
        self.cldMinMag.setTickPosition(2)
        self.cldMinMag.sliderMoved.connect(self.MinMag)


    def MinMag(self, value):
        self.lblMinMag.setText(f'Min magnitude {str(value/10)}')


    def LimitEndTime(self, date):
        limit = QDate().currentDate()
        if date > limit:
            self.dEndtime.setDate(limit)
        elif date<self.dStarttime.date():
            self.dStarttime.setDate(date)


    def LimitStartTime(self, data):
        limit = self.dEndtime.date()
        if data > limit:
            self.dStarttime.setDate(limit)

if __name__ == '__main__':
    app_main = QApplication(sys.argv)
    mainform = MainForm()
    mainform.show()
    sys.exit(app_main.exec_())
