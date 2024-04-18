from PyQt5.QtCore import Qt, QThread
from PyQt5 import QtCore
from time import sleep

class ThreadClass(QThread):
        any_signal = QtCore.pyqtSignal(int)
        def __init__(self, parent = None):
                super(ThreadClass, self).__init__(parent)
                self.is_running = True
        def run(self):
                while True:
                        self.any_signal.emit(1)
                        sleep(0.1)
        def stop(self):
                self.is_running = False
                self.terminate()
