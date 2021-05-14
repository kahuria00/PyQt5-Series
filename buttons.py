import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon,QPalette,QColor
from PyQt5.QtCore import pyqtSlot

def window():
	app = QApplication(sys.argv)
	widget = QWidget()



	redbutton = QPushButton (widget)
	redbutton.setText("Reset")
	redbutton.move (64,32)
	redbutton.setStyleSheet("background-color: red")
	redbutton.clicked.connect(redbutton_clicked)


	greenbutton = QPushButton (widget)
	greenbutton.setText("save")
	greenbutton.move (64,64)
	greenbutton.setStyleSheet("background-color: green")
	greenbutton.clicked.connect(greenbutton_clicked)

	widget.setGeometry(50,50,320,200)
	widget.setWindowTitle("Buttons")
	widget.show()
	sys.exit(app.exec_())

def redbutton_clicked():
	print("Reset button clicked")

def greenbutton_clicked():
	print("save button clicked")

if __name__ == '__main__':
	window()







