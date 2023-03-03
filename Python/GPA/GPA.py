#READ ME
#yes the program does accept number > 100
#i dont know how to stop it
#ive tried a plenty of methods and none work
# p a i n

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):
    def addRow(self):
        rowCount = self.table.rowCount()
        self.table.insertRow(rowCount)

    def calculateGPA(self):
        global gpa
        credits = 0
        for row in range(0, self.table.rowCount()):
            crData = self.table.item(row, 1)
            if crData:
                cred = int(crData.text())
                if 0 <= cred <= 100:
                    credits += 3.00
                else:
                    credits += 0.00
        self.creditInput.setText(str(credits))

        a = 0
        aMin = 0
        bPlus = 0
        b = 0
        bMin = 0
        cPlus = 0
        c = 0
        d = 0
        e = 0
        for row in range(0, self.table.rowCount()):
            score = self.table.item(row, 1)
            if score:
                scData = float(score.text())
                if 0 <= scData <= 100:
                    if scData >= 85:
                        a += 1
                    elif scData > 79:
                        aMin += 1
                    elif scData > 74:
                        bPlus += 1
                    elif scData > 69:
                        b += 1
                    elif scData > 66:
                        bMin += 1
                    elif scData > 63:
                        cPlus += 1
                    elif scData > 59:
                        c += 1
                    elif scData > 54:
                        d += 1
                    else:
                        e += 1
                else:
                    a += 0
                    aMin += 0
                    bPlus += 0
                    b += 0
                    bMin += 0
                    cPlus += 0
                    c += 0
                    d += 0
                    e += 0

        self.aInput.setText(str(a))
        self.aMininput.setText(str(aMin))
        self.bPlusinput.setText(str(bPlus))
        self.bInput.setText(str(b))
        self.bMininput.setText(str(bMin))
        self.cPlusinput.setText(str(cPlus))
        self.cInput.setText(str(c))
        self.dInput.setText(str(d))
        self.eInput.setText(str(e))

        totalIndex = ((a * 4.00 * 3) + (aMin * 3.67 * 3) + (bPlus * 3.33 * 3) + (b * 3 * 3) + (bMin * 2.67 * 3) + (cPlus * 2.33 * 3) + (c * 2 * 3) + (d * 1 * 3))
        self.indexInput.setText(str(float('%.2f' %totalIndex)))

        if totalIndex > 0:
            if credits > 0:
                gpa = float(totalIndex) / float(credits)
        else:
            gpa = 0.00

        self.GPAInput.setText(str(float('%.2f' %gpa)))

    def onChange(self, item):
        row = item.row()
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText('')

    def info(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Created in collaboration with :\n" + 
                    "PurpleSparkle a.k.a Salsabyla Azkyannisa Putri\n\n" + 
                    "Pawas x Caca"
        )
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("GPA Calculator")
        self.resize(500, 500)

        self.menubar = QMenuBar()
        self.menubar.setNativeMenuBar(False)
        self.helpMenu = self.menubar.addMenu('About')
        self.menubar.show()

        self.actionInfo = QAction('Info', self)
        self.helpMenu.addAction(self.actionInfo)

        self.actionInfo.triggered.connect(self.info)

        self.buttonAdd = QPushButton("Add Subject")
        self.buttonGPA = QPushButton("Calculate GPA (Credit Scale : 3)")
        self.blank = QLabel('')
        self.a = QLabel('A \t\t: ')
        self.aInput = QLabel('')
        self.aMin = QLabel('A-\t\t: ')
        self.aMininput = QLabel('')
        self.bPlus = QLabel('B+\t\t: ')
        self.bPlusinput = QLabel('')
        self.b = QLabel('B\t\t: ')
        self.bInput = QLabel('')
        self.bMin = QLabel('B-\t\t: ')
        self.bMininput = QLabel('')
        self.cPlus = QLabel('C+\t\t: ')
        self.cPlusinput = QLabel('')
        self.c = QLabel('C\t\t: ')
        self.cInput = QLabel('')
        self.d = QLabel('D\t\t: ')
        self.dInput = QLabel('')
        self.e = QLabel('E\t\t: ')
        self.eInput = QLabel('')
        self.blank2 = QLabel('')
        self.index = QLabel('Total Index\t: ')
        self.indexInput = QLabel('')
        self.credit = QLabel('Total Credit\t: ')
        self.creditInput = QLabel('')
        self.GPA = QLabel('GPA\t\t: ')
        self.GPAInput = QLabel('')

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Subject', 'Score (0 - 100)'])
        self.table.resize(600, 600)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.layout.addRow(self.menubar)
        self.layout.addRow(self.buttonAdd)
        self.layout.addRow(self.table)
        self.layout.addRow(self.buttonGPA)
        self.layout.addRow(self.blank)
        self.layout.addRow(self.a, self.aInput)
        self.layout.addRow(self.aMin, self.aMininput)
        self.layout.addRow(self.bPlus, self.bPlusinput)
        self.layout.addRow(self.b, self.bInput)
        self.layout.addRow(self.bMin, self.bMininput)
        self.layout.addRow(self.cPlus, self.cPlusinput)
        self.layout.addRow(self.c, self.cInput)
        self.layout.addRow(self.d, self.dInput)
        self.layout.addRow(self.e, self.eInput)
        self.layout.addRow(self.blank2)
        self.layout.addRow(self.index, self.indexInput)
        self.layout.addRow(self.credit, self.creditInput)
        self.layout.addRow(self.GPA, self.GPAInput)

        self.buttonAdd.clicked.connect(self.addRow)
        self.buttonGPA.clicked.connect(self.calculateGPA)
        self.table.itemChanged.connect(self.onChange)

app = QApplication([])

window = Window()
window.show()

app.exec_()