# https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/#menu
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys
import colors
from classes.MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
colors.prGreen('Bye!')