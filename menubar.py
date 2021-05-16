import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setLayout(layout)


		menubar = QMenuBar()
		layout.addWidget(menubar,0,0)
		actionFile = menubar.addMenu("File")
		actionFile.addAction("New")
		actionFile.addAction("Open")
		actionFile.addAction("Save")
		actionFile.addSeparator()
		actionFile.addAction("Quit")

		menubar.addMenu("Edit")
		menubar.addMenu("View")
		menubar.addMenu("Help")

		textbox = QPlainTextEdit()
		layout.addWidget(textbox,1,0)

		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = Window()
	screen.show()
	sys.exit(app.exec_())