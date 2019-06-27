# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
# File: main.py
import sys
from menu import Form
from PySide2.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form('ui/menu.ui')
    sys.exit(app.exec_())
