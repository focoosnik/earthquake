import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window
        self.setWindowTitle('Information about earthquake')
        self.setMinimumWidth(350)
        self.setMaximumWidth(350)
        self.setMinimumHeight(200)
        self.setMaximumHeight(200)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.statusBar().showMessage('Ready')
        # Start time
        self.lblStarttime = QLabel('Start time', self)
        self.lblStarttime.setFont(QFont('Cali', 10))
        self.lblStarttime.move(10, 0)

        self.dStarttime = QDateEdit(QDate().currentDate(), self)
        self.dStarttime.move(10, 25)
        self.dStarttime.setCalendarPopup(True)

        self.dStarttime.dateChanged.connect(self.LimitStartTime)
        # End time
        self.lblEndtime = QLabel('End time', self)
        self.lblEndtime.setFont(QFont('Cali', 10))
        self.lblEndtime.move(10, 60)

        self.dEndtime = QDateEdit(QDate().currentDate(), self)
        self.dEndtime.move(10, 85)
        self.dEndtime.setCalendarPopup(True)

        self.dEndtime.dateChanged.connect(self.LimitEndTime)
        # Checkbox 'show results'
        self.cbShowres = QCheckBox('Snow results in window', self)
        self.cbShowres.toggle()
        self.cbShowres.move(140, 120)
        self.cbShowres.setMinimumWidth(150)
        # Line edit latitude
        self.lblLat = QLabel('Latitude', self)
        self.lblLat.setFont(QFont('Cali', 10))
        self.lblLat.setMinimumWidth(120)
        self.lblLat.move(140, 0)

        self.latValidator = QDoubleValidator(self)
        self.latValidator.setRange(-90, 90)
        self.latValidator.setNotation(QDoubleValidator.StandardNotation)
        self.latValidator.setDecimals(6)

        self.leLat = QLineEdit('43,34', self)
        self.leLat.move(140, 25)
        self.leLat.setValidator(self.latValidator)

        #self.leLat.textChanged.connect(self.LimitLat)
        # Line edit longitude
        self.lblLong = QLabel('Longitude', self)
        self.lblLong.setFont(QFont('Cali', 10))
        self.lblLong.setMinimumWidth(120)
        self.lblLong.move(140, 60)

        self.longValidator = QDoubleValidator(self)
        self.longValidator.setRange(-180, 180)
        self.longValidator.setNotation(QDoubleValidator.StandardNotation)
        self.longValidator.setDecimals(6)

        self.leLong = QLineEdit('42,43', self)
        self.leLong.move(140, 85)
        self.leLong.setValidator(self.longValidator)
        #self.leLong.textChanged.connect(self.LimitLong)
        # Line edit Maxradiuskm
        self.lblMaxrad = QLabel('Max. radius km', self)
        self.lblMaxrad.setFont(QFont('Cali', 10))
        self.lblMaxrad.setMinimumWidth(120)
        self.lblMaxrad.move(10, 120)

        self.radValidator = QIntValidator(self)
        self.radValidator.setRange(0, 20000)

        self.leMaxrad = QLineEdit('6000', self)
        self.leMaxrad.move(10, 145)
        self.leMaxrad.setValidator(self.radValidator)
        #self.leMaxrad.textChanged.connect(self.LimitMaxrad)
        # Get data button
        self.btnGet = QPushButton('Get data', self)
        self.btnGet.move(140, 145)
        self.btnGet.setStyleSheet("background-color: #99ff99")
        # Min magnitude
        self.lblMinMag = QLabel('Mag. > 0', self)
        self.lblMinMag.setFont(QFont('Cali', 10))
        self.lblMinMag.setMinimumWidth(120)
        self.lblMinMag.move(270, 0)

        self.cldMinMag = QSlider(Qt.Vertical, self)
        self.cldMinMag.setMinimumHeight(140)
        self.cldMinMag.setMaximumWidth(25)
        self.cldMinMag.setMaximum(90)
        self.cldMinMag.move(280, 35)
        self.cldMinMag.setTickPosition(2)
        self.cldMinMag.sliderMoved.connect(self.MinMag)


    def MinMag(self, value):
        self.lblMinMag.setText(f'Mag. > {str(value/10)}')


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

    def LimitLat(self, value):
        fvalue = float(value)
        if fvalue > 90:
            pass

    def LimitLong(self, value):
        fvalue = float(value)
        if fvalue > 90:
            pass

    def LimitMaxrad(self, value):
        fvalue = float(value)
        if fvalue > 90:
            pass


if __name__ == '__main__':
    app_main = QApplication(sys.argv)
    mainform = MainForm()
    mainform.show()
    sys.exit(app_main.exec_())
