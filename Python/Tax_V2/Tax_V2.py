from os import name
from PyQt5.QtWidgets import(
    QApplication, QWidget, QFormLayout,
    QPushButton, QLabel, QLineEdit, QMenuBar,
    QAction, QFileDialog, QMessageBox
)

def calculateTi(textWidget, textWidgett, textWidgettt, nti, agi):
    if nti and agi:
        if nti.isnumeric() and agi.isnumeric():
            ti = int(agi) - int(nti)
            textWidgett.setText(str(agi))
            textWidgettt.setText(str(nti))
            textWidget.setText(str(ti))

def calculateTax(textWidget, nti, agi):
    if nti.isnumeric() and agi.isnumeric():
        ti = int(agi) - int(nti)
        if ti > 0:
            if ti <= 50000000:
                tax = ti * 5 / 100
                textWidget.setText(str(tax))
            elif ti > 50000000 & ti <= 250000000:
                tax = (5 / 100 * 50000000) + ((ti - 50000000) * 15 / 100)
                textWidget.setText(str(tax))
            elif ti > 250000000 & ti <= 500000000:
                tax = (5 / 100 * 50000000) + (15 / 100 * 200000000) 
                + ((ti - 250000000) * 25 / 100)
                textWidget.setText(str(tax))
            elif ti > 500000000:
                tax = (5 / 100 * 50000000) + (15 / 100 * 200000000) 
                + (25 / 100 * 250000000) + ((ti - 500000000) * 30 / 100)
                textWidget.setText(str(tax))
        else:
            textWidget.setText(str(0))
    else:
        textWidget.setText("Enter numbers please!")

class Window(QWidget):
    def save(self):
        name, _ = QFileDialog.getSaveFileName(
            self, "Save", self.fileName, 'TXT (*.txt)'
        )
        if name:
            self.fileName = name
            file = open(name, 'w')
            textAGI = self.AGI.text()
            textNTI = self.NTI.text()
            file.write(textAGI + '\n')
            file.write(textNTI)
            file.close()
    
    def open(self):
        name, _ = QFileDialog.getOpenFileName(
            self, "Load", "", 'TXT (*.txt)'
            )
        if name:
            self.fileName = name
            file = open(name, 'r')
            with file:
                textAGI = file.readline().rstrip('\n')
                textNTI = file.readline()
                self.AGI.setText(textAGI)
                self.NTI.setText(textNTI)
            calculateTi(
                self.TI, self.valueAGI, self.valueNTI, 
                self.NTI.text(), self.AGI.text()
            )
            calculateTax(
                self.Tax, self.NTI.text(), self.AGI.text()
            )
    
    def quit(self):
        QApplication.quit()
    
    def about(self):
        msg = QMessageBox()
        msg.setWindowTitle("AMOGUS")
        msg.setIcon(QMessageBox.Information)
        msg.setText("when the impostor is sus")
        msg.setInformativeText(
            "⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌\n⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌\n" + 
            "⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪\n" + 
            "⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐\n" + 
            "⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘\n" + 
            "⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗\n" + 
            "⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟\n" + 
            "⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊\n" + 
            "⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁\n" + 
            "⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀\n" + 
            "⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾\n" + 
            "⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽"
        )
        msg.setDetailedText(
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⠿⠛⠿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠄⣀⡤⢤⣤⣈⠁⣠⡔⠶⣾⣿\n" +
            "⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠁⠄⠄⠄⣼⣿⠁⡀⢹⣿⣷⢹⡇⠄⠎⣿\n⣿⣿⣿⠿⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠹⣇⣀⣡⣾⣿⡿⠉⠛⠒⠒⠋\n" +
            "⡿⠋⠁⠄⠄⢀⣤⣤⡀⠄⠄⠄⠄⠄⠄⠈⠙⠛⠛⠉⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⢹⣧⡈⠿⣷⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠\n" +
            "⠄⠄⠄⠄⠄⠈⠻⢿⣶⣌⣙⡛⠛⠿⠶⠶⠶⠶⠶⠖⣒⣒⣚⣋⡩⢱\n⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠛⠛⠛⠻⠿⠿⠟⠛⠛⠛⠉⢉⣥⣶⣾⣿\n" +
            "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠒⠶⣿⣿⣿⣿⣿⣿"
        )
        msg.setStandardButtons(QMessageBox.Yes)
        msg.exec_()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Tax Calculator V2")
        self.resize(300, 200)
        self.fileName = ""

        self.menubar = QMenuBar()
        self.menubar.setNativeMenuBar(False)
        self.fileMenu = self.menubar.addMenu('File')
        self.helpMenu = self.menubar.addMenu('Help')
        self.menubar.show()

        self.actionSave = QAction('Save', self)
        self.actionOpen = QAction('Open', self)
        self.actionQuit = QAction('Quit', self)
        self.actionAbout = QAction('About', self)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionQuit.setShortcut('Ctrl+Q')
        self.fileMenu.addAction(self.actionSave)
        self.fileMenu.addAction(self.actionOpen)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionQuit)
        self.helpMenu.addAction(self.actionAbout)
        
        self.actionSave.triggered.connect(self.save)
        self.actionOpen.triggered.connect(self.open)
        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout.triggered.connect(self.about)

        self.labelAGI = QLabel("Annual Income : ")
        self.AGI = QLineEdit()
        self.AGI.setPlaceholderText("Enter Value")
        self.labelNTI = QLabel("Non-Taxable Income : ")
        self.NTI = QLineEdit()
        self.NTI.setPlaceholderText("Enter Value")
        self.button = QPushButton("Calculate Tax")
        self.labelLabelAGI = QLabel("Annual Income : ")
        self.valueAGI = QLabel()
        self.valueAGI.setText("0")
        self.labelLabelNTI = QLabel("Non-Taxable Income : ")
        self.valueNTI = QLabel()
        self.valueNTI.setText("0")
        self.labelTI = QLabel("Taxable Income : ")
        self.TI = QLabel()
        self.TI.setText("0")
        self.labelTax = QLabel("Tax : ")
        self.Tax = QLabel()
        self.Tax.setText("0")
        
        self.button.clicked.connect(
           lambda: calculateTi(self.TI, self.valueAGI, self.valueNTI, 
           self.NTI.text(), self.AGI.text())
        )
        self.button.clicked.connect(
           lambda: calculateTax(self.Tax, self.NTI.text(), self.AGI.text())
        )
        
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.layout.addRow(self.menubar)
        self.layout.addRow(self.labelAGI, self.AGI)
        self.layout.addRow(self.labelNTI, self.NTI)
        self.layout.addRow(self.button)
        self.layout.addRow(self.labelLabelAGI, self.valueAGI)
        self.layout.addRow(self.labelLabelNTI, self.valueNTI)
        self.layout.addRow(self.labelTI, self.TI)
        self.layout.addRow(self.labelTax, self.Tax)

app = QApplication([])

window = Window()
window.show()

app.exec_()

