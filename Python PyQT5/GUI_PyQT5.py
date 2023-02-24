import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QGridLayout, QWidget, QPushButton, QScrollArea, QComboBox
from PyQt5.QtGui import QPixmap


#Creation of class MainWindow inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Ouvrir une image")
        self.setGeometry(100, 100, 800, 600)
        self.scroll_area = QScrollArea(self)
        self.setCentralWidget(self.scroll_area)
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.grid = QGridLayout(self.scroll_area_widget)
        self.widgets = []
        self.image_index = 0
        self.comboBox = QComboBox(self)
        self.comboBox.move(20, 60)
        self.comboBox.currentIndexChanged.connect(self.change_image)
        self.pushButton = QPushButton("Ouvrir un fichier", self)
        self.pushButton.move(20, 20)
        self.pushButton.clicked.connect(self.open_file)
        self.textEdit = QLabel(self)
        self.textEdit.move(600, 20)
        self.textEdit.resize(250, 150)

    def open_file(self):
        directory = QFileDialog.getExistingDirectory(self, "Ouvrir un dossier", "")
        if directory:
            self.clear_widgets()
            images = []
            for filename in os.listdir(directory):
                if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".bmp") or filename.endswith(".xpm"):
                    images.append(filename)
            if images:
                self.image_index = 0
                for i, image in enumerate(images):
                    pixmap = QPixmap(os.path.join(directory, image))
                    label = QLabel()
                    label.setPixmap(pixmap.scaled(150, 150))
                    self.grid.addWidget(label, i // 4, i % 4)
                    self.widgets.append(label)
                self.display_stats(os.path.join(directory, images[self.image_index]))
                self.comboBox.addItems(images)
            else:
                label = QLabel("Aucune image trouvée dans ce dossier.")
                self.grid.addWidget(label)


    def clear_widgets(self):
        for widget in self.widgets:
            self.grid.removeWidget(widget)
            widget.deleteLater()
        self.widgets = []
        self.comboBox.clear()

    
    def change_image(self, index):
        if self.sender() == self.comboBoxImages:
            self.image_index = index
        filename = os.path.join(os.path.dirname(self.comboBoxImages.currentText()), self.comboBoxImages.currentText())
        pixmap = QPixmap(filename)
        self.label.setPixmap(pixmap.scaled(self.label.width(), self.label.height()))
        self.display_stats(filename)

    def display_stats(self, filename):
        self.textEdit.clear()
        self.textEdit.setText(f"Nom du fichier: {os.path.basename(filename)}\n")
        self.textEdit.insertPlainText(f"Chemin absolu: {os.path.abspath(filename)}\n")
        self.textEdit.insertPlainText(f"Taille du fichier: {os.path.getsize(filename)} octets\n")
        self.textEdit.insertPlainText(f"Date de création: {os.path.getctime(filename)}\n")
        self.textEdit.insertPlainText(f"Date de dernière modification: {os.path.getmtime(filename)}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())