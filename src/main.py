# Kelby Hubbard
# Started: 2022-02-13
# Updated: 
# main.py
#
# Main source file for PyPasswordGenerator

import sys

from PyQt5.QtWidgets import QApplication
from .visual import Window

# Main function for PyPasswordGenerator
def main():
    # Create PyQT application
    app = QApplication(sys.argv)
    # Create PyQT main window
    main_window = Window()
    main_window.show()
    # Main Loop
    sys.exit(app.exec())