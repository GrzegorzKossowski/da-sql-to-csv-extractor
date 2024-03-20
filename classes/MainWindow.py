from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QPushButton, QPlainTextEdit, QLabel, QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QToolBar
from classes.SchemaWindow import SchemaWindow 
from tools import save_csv_file

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.w = SchemaWindow()

    # toolbar
    self.toolbar = QToolBar('Main toolbar')

    # labels
    textEditorLabel = QLabel('SQL query:')
    folderLabel = QLabel('CSV Filename: */csvs/')
    fileExtLabel = QLabel('.csv')

    # text inputs
    self.queryEdit = QPlainTextEdit()
    self.filenameInput = QLineEdit()

    # RUN Query button
    self.runQueryBnt = QPushButton('RUN')
    self.runQueryBnt.setEnabled(False)
    self.runQueryBnt.clicked.connect(self.query_btn_action)
    self.runQueryBnt.setStatusTip('Save csv file based on SQL query')

    # Show DB Schema Button
    self.showDbSchemaBtn = QPushButton('Schema')
    self.showDbSchemaBtn.clicked.connect(self.toggleSchemaVisibility)

    # Query Font Resize Buttons
    self.queryFontZoomIn = QPushButton('aA+')
    self.queryFontZoomOut = QPushButton('Aa-')
    self.queryFontZoomIn.clicked.connect(lambda: self.queryEdit.zoomIn(1))
    self.queryFontZoomOut.clicked.connect(lambda: self.queryEdit.zoomOut(1))

    # -------------
    reg_ex = QRegExp("^[0-9a-zA-Z_-]{5,32}$")
    input_validator = QRegExpValidator(reg_ex, self.filenameInput)
    self.filenameInput.setValidator(input_validator)
    self.filenameInput.textChanged.connect(self.text_changed)
    self.filenameInput.setStatusTip('Csv filename. 5-32 characters (a-zA-Z_-). No spaces.')

    # topBoxLayout
    topBoxLayout = QHBoxLayout()
    topBoxLayout.addWidget(self.queryFontZoomIn)
    topBoxLayout.addWidget(self.queryFontZoomOut)
    topBoxLayout.addWidget(textEditorLabel)
    topBoxLayout.addStretch()
    topBoxLayout.addWidget(self.showDbSchemaBtn)

    # filePathLayout
    filePathLayout = QHBoxLayout()
    filePathLayout.addWidget(folderLabel)
    filePathLayout.addWidget(self.filenameInput)
    filePathLayout.addWidget(fileExtLabel)
    filePathLayout.addWidget(self.runQueryBnt)

    # mainBoxLayout
    mainBoxLayout = QVBoxLayout()
    mainBoxLayout.addLayout(topBoxLayout)
    mainBoxLayout.addWidget(self.queryEdit)
    mainBoxLayout.addLayout(filePathLayout)

    # main widget
    widget = QWidget()
    widget.setLayout(mainBoxLayout)
    self.setCentralWidget(widget)
    self.setWindowTitle("SQL to CSV extractor")
    self.setMinimumSize(QSize(640,480))
    self.setMaximumSize(QSize(800,600))
  
  def closeEvent(self, event):
    if self.w:
      self.w.close()

  def toggleSchemaVisibility(self):
    if self.w.isVisible():
      self.w.hide()
    else:
      self.w.show()

  def query_btn_action(self):
    save_csv_file(self.filenameInput.text(), self.queryEdit.toPlainText())
    self.filenameInput.clear()
    self.queryEdit.clear()

  def text_changed(self):
    if self.filenameInput.hasAcceptableInput() and self.filenameInput.text():
      self.runQueryBnt.setEnabled(True)
    else:
      self.runQueryBnt.setEnabled(False)
