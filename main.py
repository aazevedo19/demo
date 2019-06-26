# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
# File: main.py
import sys
from forms.formpessoa import Form
from PySide2.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form('main.ui')
    sys.exit(app.exec_())
