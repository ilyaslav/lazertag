import settings
import json
import threading
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
			if settings.gameStatus:
				stop_script()
			else:
				start_script()
		elif mes == 'game_button0':
			settings.inputs['game_button'] = False
		elif mes == 'start_stage1':
			settings.inputs['start_stage'] = True
		elif mes == 'start_stage0':
			settings.inputs['start_stage'] = False
		if mes == 'stop_stage1':
			settings.inputs['stop_stage'] = True
		elif mes == 'stop_stage0':
			settings.inputs['stop_stage'] = False
		if mes == 'sound_button1':
			settings.inputs['sound_button'] = True
		elif mes == 'sound_button0':
			settings.inputs['sound_button'] = False
		if mes == 'light_button1':
			settings.inputs['light_button'] = True
		elif mes == 'light_button0':
			settings.inputs['light_button'] = False
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

def start_script():
	if settings.readyToStart:
		settings.initStatus = True
		settings.event = True
	elif settings.initStatus:
		settings.gameStatus = True
		settings.event = True

def stop_script():
	settings.readyToStart = False
	settings.initStatus = False
	settings.gameStatus = False
	settings.event = True

def check_to_start():
	for status in settings.settingsToStart:
		if not settings.settingsToStart[status]:
			settings.readyToStart = False
			return settings.readyToStart
	if not settings.gameStatus and not settings.initStatus:
		settings.readyToStart = True
	return settings.readyToStart

def init_settings():
	pass

def init_game():
	settings.outs['hallway1_WK1'] = True
	settings.outs['give_LK1'] = False
	settings.outs['AdminLight'] = False
	if not settings.emergencyStatus:
		reset_out('hallway1_WK1')
		reset_out('AdminLight')
		reset_out('give_LK1')

def start_game():
	settings.outs['tableButton'] = False
	settings.outs['hallway1_WK1'] = False
	settings.outs['hallway1_WK1'] = True
	settings.outs['AdminLight'] = True
	if not settings.emergencyStatus:
		reset_out('tableButton')
		reset_out('hallway1_WK1')
		reset_out('AdminLight')
		reset_out('give_LK1')

def stop_game():
	pass

def start_stage():
	pass

def stop_stage():
	pass

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
	reset_out('area1_W1')
	reset_out('area1_TL1')
	reset_out('area2_W2')
	reset_out('area2_TL2')
	reset_out('area3_W3')
	reset_out('area3_TL3')
	reset_out('area4_W4')
	reset_out('area4_TL4')
	reset_out('hallway1_WK1')
	reset_out('hallway1_TLK1')
	reset_out('hallway2_WK2')
	reset_out('hallway2_TLK2')

def reset_out(message):
	if settings.outs[message]:
		gs.send_message(f'{message}1;')
	else:
		gs.send_message(f'{message}0;')