from PyQt5.QtWidgets import(
    QApplication, QWidget, QFormLayout,
    QPushButton, QLabel, QLineEdit
)

def calculateTi(textWidget, nti, agi):
    if nti and agi:
        if nti.isnumeric() and agi.isnumeric():
            ti = int(agi) - int(nti)
            textWidget.setText(str(ti))
        else:
            textWidget.setText("Enter numbers please!")

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


def main():
    app = QApplication([])
    window = QWidget()

    layout = QFormLayout()
    label_nti = QLabel("Non-Taxable Income")
    label_agi = QLabel("Annual Income")
    label_ti = QLabel("Taxable Income : ")
    ti = QLabel()
    label_tax = QLabel("Tax : ")
    tax = QLabel()
    nti = QLineEdit()
    agi = QLineEdit()

    button = QPushButton("Calculate Tax")
    button.clicked.connect(
        lambda: calculateTi(ti, nti.text(), agi.text())
    )
    button.clicked.connect(
        lambda: calculateTax(tax, nti.text(), agi.text())
    )
    
    layout.addRow(label_agi, agi)
    layout.addRow(label_nti, nti)
    layout.addRow(button)
    layout.addRow(label_ti, ti)
    layout.addRow(label_tax, tax)

    window.setWindowTitle("Tax Calculator")
    window.setLayout(layout)
    window.show()
    app.exec_()

main()