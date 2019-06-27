import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class NewWindow(QWidget):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.LLayout = QGridLayout()
        self.btn2 = QPushButton('Present Window')
        self.LLayout.addWidget(self.btn2)
        self.setLayout(self.LLayout)
        self.setWindowTitle('My SWindow')
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.WLayout = QGridLayout()
        self.btn = QPushButton('Next Window')
        self.btn.clicked.connect(self.windowfunction)


        self.WLayout.addWidget(self.btn)

        self.setLayout(self.WLayout)
        self.setWindowTitle('My FWindow')
        self.show()

    def windowfunction(self):
#        new_window = NewWindow() wrong way
        self.new_window = NewWindow()

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

main()