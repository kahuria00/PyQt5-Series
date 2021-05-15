import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QGridLayout,QWidget
from PyQt5.QtGui import QPixmap

class Pixmapexample(QWidget):

	def __init__(self):
		super().__init__()


		self.image = QPixmap("/home/charity/Documents/CS5/buttons.jpg")
		self.label = QLabel()
		self.label.setPixmap(self.image)

		self.grid = QGridLayout()
		self.grid.addWidget(self.label,1,1)
		self.setLayout(self.grid)

		self.setGeometry(50,50,320,200)
		self.setWindowTitle("show image")
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Pixmapexample()
	sys.exit(app.exec_())