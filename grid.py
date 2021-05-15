import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QGridLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
	app = QApplication(sys.argv)
	widget = QWidget()
	grid = QGridLayout()

	for x in range (0,5):
		for y in range(0,5):
			grid.addWidget(QPushButton(str(x)+str(y)),x,y)

	widget.setLayout(grid)
	widget.setWindowTitle("Grid")
	widget.setGeometry(50,50,300,300)
	widget.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	window()


