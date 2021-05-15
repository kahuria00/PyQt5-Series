import sys
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
	app =QApplication(sys.argv)
	widget = QWidget()
	button =QPushButton(widget)
	button.setText("show dialog")
	button.move (50,50)
	button.clicked.connect(showDialog)
	widget.setWindowTitle("Click here")
	widget.show()
	sys.exit(app.exec_())

def showDialog():
	msgBox = QMessageBox()
	msgBox.setIcon(QMessageBox.Information)
	msgBox.setText("if you are seeing this it's working!")
	msgBox.setWindowTitle("Alert!")
	msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	msgBox.buttonClicked.connect(msgButtonClick)

	returnValue = msgBox.exec()
	if returnValue == QMessageBox.Ok:
		print("OK clicked")

def msgButtonClick(i):
	print("Button clicked is:",i.text())


if __name__ == "__main__":
	window()
