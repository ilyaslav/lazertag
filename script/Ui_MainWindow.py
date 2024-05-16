# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lasertag.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt, QThread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from noScriptWidget import NoScriptWidget
from scriptWidget import ScriptWidget
from MainMenuWidget import MainMenuWidget
from diagnosticWidget import DiagnosticWidget
from TabWidget import TabWidget
import settings
import functools


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #373e4e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = TabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.tabWidget.addTab(self.main_tab, "")
        self.script1_tab = QtWidgets.QWidget()
        self.script1_tab.setObjectName("script1_tab")
        self.tabWidget.addTab(self.script1_tab, "")
        self.script2_tab = QtWidgets.QWidget()
        self.script2_tab.setObjectName("script2_tab")
        self.tabWidget.addTab(self.script2_tab, "")
        self.script3_tab = QtWidgets.QWidget()
        self.script3_tab.setObjectName("script3_tab")
        self.tabWidget.addTab(self.script3_tab, "")
        self.script4_tab = QtWidgets.QWidget()
        self.script4_tab.setObjectName("script4_tab")
        self.tabWidget.addTab(self.script4_tab, "")
        self.script5_tab = QtWidgets.QWidget()
        self.script5_tab.setObjectName("script5_tab")
        self.tabWidget.addTab(self.script5_tab, "")
        self.diagnostics = QtWidgets.QWidget()
        self.diagnostics.setObjectName("diagnostics")
        self.tabWidget.addTab(self.diagnostics, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.tabWidget.addTab(self.settings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_main_menu()
        self.add_script1_widget()
        self.add_script2_widget()
        self.add_script3_widget()
        self.add_script4_widget()
        self.add_script5_widget()
        self.add_diagnostic()
        self.connect_functions()

    def add_main_menu(self):
        self.gridLayout_00 = QtWidgets.QGridLayout(self.main_tab)
        self.gridLayout_00.setObjectName("gridLayout_00")
        self.mainMenuWidget = MainMenuWidget(self.main_tab)
        self.gridLayout_00.addWidget(self.mainMenuWidget, 0, 0, 1, 1)
    def add_script1_widget(self):
        self.gridLayout_11 = QtWidgets.QGridLayout(self.script1_tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.script1_widget = ScriptWidget(self.script1_tab)
        self.gridLayout_11.addWidget(self.script1_widget, 0, 0, 1, 1)
    def add_script2_widget(self):
        self.gridLayout_22 = QtWidgets.QGridLayout(self.script2_tab)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.script2_widget = ScriptWidget(self.script2_tab)
        self.gridLayout_22.addWidget(self.script2_widget, 0, 0, 1, 1)
    def add_script3_widget(self):
        self.gridLayout_33 = QtWidgets.QGridLayout(self.script3_tab)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.script3_widget = ScriptWidget(self.script3_tab)
        self.gridLayout_33.addWidget(self.script3_widget, 0, 0, 1, 1)
    def add_script4_widget(self):
        self.gridLayout_44 = QtWidgets.QGridLayout(self.script4_tab)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.script4_widget = ScriptWidget(self.script4_tab)
        self.gridLayout_44.addWidget(self.script4_widget, 0, 0, 1, 1)
    def add_script5_widget(self):
        self.gridLayout_55 = QtWidgets.QGridLayout(self.script5_tab)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.script5_widget = ScriptWidget(self.script5_tab)
        self.gridLayout_55.addWidget(self.script5_widget, 0, 0, 1, 1)
    def add_diagnostic(self):
        self.gridLayout_66 = QtWidgets.QGridLayout(self.diagnostics)
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.diagnosticWidget = DiagnosticWidget(self.diagnostics)
        self.gridLayout_66.addWidget(self.diagnosticWidget, 0, 0, 1, 1)

    def bt_out_press(self, out):
        pass

    def change_participants(self):
        self.mainMenuWidget.change_participants_box()
        settings.settingsToWrite['players'] = self.mainMenuWidget.participants_box.value()
        if self.mainMenuWidget.participants_box.value() > 5:
            settings.settingsToStart['players'] = True
        else:
            settings.settingsToStart['players'] = False
            self.set_notReady()

    def change_celebrant(self):
        self.mainMenuWidget.change_celebrant_box()
        settings.settingsToWrite['celebrant'] = self.mainMenuWidget.celebrant_box.currentText()
        if self.mainMenuWidget.celebrant_box.currentIndex() != 0:
            settings.settingsToStart['celebrant'] = True
        else:
            settings.settingsToStart['celebrant'] = False
            self.set_notReady()

    def change_instructors(self):
        self.mainMenuWidget.change_instructors_box()
        settings.settingsToWrite['instructors'] = self.mainMenuWidget.instructors_box.toPlainText()
        if self.mainMenuWidget.instructors_box.toPlainText() != '':
            settings.settingsToStart['instructors'] = True
        else:
            settings.settingsToStart['instructors'] = False
            self.set_notReady()

    def connect_functions(self):
        self.mainMenuWidget.emergency_lighting_button.pressed.connect(self.mainMenuWidget.emergency_button_press)
        self.mainMenuWidget.add_time_button.pressed.connect(self.mainMenuWidget.add_time)
        self.mainMenuWidget.reduce_time_button.pressed.connect(self.mainMenuWidget.reduce_time)
        self.mainMenuWidget.up_red_button.pressed.connect(self.mainMenuWidget.add_main_score_red)
        self.mainMenuWidget.up_blue_button.pressed.connect(self.mainMenuWidget.add_main_score_blue)
        self.mainMenuWidget.down_red_button.pressed.connect(self.mainMenuWidget.reduce_main_score_red)
        self.mainMenuWidget.down_blue_button.pressed.connect(self.mainMenuWidget.reduce_main_score_blue)
        self.mainMenuWidget.check_game_time.stateChanged.connect(self.check_game_time_event)
        self.mainMenuWidget.check_game_score.stateChanged.connect(self.check_game_score_event)
        self.mainMenuWidget.scripts_map.activated.connect(self.scripts_map_event)
        self.mainMenuWidget.scripts_map.currentTextChanged.connect(self.scripts_map_event)
        self.mainMenuWidget.script1_box.currentTextChanged.connect(self.script1_box_event)
        self.mainMenuWidget.script2_box.currentTextChanged.connect(self.script2_box_event)
        self.mainMenuWidget.script3_box.currentTextChanged.connect(self.script3_box_event)
        self.mainMenuWidget.script4_box.currentTextChanged.connect(self.script4_box_event)
        self.mainMenuWidget.script5_box.currentTextChanged.connect(self.script5_box_event)
        self.mainMenuWidget.start_game_button.pressed.connect(self.start_game_button_press)
        self.mainMenuWidget.stop_game_button.pressed.connect(self.stop_game_button_press)
        self.mainMenuWidget.volume_level.valueChanged.connect(self.change_volume_level)
        self.mainMenuWidget.participants_box.valueChanged.connect(self.change_participants)
        self.mainMenuWidget.instructors_box.textChanged.connect(self.change_instructors)
        self.mainMenuWidget.celebrant_box.currentTextChanged.connect(self.change_celebrant)
        self.diagnosticWidget.diagnostic_state.pressed.connect(self.diagnosticWidget.bt_diagnostic_press)
        for out in self.diagnosticWidget.outs:
            self.diagnosticWidget.outs[out].pressed.connect(functools.partial(self.bt_out_press, out))

    def set_notReady(self):
        settings.readyToStart = False
        self.mainMenuWidget.white_start_button()

    def change_scripts_map(self, ind, numberOfStage):
        settings.scriptsMap = ind
        settings.numberOfStage = numberOfStage
        if settings.scriptsMap != 0:
            settings.settingsToStart['scriptsMap'] = True
            self.mainMenuWidget.scripts_map.setStyleSheet("border-color: #00bb00;combobox-popup: 0;")
            self.mainMenuWidget.enabled_scripts()
        else:
            settings.settingsToStart['scriptsMap'] = False
            self.mainMenuWidget.scripts_map.setStyleSheet("border-color: #bb0000;combobox-popup: 0;")
            self.mainMenuWidget.disabled_scripts()
            self.set_notReady()

    def scripts_map_event(self):
        settings.settingsToWrite['scriptsMap'] = self.mainMenuWidget.scripts_map.currentText()
        for scr in self.mainMenuWidget.data['scripts_map']:
            if self.mainMenuWidget.scripts_map.currentText() == scr['name']:
                self.change_scripts_map(scr['id'], scr['numberOfStage'])
                self.mainMenuWidget.set_scripts_text(self.mainMenuWidget.script1_box, scr['scripts'][0])
                self.mainMenuWidget.set_scripts_text(self.mainMenuWidget.script2_box, scr['scripts'][1])
                self.mainMenuWidget.set_scripts_text(self.mainMenuWidget.script3_box, scr['scripts'][2])
                self.mainMenuWidget.set_scripts_text(self.mainMenuWidget.script4_box, scr['scripts'][3])
                self.mainMenuWidget.set_scripts_text(self.mainMenuWidget.script5_box, scr['scripts'][4])

    def activate_stage(self, num, boolean, name):
        settings.stages[num-1] = boolean
        settings.stages[num] = boolean
        settings.stageNames[int(num/2)] = name

    def change_active_stage(self):
        if settings.currentStage:
            settings.currentStage-=1
            settings.changeStageEvent = True

    def script1_box_event(self):
        self.gridLayout_11.removeWidget(self.script1_widget)
        self.tabWidget.setTabText(1, self.mainMenuWidget.script1_box.currentText())
        self.mainMenuWidget.change_script_box(self.mainMenuWidget.script1_box)
        name = self.mainMenuWidget.script1_box.currentText()
        self.activate_stage(1, True, name)
        self.change_active_stage()

        if self.mainMenuWidget.script1_box.currentText() == 'Сценарий не выбран':
            settings.currentStage = 0
            self.activate_stage(1, False, name)
            self.script1_widget = QtWidgets.QWidget(self.script1_tab)
            self.gridLayout_11.addWidget(self.script1_widget, 0, 0, 1, 1)
        elif self.mainMenuWidget.script1_box.currentText() == 'Без сценария'\
        or self.mainMenuWidget.script1_box.currentText() == 'Без сценария +':
            self.script1_widget = NoScriptWidget(self.script1_tab)
            self.gridLayout_11.addWidget(self.script1_widget, 0, 0, 1, 1)
        else:
            self.script1_widget = NoScriptWidget(self.script1_tab)
            self.gridLayout_11.addWidget(self.script1_widget, 0, 0, 1, 1)

        if self.mainMenuWidget.script1_box.currentText()[-1] == '+':
            self.script1_widget.wow_effects1.setCheckState(2)
            self.script1_widget.wow_effects2.setCheckState(2)

    def script2_box_event(self):
        self.gridLayout_22.removeWidget(self.script1_widget)
        self.tabWidget.setTabText(2, self.mainMenuWidget.script2_box.currentText())
        self.mainMenuWidget.change_script_box(self.mainMenuWidget.script2_box)
        name = self.mainMenuWidget.script2_box.currentText()
        self.activate_stage(3, True, name)
        self.change_active_stage()

        if self.mainMenuWidget.script2_box.currentText() == 'Сценарий не выбран':
            self.activate_stage(3, False, name)
            self.script2_widget = QtWidgets.QWidget(self.script2_tab)
            self.gridLayout_22.addWidget(self.script2_widget, 0, 0, 1, 1)
        elif self.mainMenuWidget.script2_box.currentText() == 'Без сценария'\
        or self.mainMenuWidget.script2_box.currentText() == 'Без сценария +':
            self.script2_widget = NoScriptWidget(self.script2_tab)
            self.gridLayout_22.addWidget(self.script2_widget, 0, 0, 1, 1)
        else:
            self.script2_widget = NoScriptWidget(self.script2_tab)
            self.gridLayout_22.addWidget(self.script2_widget, 0, 0, 1, 1)

        if self.mainMenuWidget.script2_box.currentText()[-1] == '+':
            self.script2_widget.wow_effects1.setCheckState(2)
            self.script2_widget.wow_effects2.setCheckState(2)

    def script3_box_event(self):
        self.gridLayout_33.removeWidget(self.script1_widget)
        self.tabWidget.setTabText(3, self.mainMenuWidget.script3_box.currentText())
        self.mainMenuWidget.change_script_box(self.mainMenuWidget.script3_box)
        name = self.mainMenuWidget.script3_box.currentText()
        self.activate_stage(5, True, name)
        self.change_active_stage()

        if self.mainMenuWidget.script3_box.currentText() == 'Сценарий не выбран':
            self.activate_stage(5, False, name)
            self.script3_widget = QtWidgets.QWidget(self.script3_tab)
            self.gridLayout_33.addWidget(self.script3_widget, 0, 0, 1, 1)
        elif self.mainMenuWidget.script3_box.currentText() == 'Без сценария'\
        or self.mainMenuWidget.script3_box.currentText() == 'Без сценария +':
            self.script3_widget = NoScriptWidget(self.script3_tab)
            self.gridLayout_33.addWidget(self.script3_widget, 0, 0, 1, 1)
        else:
            self.script3_widget = NoScriptWidget(self.script3_tab)
            self.gridLayout_33.addWidget(self.script3_widget, 0, 0, 1, 1)

        if self.mainMenuWidget.script3_box.currentText()[-1] == '+':
            self.script3_widget.wow_effects1.setCheckState(2)
            self.script3_widget.wow_effects2.setCheckState(2)

    def script4_box_event(self):
        self.gridLayout_44.removeWidget(self.script1_widget)
        self.tabWidget.setTabText(4, self.mainMenuWidget.script4_box.currentText())
        self.mainMenuWidget.change_script_box(self.mainMenuWidget.script4_box)
        name = self.mainMenuWidget.script4_box.currentText()
        self.activate_stage(7, True, name)
        self.change_active_stage()

        if self.mainMenuWidget.script4_box.currentText() == 'Сценарий не выбран':
            self.activate_stage(7, False, name)
            self.script4_widget = QtWidgets.QWidget(self.script4_tab)
            self.gridLayout_44.addWidget(self.script4_widget, 0, 0, 1, 1)
        elif self.mainMenuWidget.script4_box.currentText() == 'Без сценария'\
        or self.mainMenuWidget.script4_box.currentText() == 'Без сценария +':
            self.script4_widget = NoScriptWidget(self.script4_tab)
            self.gridLayout_44.addWidget(self.script4_widget, 0, 0, 1, 1)
        else:
            self.script4_widget = NoScriptWidget(self.script4_tab)
            self.gridLayout_44.addWidget(self.script4_widget, 0, 0, 1, 1)

        if self.mainMenuWidget.script4_box.currentText()[-1] == '+':
            self.script4_widget.wow_effects1.setCheckState(2)
            self.script4_widget.wow_effects2.setCheckState(2)

    def script5_box_event(self):
        self.gridLayout_55.removeWidget(self.script1_widget)
        self.tabWidget.setTabText(5, self.mainMenuWidget.script5_box.currentText())
        self.mainMenuWidget.change_script_box(self.mainMenuWidget.script5_box)
        name = self.mainMenuWidget.script5_box.currentText()
        self.activate_stage(9, True, name)
        self.change_active_stage()

        if self.mainMenuWidget.script5_box.currentText() == 'Сценарий не выбран':
            self.activate_stage(9, False, name)
            self.script5_widget = QtWidgets.QWidget(self.script5_tab)
            self.gridLayout_55.addWidget(self.script5_widget, 0, 0, 1, 1)
        elif self.mainMenuWidget.script5_box.currentText() == 'Без сценария'\
        or self.mainMenuWidget.script5_box.currentText() == 'Без сценария +':
            self.script5_widget = NoScriptWidget(self.script5_tab)
            self.gridLayout_55.addWidget(self.script5_widget, 0, 0, 1, 1)
        else:
            self.script5_widget = NoScriptWidget(self.script5_tab)
            self.gridLayout_55.addWidget(self.script5_widget, 0, 0, 1, 1)

        if self.mainMenuWidget.script5_box.currentText()[-1] == '+':
            self.script5_widget.wow_effects1.setCheckState(2)
            self.script5_widget.wow_effects2.setCheckState(2)

    def start_game_button_press(self):
        if settings.readyToStart:
            settings.initStatus = True
            settings.event = True
        elif settings.initStatus:
            settings.gameStatus = True
            settings.event = True

    def stop_game_button_press(self):
        if settings.gameStatus and not settings.stageStatus or settings.initStatus:
            settings.readyToStart = False
            settings.initStatus = False
            settings.gameStatus = False
            settings.event = True

    def check_game_score_event(self):
        if self.mainMenuWidget.check_game_score.checkState() == 2:
            settings.check_game_score = True
        else:
            settings.check_game_score = False

    def check_game_time_event(self):
        print(self.mainMenuWidget.check_game_time.checkState())

    def set_default(self):
        self.mainMenuWidget.white_start_button()
        self.mainMenuWidget.enabled_scripts_map()
        self.mainMenuWidget.enabled_check_time()
        self.mainMenuWidget.scripts_map.setCurrentText('Сценарная карта не выбрана')
        self.mainMenuWidget.participants_box.setValue(1)
        self.mainMenuWidget.celebrant_box.setCurrentIndex(0)
        self.mainMenuWidget.instructors_box.setText('')
        self.mainMenuWidget.red_timer()

    def change_volume_level(self):
        if settings.volume != self.mainMenuWidget.volume_level.value():
            settings.volume = self.mainMenuWidget.volume_level.value()
            settings.volumeEvent = True
            print(settings.volume)

    def set_volume_level(self, value):
        if value >= 0 and value <= 100:
            self.mainMenuWidget.volume_level.setValue(value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("MainWindow", "Основные настройки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script1_tab), _translate("MainWindow", "Сценарий не выбран"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script2_tab), _translate("MainWindow", "Сценарий не выбран"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script3_tab), _translate("MainWindow", "Сценарий не выбран"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script4_tab), _translate("MainWindow", "Сценарий не выбран"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script5_tab), _translate("MainWindow", "Сценарий не выбран"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagnostics), _translate("MainWindow", "Диагностика"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Общие настройки"))



if __name__ == "__main__":
        import sys
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("fusion")
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
