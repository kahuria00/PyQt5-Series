import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QComboBox,QPushButton


class Combobox(QMainWindow):

	def __init__(self):
		super().__init__()

		combo = QComboBox(self)
		item_list =["Apple","Mango","Pear","Pineapple"]
		combo.addItems(item_list)
		combo.move(50,50)

		self.qlabel = QLabel(self)
		self.qlabel.move(50,16)

		combo.activated[str].connect(self.onChange)

		self.setWindowTitle("Select a Fruit")
		self.show()

	def onChange(self,text):
		self.qlabel.setText(text)
		self.qlabel.adjustSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Combobox()
	sys.exit(app.exec_())