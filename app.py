import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUiType

from dj_ripper_ui import Ui_MainWindow

baseUIClass, baseUIWidget = loadUiType("ui/dj_ripper.ui")


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

    @staticmethod
    def browseButtonHandler():
        print("Sopie")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window(None)
    win.show()
    sys.exit(app.exec())
