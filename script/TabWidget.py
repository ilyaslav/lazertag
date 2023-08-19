from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor


class TabBar(QtWidgets.QTabBar):
	def __init__(self, texts, colors, parent=None):
		super(TabBar, self).__init__(parent)
		self.mColors = colors
		self.mTexts = texts

		font = QtGui.QFont()
		font.setPointSize(13)
		font.setBold(True)
		font.setWeight(75)
		self.setFont(font)

	def paintEvent(self, event):
		painter = QtWidgets.QStylePainter(self)
		opt = QtWidgets.QStyleOptionTab()

		for i in range(self.count()):
			self.initStyleOption(opt, i)
			opt.palette.setColor(
				QtGui.QPalette.Button, self.mColors[i]
			)
			painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
			painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)

	def set_colors(self, colors):
		self.mColors = colors
		self.update()
	def set_texts(self, texts):
		self.mTexts = texts
		self.update()


class TabWidget(QtWidgets.QTabWidget):
	def __init__(self, parent=None):
		super(TabWidget, self).__init__(parent)
		self.tab_texts = [
			"Основные настройки",
			"Сценарий не выбран",
			"Сценарий не выбран",
			"Сценарий не выбран",
			"Сценарий не выбран",
			"Сценарий не выбран",
			"Диагностика",
			"Общие настройки",
		]
		self.tab_colors = [
			QtGui.QColor("#00bb00"),
			QtGui.QColor("#cfd1cd"),
			QtGui.QColor("#cfd1cd"),
			QtGui.QColor("#cfd1cd"),
			QtGui.QColor("#cfd1cd"),
			QtGui.QColor("#cfd1cd"),
			QtGui.QColor("#cfd1cd"),
			QtGui.QColor("#cfd1cd"),
		]

		self.tabBar = TabBar(self.tab_texts, self.tab_colors)
		self.setTabBar(self.tabBar)
		self.setStyleSheet("QTabWidget::pane\n"
"{\n"
"    border: 1px;\n"
"    background: rgb(4,38,14);\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #B5B8B1, stop: 1 #ffffff);\n"
"}\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"    background: #373e4e;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTabBar::tab::hover\n"
"{\n"
"    background: #DCDCDC;\n"
"    color: #000000;\n"
"}")
	def update_colors(self):
		self.tabBar.set_colors(self.tab_colors)
	def update_texts(self):
		self.tabBar.set_texts(self.tab_texts)
	def set_color(self, ind, color):
		self.tab_colors[ind] = color
		self.update_colors()
	def set_green(self, ind):
		self.set_gray()
		self.set_color(ind, QtGui.QColor("#00bb00"))
	def set_gray(self):
		for i in range(len(self.tab_colors)):
			self.set_color(i, QtGui.QColor("#cfd1cd"))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	w = TabWidget()
	w.show()
	sys.exit(app.exec_())