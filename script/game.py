import settings
import json
import threading
import time
from server import Server

data = {}
with open('data.txt') as json_file:
	data = json.load(json_file)

class GameServer(Server):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def message_handler(self, mes):
		print(f'Принято сообщение: {mes}')
		if mes == 'game_button1':
			settings.inputs['game_button'] = True
			start_main_timer()
		elif mes == 'game_button0':
			settings.inputs['game_button'] = False
			stop_main_timer()
		elif mes == 'start_stage1':
			settings.inputs['start_stage'] = True
			start_stage_timer1()
		elif mes == 'start_stage0':
			settings.inputs['start_stage'] = False
			start_stage_timer0()
		if mes == 'stop_stage1':
			settings.inputs['stop_stage'] = True
			start_stop_timer1()
		elif mes == 'stop_stage0':
			settings.inputs['stop_stage'] = False
			stop_stage_timer0()
		if mes == 'sound_button1':
			settings.inputs['sound_button'] = True
			start_sound_timer()
		elif mes == 'sound_button0':
			settings.inputs['sound_button'] = False
			stop_sound_timer()
		if mes == 'light_button1':
			settings.inputs['light_button'] = True
			start_emergency_timer()
		elif mes == 'light_button0':
			settings.inputs['light_button'] = False
			stop_emergency_timer()
		if mes == 'signal_R1':
			settings.inputs['signal_R'] = True
		elif mes == 'signal_R0':
			settings.inputs['signal_R'] = False
		if mes == 'signal_G1':
			settings.inputs['signal_G'] = True
		elif mes == 'signal_G0':
			settings.inputs['signal_G'] = False
		if mes == 'signal_B1':
			settings.inputs['signal_B'] = True
		elif mes == 'signal_B0':
			settings.inputs['signal_B'] = False
		if mes == 'takeFlag_A1':
			settings.inputs['takeFlag_A'] = True
		elif mes == 'takeFlag_A0':
			settings.inputs['takeFlag_A'] = False
		if mes == 'takeFlag_B1':
			settings.inputs['takeFlag_B'] = True
		elif mes == 'takeFlag_B0':
			settings.inputs['takeFlag_B'] = False
		if mes == 'giveFlag_A1':
			settings.inputs['giveFlag_A'] = True
		elif mes == 'giveFlag_A0':
			settings.inputs['giveFlag_A'] = False
		if mes == 'giveFlag_B1':
			settings.inputs['giveFlag_B'] = True
		elif mes == 'giveFlag_B0':
			settings.inputs['giveFlag_B'] = False
		if mes == 'bomb_activated1':
			settings.inputs['bomb_activated'] = True
		elif mes == 'bomb_activated0':
			settings.inputs['bomb_activated'] = False
		if mes == 'bomb_planted1':
			settings.inputs['bomb_planted'] = True
		elif mes == 'bomb_planted0':
			settings.inputs['bomb_planted'] = False

	def init_settings(self):
		if not settings.emergencyStatus:
			for out in settings.outs:
				reset_out(out)
		else:
			emergency_on()

gs = GameServer()
threading.Thread(target=gs.start_server, daemon=True).start()

def set_main_time():
	settings.mainTime = settings.time[0]['mainTime']
	settings.addedTime = 0

def set_stage_time():
	settings.stageTime = settings.time[0]['t5']


settings.time = data['time']
set_main_time()
set_stage_time()
settings.numberOfStage = data['scripts_map'][0]['numberOfStage']
settings.scriptsMap = data['scripts_map'][0]['id']

def start_main_timer():
	settings.startMainTime = time.time()
	settings.mainTimer = True

def start_stage_timer1():
	settings.startStageTime1 = time.time()
	settings.stageTimer1 = True

def start_stage_timer0():
	settings.startStageTime0 = time.time()
	settings.stageTimer0 = True

def start_sound_timer():
	settings.startSoundTime = time.time()
	settings.soundTimer = True

def start_emergency_timer():
	settings.startEmergencyTime = time.time()
	settings.emergencyTimer = True

def stop_main_timer():
	settings.mainTimer = False

def stop_stage_timer1():
	settings.stageTimer1 = False

def stop_stage_timer0():
	settings.stageTimer0 = False

def stop_sound_timer():
	settings.soundTimer = False

def stop_emergency_timer():
	settings.emergencyTimer = False

def check_timers():
	if settings.mainTimer:
		if check_time(settings.startMainTime):
			if settings.gameStatus:
				stop_game_script()
			else:
				start_game_script()
	if settings.stageTimer1:
		if check_time(settings.startStageTime1):
			start_stage_script()
	if settings.stageTimer0:
		if check_time(settings.startStageTime0):
			stop_stage_script()
	if settings.soundTimer:
		if check_time(settings.startSoundTime):
			sound_script()
	if settings.emergencyTimer:
		if check_time(settings.startEmergencyTime):
			emergency_script()

def check_time(timer):
	return time.time() - timer >= 2 and time.time() - timer < 4

def start_game_script():
	settings.mainTimer = False
	if settings.readyToStart:
		settings.initStatus = True
		settings.event = True
	elif settings.initStatus:
		settings.gameStatus = True
		settings.event = True

def stop_game_script():
	settings.mainTimer = False
	settings.readyToStart = False
	settings.initStatus = False
	settings.gameStatus = False
	settings.event = True

def start_stage_script():
	settings.stageTimer1 = False
	if not settings.stageStatus and settings.gameStatus:
		settings.startStageEvent = True

def stop_stage_script():
	settings.stageTimer0 = False
	if settings.stageStatus and settings.gameStatus:
		settings.stopStageEvent = True

def sound_script():
	settings.soundTimer = False
	if settings.volume:
		settings.volume = 0
	else:
		settings.volume = 100
	settings.volumeEvent = True

def emergency_script():
	settings.emergencyTimer = False
	settings.emergencyEvent = True

def check_to_start():
	for status in settings.settingsToStart:
		if not settings.settingsToStart[status]:
			settings.readyToStart = False
			return settings.readyToStart
	if not settings.gameStatus and not settings.initStatus:
		settings.readyToStart = True
	return settings.readyToStart

def change_volume():
	gs.send_message(f'volume{int(settings.volume)};')

def play_music(music):
	gs.send_message(f'play{music};')

def pause_music(music):
	gs.send_message(f'pause{music};')

def stop_music(music):
	gs.send_message(f'stop{music};')

def init_settings():
	settings.outs = {
	'tableButton': True,
	'ARed': True,
	'ABlue': True,
	'BRed': True,
	'BBlue': True,
	'AdminLight': True,
	'area1_W1': False,
	'area1_TL1': True,
	'area2_W2': False,
	'area2_TL2': True,
	'area3_W3': False,
	'area3_TL3': True,
	'area4_W4': False,
	'area4_TL4': True,
	'hallway1_WK1': False,
	'hallway1_TLK1': True,
	'hallway2_WK2': False,
	'hallway2_TLK2': True,
	'give_LK1': True,
	'medicBag_A': False,
	'medicBag_B': False
}
	if not settings.emergencyStatus:
		for out in settings.outs:
			reset_out(out)

def init_game():
	settings.outs['hallway1_WK1'] = True
	settings.outs['give_LK1'] = False
	settings.outs['AdminLight'] = False

	if not settings.emergencyStatus:
		for out in settings.outs:
			reset_out(out)

def start_game():
	settings.outs['tableButton'] = False
	settings.outs['hallway1_WK1'] = False
	settings.outs['hallway1_WK1'] = True
	settings.outs['AdminLight'] = True

	if not settings.emergencyStatus:
		for out in settings.outs:
			reset_out(out)

def stop_game():
	init_settings()

def init_stage():
	settings.outs['area1_W1'] = True
	settings.outs['area3_W3'] = True
	if not settings.currentStage%2:
		settings.outs['ARed'] = False
		settings.outs['BBlue'] = False
	else:
		settings.outs['BRed'] = False
		settings.outs['ABlue'] = False

	if not settings.emergencyStatus:
		for out in settings.outs:
			reset_out(out)

def start_stage():
	if not settings.currentStage%2:
		settings.outs['ARed'] = True
		settings.outs['BBlue'] = True
	else:
		settings.outs['BRed'] = True
		settings.outs['ABlue'] = True
	if not settings.wowEffects:
		settings.outs['area1_W1'] = False
		settings.outs['area3_W3'] = False
	else:
		settings.outs['area1_W1'] = True
		settings.outs['area1_TL1'] = False
		settings.outs['area2_W2'] = True
		settings.outs['area2_TL2'] = False
		settings.outs['area3_W3'] = True
		settings.outs['area3_TL3'] = False
		settings.outs['area4_W4'] = True
		settings.outs['area4_TL4'] = False
		settings.outs['hallway1_WK1'] = True
		settings.outs['hallway1_TLK1'] = False
		settings.outs['hallway2_WK2'] = True
		settings.outs['hallway2_TLK2'] = False
		settings.outs['give_LK1'] = True

	if not settings.emergencyStatus:
		for out in settings.outs:
			reset_out(out)

def stop_stage():
	if settings.wowEffects:
		settings.outs['area1_W1'] = False
		settings.outs['area1_TL1'] = True
		settings.outs['area2_W2'] = False
		settings.outs['area2_TL2'] = True
		settings.outs['area3_W3'] = False
		settings.outs['area3_TL3'] = True
		settings.outs['area4_W4'] = False
		settings.outs['area4_TL4'] = True
		settings.outs['hallway1_WK1'] = False
		settings.outs['hallway1_TLK1'] = True
		settings.outs['hallway2_WK2'] = False
		settings.outs['hallway2_TLK2'] = True
		settings.outs['give_LK1'] = False

		if not settings.emergencyStatus:
			for out in settings.outs:
				reset_out(out)

def emergency_on():
	gs.send_message('area1_W10;')
	gs.send_message('area1_TL11;')
	gs.send_message('area2_W20;')
	gs.send_message('area2_TL21;')
	gs.send_message('area3_W30;')
	gs.send_message('area3_TL31;')
	gs.send_message('area4_W40;')
	gs.send_message('area4_TL41;')
	gs.send_message('hallway1_WK10;')
	gs.send_message('hallway1_TLK11;')
	gs.send_message('hallway2_WK20;')
	gs.send_message('hallway2_TLK21;')

def emergency_off():
	if not settings.emergencyStatus:
		for out in settings.outs:
			reset_out(out)

def reset_out(message):
	if settings.outs[message]:
		gs.send_message(f'{message}1;')
	else:
		gs.send_message(f'{message}0;')