from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout

class SchemaWindow(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout(self)
    self.setLayout(layout)
    # Załaduj obraz
    self.pixmap = QPixmap("img/northwind.png")
    # Utwórz QLabel, aby wyświetlić obraz
    self.label = QLabel(self)
    self.label.setAlignment(Qt.AlignCenter)  # Wyśrodkuj obraz wewnątrz QLabel
    # Dodaj QLabel do layoutu
    layout.addWidget(self.label)
    self.setWindowTitle('Obraz w PyQt5')
    self.setGeometry(0, 0, 1152, 743)  # Ustawienie początkowych rozmiarów okna

  def resizeEvent(self, event):
        # Przeskaluj obraz, gdy okno zostanie zmienione
        scaled_pixmap = self.pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.label.adjustSize()  # Dostosuj rozmiar QLabel do rozmiaru obrazu
