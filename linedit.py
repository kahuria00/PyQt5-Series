import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QLabel

class Lineedit(QMainWindow):

	def  __init__(self):
		super().__init__()

		self.lineEntry = QLineEdit(self)
		self.lineEntry.move(20,20)
		self.lineEntry.resize(220,60)

		self.qlabel =QLabel(self)
		self.qlabel.move(20,68)

		self.lineEntry.textChanged.connect(self.onChange)

		self.setGeometry(50,50,320,200)
		self.setWindowTitle("Line Edit")
		self.show()

	def onChange(self,text):
		self.qlabel.setText(text)
		self.qlabel.adjustSize()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Lineedit()
	sys.exit(app.exec_())

