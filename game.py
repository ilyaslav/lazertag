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
		pass

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
	pass

def start_game():
	pass

def stop_game():
	pass

def start_stage():
	pass

def stop_stage():
	pass

def reset_out(message):
	if settings.outs[message]:
		gs.send_message(f'{message}1;')
	else:
		gs.send_message(f'{message}0;')