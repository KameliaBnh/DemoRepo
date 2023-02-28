import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QMenu
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("interface.ui", self)
        self.setWindowTitle("Automated Pollinator Monitoring")

        # Get the "Open File" QAction from the QMenuBar
        open_action = self.menuBar().findChild(QMenu, "Open")
        open_file_action = open_action.findChild(QAction, "OpenFile")
        open_file_action.triggered.connect(self.open_file)

    def open_file(self):
        # Open a file dialog and get the selected file path
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            # Load the selected image and display it
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loadUi("interface.ui")
    window.show()
    sys.exit(app.exec_())