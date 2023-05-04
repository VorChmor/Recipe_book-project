from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('path/to/default/image'))
        self.label.setScaledContents(True)
        self.label.mousePressEvent = self.selectImage
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Select Image Example')
        self.show()
    
    def selectImage(self, event):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image Files (*.png *.jpg *.bmp)')
        if fileName:
            self.label.setPixmap(QPixmap(fileName))


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec()