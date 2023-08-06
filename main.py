from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QTextCodec
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_MainWindow import Ui_MainWindow
from noScriptWidget import NoScriptWidget
from MainMenuWidget import MainMenuWidget
from TabWidget import TabWidget

import game
import settings

class MyApp(Ui_MainWindow):
	def setupUi(self, MainWindow):
		super(MyApp, self).setupUi(MainWindow)
		self.blink_timer = QTimer()
		self.main_timer = QTimer()
		self.start_worker()

	def main_loop(self):
		self.change_game_status()
		self.change_stage_status()
		self.emergencyEvent()
		self.change_stage()
		self.restart_stage()
		self.exclude_stage()
		self.include_stage()

	def change_game_status(self):
		if not settings.readyToStart and not settings.initStatus\
		and not settings.gameStatus and settings.event:
			self.stop_game()
		elif not settings.readyToStart and game.check_to_start():
			self.mainMenuWidget.yellow_start_button()
		elif settings.initStatus and settings.readyToStart and settings.event:
			self.init_game()
		elif settings.gameStatus and settings.initStatus and settings.event:
			self.start_game()

	def change_stage_status(self):
		widget = self.find_stage()
		if widget:
			if settings.startStageEvent and not settings.stageStatus:
				self.start_stage(widget)
			elif settings.stopStageEvent and settings.stageStatus:
				self.stop_stage(widget)

	def find_stage(self):
		if settings.currentStage == 0:
			return None
		elif settings.currentStage == 1 or settings.currentStage == 2:
			return self.script1_widget
		elif settings.currentStage == 3 or settings.currentStage == 4:
			return self.script2_widget
		elif settings.currentStage == 5 or settings.currentStage == 6:
			return self.script3_widget
		elif settings.currentStage == 7 or settings.currentStage == 8:
			return self.script4_widget
		elif settings.currentStage == 9 or settings.currentStage == 10:
			return self.script5_widget

	def restart_stage(self):
		if settings.restartStageEvent:
			if self.script1_widget.is_selected1:
				settings.stages[0] = True
			if self.script1_widget.is_selected2:
				settings.stages[1] = True
			if self.script2_widget.is_selected1:
				settings.stages[2] = True
			if self.script2_widget.is_selected2:
				settings.stages[3] = True
			if self.script3_widget.is_selected1:
				settings.stages[4] = True
			if self.script3_widget.is_selected2:
				settings.stages[5] = True
			if self.script4_widget.is_selected1:
				settings.stages[6] = True
			if self.script4_widget.is_selected2:
				settings.stages[7] = True
			if self.script5_widget.is_selected1:
				settings.stages[8] = True
			if self.script5_widget.is_selected2:
				settings.stages[9] = True
			settings.restartStageEvent = False
			settings.changeStageEvent = True


	def change_stage(self):
		if settings.changeStageEvent:
			print(settings.stages)
			settings.currentStage = 0
			for st in settings.stages:
				if st:
					settings.currentStage = settings.stages.index(st)+1
					print(settings.currentStage)
					break
			self.remove_selection()
			if settings.currentStage == 1:
				self.script1_widget.is_selected1 = True
				self.script1_widget.yellow_stage_label1()
			elif settings.currentStage == 2:
				self.script1_widget.is_selected2 = True
				self.script1_widget.yellow_stage_label2()
			elif settings.currentStage == 3:
				self.script2_widget.is_selected1 = True
				self.script2_widget.yellow_stage_label1()
			elif settings.currentStage == 4:
				self.script2_widget.is_selected2 = True
				self.script2_widget.yellow_stage_label2()
			elif settings.currentStage == 5:
				self.script3_widget.is_selected1 = True
				self.script3_widget.yellow_stage_label1()
			elif settings.currentStage == 6:
				self.script3_widget.is_selected2 = True
				self.script3_widget.yellow_stage_label2()
			elif settings.currentStage == 7:
				self.script4_widget.is_selected1 = True
				self.script4_widget.yellow_stage_label1()
			elif settings.currentStage == 8:
				self.script4_widget.is_selected2 = True
				self.script4_widget.yellow_stage_label2()
			elif settings.currentStage == 9:
				self.script5_widget.is_selected1 = True
				self.script5_widget.yellow_stage_label1()
			elif settings.currentStage == 10:
				self.script5_widget.is_selected2 = True
				self.script5_widget.yellow_stage_label2()
			settings.changeStageEvent = False
			self.change_tab_color()

	def exclude_stage(self):
		if settings.excludeStageEvent:
			widget = self.find_stage()
			if widget:
				self.exclude_disabling()
				if widget.is_selected1:
					widget.exclude_stage1_event()
				elif widget.is_selected2:
					widget.exclude_stage2_event()
			settings.excludeStageEvent = False

	def include_stage(self):
		if settings.includeStageEvent:
			settings.currentStage-=1
			widget = self.find_stage()
			settings.currentStage+=1
			if widget:
				if widget.is_exclude1:
					widget.include_stage1_event()
				elif widget.is_exclude2:
					widget.include_stage2_event()
			settings.includeStageEvent = False

	def remove_selection(self):
		self.script1_widget.is_selected1 = False
		self.script1_widget.is_selected2 = False
		self.script2_widget.is_selected1 = False
		self.script2_widget.is_selected2 = False
		self.script3_widget.is_selected1 = False
		self.script3_widget.is_selected2 = False
		self.script4_widget.is_selected1 = False
		self.script4_widget.is_selected2 = False
		self.script5_widget.is_selected1 = False
		self.script5_widget.is_selected2 = False

	def exclude_disabling(self):
		self.script1_widget.exclude_disabling()
		self.script2_widget.exclude_disabling()
		self.script3_widget.exclude_disabling()
		self.script4_widget.exclude_disabling()
		self.script5_widget.exclude_disabling()

	def emergencyEvent(self):
		if settings.emergencyEvent:
			if settings.emergencyStatus:
				self.mainMenuWidget.emergency_button_off()
			else:
				self.mainMenuWidget.emergency_button_on()
			print('emergencyStatus =', settings.emergencyStatus)
			settings.emergencyEvent = False

	def init_game(self):
		self.mainMenuWidget.green_start_button()
		self.start_blink_timer()
		self.mainMenuWidget.disabled_scripts_map()
		self.mainMenuWidget.disabled_check_time()
		self.mainMenuWidget.green_timer()
		self.start_main_timer()
		settings.readyToStart = False
		settings.event = False

	def start_game(self):
		self.stop_blink_timer()
		self.mainMenuWidget.green_start_button()
		settings.changeStageEvent = True
		settings.initStatus = False
		settings.event = False

	def stop_game(self):
		self.stop_blink_timer()
		self.stop_main_timer()
		game.set_main_time()
		game.set_stage_time()
		self.mainMenuWidget.set_main_time()
		self.set_default()
		settings.event = False

	def start_stage(self, widget):
		widget.start_event()
		widget.init_time()
		self.start_stage_timer(widget)
		self.exclude_disabling()
		settings.startStageEvent = False
		settings.stageStatus = True

	def stop_stage(self, widget):
		widget.stop_event()
		self.stop_stage_timer()
		settings.stopStageEvent = False
		settings.currentStage = widget.find_next()
		settings.stageStatus = False
		settings.changeStageEvent = True
		settings.stageTime = 600

	def blink_button(self):
		if not settings.outs['tableButton']:
			self.mainMenuWidget.green_start_button()
		else:
			self.mainMenuWidget.white_start_button()
		settings.outs['tableButton'] = not settings.outs['tableButton']
	def start_blink_timer(self):
		self.blink_timer = QTimer()
		self.blink_timer.timeout.connect(self.blink_button)
		self.blink_timer.start(settings.time[0]['t3']*1000)
	def stop_blink_timer(self):
		self.blink_timer.stop()

	def main_timer_event(self):
		if settings.mainTime:
			settings.mainTime-=1
			self.mainMenuWidget.set_main_time()
		else:
			self.stop_main_timer()
	def start_main_timer(self):
		self.main_timer = QTimer()
		self.main_timer.timeout.connect(self.main_timer_event)
		self.main_timer.start(1000)
	def stop_main_timer(self):
		self.main_timer.stop()

	def stage_timer_event(self, widget):
		if settings.stageTimer == 'decreasing':
			if settings.stageTime:
				settings.stageTime-=1
				widget.set_time()
			else:
				self.stop_stage_timer()
				widget.stop_event()
		else:
			settings.stageTime+=1
			widget.set_time()
	def start_stage_timer(self, widget):
		self.stage_timer = QTimer()
		self.stage_timer.timeout.connect(lambda: self.stage_timer_event(widget))
		self.stage_timer.start(1000)
	def stop_stage_timer(self):
		self.stage_timer.stop()

	def change_tab_color(self):
		print(int((settings.currentStage+1)/2))
		self.tabWidget.set_green(int((settings.currentStage+1)/2))

if __name__ == "__main__":
	import sys
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("fusion")
	MainWindow = QtWidgets.QMainWindow()
	ui = MyApp()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())