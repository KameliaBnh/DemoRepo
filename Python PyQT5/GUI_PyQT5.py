import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("interface.ui", self)
        self.setWindowTitle("Automated Pollinator Monitoring")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loadUi("interface.ui")
    window.show()
    sys.exit(app.exec_())