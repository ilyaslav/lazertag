from PyQt5 import QtCore, QtGui, QtWidgets

class ScriptWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(ScriptWidget, self).__init__(*args, **kwargs)
        self.is_selected1 = False
        self.is_selected2 = False

    def startEvent(self):
    	pass
    def stopEvent(self):
    	pass
    def set_time(self):
    	pass
    def exclude_disabling(self):
        pass