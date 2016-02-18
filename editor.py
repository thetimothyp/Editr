import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtPrintSupport
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.filename = ""
		self.initUI()

	def initToolbar(self):
		self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"), "New Blank Document", self)
		self.newAction.setStatusTip("Create a new document.")
		self.newAction.setShortcut("Ctrl+N")
		self.newAction.triggered.connect(self.new)

		self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"), "Open...", self)
		self.openAction.setStatusTip("Open existing document")
		self.openAction.setShortcut("Ctrl+O")
		self.openAction.triggered.connect(self.open)

		self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save.png"), "Save", self)
		self.saveAction.setStatusTip("Save document")
		self.saveAction.setShortcut("Ctrl+S")
		self.saveAction.triggered.connect(self.save)

		self.saveAsAction = QtWidgets.QAction("Save As...", self)
		self.saveAsAction.setShortcut("Ctrl+Shift+S")
		self.saveAsAction.triggered.connect(self.saveAs)

		self.printAction = QtWidgets.QAction(QtGui.QIcon("icons/print.png"), "Print...", self)
		self.printAction.setStatusTip("Print document")
		self.printAction.setShortcut("Ctrl+P")
		self.printAction.triggered.connect(self.printDoc)

		self.previewAction = QtWidgets.QAction(QtGui.QIcon("icons/preview.png"), "Print Preview", self)
		self.previewAction.setStatusTip("Preview page before printing")
		self.previewAction.setShortcut("Ctrl+Shift+P")
		self.previewAction.triggered.connect(self.preview)

		self.cutAction = QtWidgets.QAction("Cut", self)
		self.cutAction.setShortcut("Ctrl+X")
		self.cutAction.triggered.connect(self.text.cut)

		self.copyAction = QtWidgets.QAction("Copy", self)
		self.copyAction.setShortcut("Ctrl+C")
		self.copyAction.triggered.connect(self.text.copy)

		self.pasteAction = QtWidgets.QAction("Paste", self)
		self.pasteAction.setShortcut("Ctrl+V")
		self.pasteAction.triggered.connect(self.text.paste)

		self.undoAction = QtWidgets.QAction("Undo", self)
		self.undoAction.setShortcut("Ctrl+Z")
		self.undoAction.triggered.connect(self.text.undo)

		self.redoAction = QtWidgets.QAction("Redo", self)
		self.redoAction.setShortcut("Ctrl+Y")
		self.redoAction.triggered.connect(self.text.redo)

		bulletAction = QtWidgets.QAction(QtGui.QIcon("icons/bullet.png"), "Insert bullet list", self)
		bulletAction.setStatusTip("Insert bullet list")
		bulletAction.setShortcut("Ctrl+Shift+B")
		bulletAction.triggered.connect(self.bulletList)

		numberedAction = QtWidgets.QAction(QtGui.QIcon("icons/number.png"), "Insert numbered list", self)
		numberedAction.setStatusTip("Insert numbered list")
		numberedAction.setShortcut("Ctrl+Shift+L")
		numberedAction.triggered.connect(self.numberList)

		self.toolbar = self.addToolBar("Options")

		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)
		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)
		self.toolbar.addAction(bulletAction)
		self.toolbar.addAction(numberedAction)

		self.toolbar.addSeparator()

		self.addToolBarBreak()

	def initFormatbar(self):
		fontBox = QtWidgets.QFontComboBox(self)
		fontBox.currentFontChanged.connect(self.fontFamily)

		fontSize = QtWidgets.QComboBox(self)
		fontSize.setEditable(True)

		# Minimum number of chars displayed
		fontSize.setMinimumContentsLength(3)

		fontSize.activated.connect(self.fontSize)

		fontSizes = ['6','7','8','9','10','11','12','14','18','24','36','48','72']

		for i in fontSizes:
			fontSize.addItem(i)

		fontColor = QtWidgets.QAction(QtGui.QIcon("icons/font-color.png"), "Change font color", self)
		fontColor.triggered.connect(self.fontColor)

		backColor = QtWidgets.QAction(QtGui.QIcon("icons/highlight.png"), "Change highlight color", self)
		backColor.triggered.connect(self.highlight)

		boldAction = QtWidgets.QAction(QtGui.QIcon("icons/bold.png"), "Bold", self)
		boldAction.triggered.connect(self.bold)

		italicAction = QtWidgets.QAction(QtGui.QIcon("icons/italic.png"), "Italic", self)
		italicAction.triggered.connect(self.italic)

		underlAction = QtWidgets.QAction(QtGui.QIcon("icons/underline.png"), "Underline", self)
		underlAction.triggered.connect(self.underline)

		strikeAction = QtWidgets.QAction(QtGui.QIcon("icons/strike.png"), "Strike-through", self)
		strikeAction.triggered.connect(self.strike)

		superAction = QtWidgets.QAction(QtGui.QIcon("icons/superscript.png"), "Superscript", self)
		superAction.triggered.connect(self.superScript)

		subAction = QtWidgets.QAction(QtGui.QIcon("icons/subscript.png"), "Subscript", self)
		subAction.triggered.connect(self.subScript)

		self.formatbar = self.addToolBar("Format")

		self.formatbar.addWidget(fontBox)
		self.formatbar.addWidget(fontSize)

		self.formatbar.addSeparator()

		self.formatbar.addAction(fontColor)
		self.formatbar.addAction(backColor)

		self.formatbar.addSeparator()

		self.formatbar.addAction(boldAction)
		self.formatbar.addAction(italicAction)
		self.formatbar.addAction(underlAction)
		self.formatbar.addAction(strikeAction)
		self.formatbar.addAction(superAction)
		self.formatbar.addAction(subAction)

		self.formatbar.addSeparator()

	def initMenubar(self):
		menubar = self.menuBar()
		
		file = menubar.addMenu("File")
		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		file.addAction(self.saveAsAction)
		file.addAction(self.printAction)
		file.addAction(self.previewAction)

		edit = menubar.addMenu("Edit")
		edit.addAction(self.undoAction)
		edit.addAction(self.redoAction)
		edit.addAction(self.cutAction)
		edit.addAction(self.copyAction)
		edit.addAction(self.pasteAction)

		view = menubar.addMenu("View")

	def initUI(self):
		self.text = QtWidgets.QTextEdit(self)
		self.setCentralWidget(self.text)

		self.initToolbar()
		self.initFormatbar()
		self.initMenubar()

		self.text.setTabStopWidth(33)

		self.statusbar = self.statusBar()

		self.text.cursorPositionChanged.connect(self.cursorPosition)

		self.setGeometry(100,100,1024,600)
		self.setWindowTitle("Writer")

	def new(self):
		spawn = Main(self)
		spawn.show()

	def open(self):
		self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.writer)")[0]

		if self.filename:
			with open(self.filename, "r+") as file:
				self.text.setText(file.read())

	def save(self):
		if not self.filename:
			self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]

		if not self.filename.endswith(".writer"):
			self.filename += ".writer"

		with open(self.filename, "r+") as file:
			file.write(self.text.toHtml())

	def saveAs(self):
		fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
		
		if not fname.endswith(".writer"):
			fname += ".writer"

		with open(fname, "r+") as file:
			file.write(self.text.toHtml())

	def preview(self):
		preview = QtPrintSupport.QPrintPreviewDialog()

		preview.paintRequested.connect(lambda p: self.text.print_(p))

		preview.exec_()

	def printDoc(self):
		dialog = QtPrintSupport.QPrintDialog()

		if dialog.exec_() == QtWidgets.QDialog.Accepted:
			self.text.document().print_(dialog.printer())

	def cursorPosition(self):
		cursor = self.text.textCursor()

		line = cursor.blockNumber() + 1
		col = cursor.columnNumber()

		self.statusbar.showMessage("Line: {} | Col: {}".format(line, col))

	def bulletList(self):
		cursor = self.text.textCursor()

		cursor.insertList(QtGui.QTextListFormat.ListDisc)

	def numberList(self):
		cursor = self.text.textCursor()
		cursor.insertList(QtGui.QTextListFormat.ListDecimal)

	def fontFamily(self, font):
		self.text.setCurrentFont(font)

	def fontSize(self, fontsize):
		self.text.setFontPointSize(int(fontsize))

	def fontColor(self):
		# Get a color from the text dialog
		color = QtWidgets.QColorDialog.getColor()

		# Set it as the new text color
		self.text.setTextColor(color)

	def highlight(self):
		color = QtWidgets.QColorDialog.getColor()
		self.text.setTextBackgroundColor(color)

	def bold(self):
		if self.text.fontWeight() == QtGui.QFont.Bold:
			self.text.setFontWeight(QtGui.QFont.Normal)
		else:
			self.text.setFontWeight(QtGui.QFont.Bold)

	def italic(self):
		state = self.text.fontItalic()
		self.text.setFontItalic(not state)

	def underline(self):
		state = self.text.fontUnderline()
		self.text.setFontUnderline(not state)

	def strike(self):
		# Get text format
		fmt = self.text.currentCharFormat()

		# Set StrikeOut property to its opposite
		fmt.setFontStrikeOut(not fmt.fontStrikeOut())

		# Set next char format
		self.text.setCurrentCharFormat(fmt)

	def superScript(self):
		fmt = self.text.currentCharFormat()

		# Get vertical alignment property
		align = fmt.verticalAlignment()

		# Toggle the state
		if align == QtGui.QTextCharFormat.AlignNormal:
			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
		else:
			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

		self.text.setCurrentCharFormat(fmt)

	def subScript(self):
		fmt = self.text.currentCharFormat()

		align = fmt.verticalAlignment()

		if align == QtGui.QTextCharFormat.AlignNormal:
			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
		else:
			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
		self.text.setCurrentCharFormat(fmt)

def main():

	app = QtWidgets.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
