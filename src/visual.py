# Kelby Hubbard
# Started: 2022-02-13
# Updated: 
# visual.py
#
# Main source file for PyPasswordGenerator

# GUI for PyPasswordGenerator

from .generate import random_password
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QGridLayout,
    QCheckBox,
    QLineEdit,
    QSlider,
    QLabel,
    QVBoxLayout,
)

# Main Window
class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PyPasswordGenerator")
        self.setFixedSize(650,200)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QGridLayout()
        self.centralWidget.setLayout(self.layout)
        self.initUI()

    # Initialize main window UI
    def initUI(self):

        # Line edit
        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)

        # Check boxes
        self.lowercaseCheckBox = QCheckBox('Lowercase (abc)')
        self.lowercaseCheckBox.setChecked(True)
        self.uppercaseCheckBox = QCheckBox('Uppercase (ABC)')
        self.uppercaseCheckBox.setChecked(True)
        self.symbolCheckBox = QCheckBox('Symbols (!@#$%^&*(){}')
        self.symbolCheckBox.setChecked(True)

        # Length slider
        self.lengthSlider = QSlider(Qt.Horizontal)
        self.lengthSlider.setMinimum(8)
        self.lengthSlider.setMaximum(24)
        self.lengthSlider.valueChanged.connect(self.updateLabel)
        value = self.lengthSlider.value()

        # Slider value label
        self.label = QLabel('Length: ' + str(value), self)  
        self.label.setAlignment(Qt.AlignCenter)

        # Slider and slider value sublayout
        self.subLayout = QVBoxLayout()
        self.subLayout.addWidget(self.lengthSlider)
        self.subLayout.addWidget(self.label)

        # Generate button
        self.generateButton = QPushButton('Generate')
        self.generateButton.clicked.connect(lambda: self.setLineEditText(random_password(self.lowercaseCheckBox.isChecked(), self.uppercaseCheckBox.isChecked(), self.symbolCheckBox.isChecked(), self.lengthSlider.value())))

        # Layout
        self.layout.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.layout.addWidget(self.generateButton, 0, 3)
        self.layout.addWidget(self.lowercaseCheckBox, 1, 0)
        self.layout.addWidget(self.uppercaseCheckBox, 1, 1)
        self.layout.addWidget(self.symbolCheckBox, 1, 2)
        self.layout.addLayout(self.subLayout, 1, 3)

    # Update slider label value
    def updateLabel(self, value):
        self.label.setText('Length: ' + str(value))

    # Generate Password
    def setLineEditText(self, string):
        self.lineEdit.setText(string)
