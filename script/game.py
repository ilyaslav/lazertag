import settings
import json
import threading
import time
from server import Server

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

class GameServer(Server):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def message_handler(self, mes):
		print(f'Принято сообщение: {mes}')
		if mes == 'game_button1':
			settings.inputs['game_button'] = settings.HIGHT
			start_main_timer()
		elif mes == 'game_button0':
			settings.inputs['game_button'] = settings.LOW
			stop_main_timer()
		elif mes == 'start_stage1':
			settings.inputs['start_stage'] = settings.HIGHT
			start_stage_timer1()
		elif mes == 'start_stage0':
			settings.inputs['start_stage'] = settings.LOW
			stop_stage_timer1()
		if mes == 'stop_stage1':
			settings.inputs['stop_stage'] = settings.HIGHT
			start_stage_timer0()
		elif mes == 'stop_stage0':
			settings.inputs['stop_stage'] = settings.LOW
			stop_stage_timer0()
		if mes == 'sound_button1':
			settings.inputs['sound_button'] = settings.HIGHT
			start_sound_timer()
		elif mes == 'sound_button0':
			settings.inputs['sound_button'] = settings.LOW
			stop_sound_timer()
		if mes == 'light_button1':
			settings.inputs['light_button'] = settings.HIGHT
			start_emergency_timer()
		elif mes == 'light_button0':
			settings.inputs['light_button'] = settings.LOW
			stop_emergency_timer()
		if mes == 'signal_R1':
			settings.inputs['signal_R'] = settings.HIGHT
		elif mes == 'signal_R0':
			settings.inputs['signal_R'] = settings.LOW
		if mes == 'signal_G1':
			settings.inputs['signal_G'] = settings.HIGHT
		elif mes == 'signal_G0':
			settings.inputs['signal_G'] = settings.LOW
		if mes == 'signal_B1':
			settings.inputs['signal_B'] = settings.HIGHT
		elif mes == 'signal_B0':
			settings.inputs['signal_B'] = settings.LOW
		if mes == 'takeFlag_A1':
			settings.inputs['takeFlag_A'] = settings.HIGHT
		elif mes == 'takeFlag_A0':
			settings.inputs['takeFlag_A'] = settings.LOW
		if mes == 'takeFlag_B1':
			settings.inputs['takeFlag_B'] = settings.HIGHT
		elif mes == 'takeFlag_B0':
			settings.inputs['takeFlag_B'] = settings.LOW
		if mes == 'giveFlag_A1':
			settings.inputs['giveFlag_A'] = settings.HIGHT
		elif mes == 'giveFlag_A0':
			settings.inputs['giveFlag_A'] = settings.LOW
		if mes == 'giveFlag_B1':
			settings.inputs['giveFlag_B'] = settings.HIGHT
		elif mes == 'giveFlag_B0':
			settings.inputs['giveFlag_B'] = settings.LOW
		if mes == 'bomb_activated1':
			settings.inputs['bomb_activated'] = settings.HIGHT
		elif mes == 'bomb_activated0':
			settings.inputs['bomb_activated'] = settings.LOW
		if mes == 'bomb_planted1':
			settings.inputs['bomb_planted'] = settings.HIGHT
		elif mes == 'bomb_planted0':
			settings.inputs['bomb_planted'] = settings.LOW

	def init_settings(self):
		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)
		else:
			self.emergency_on()

	def emergency_on(self):
		self.send_message('area1_W10;')
		self.send_message('area1_TL11;')
		self.send_message('area2_W20;')
		self.send_message('area2_TL21;')
		self.send_message('area3_W30;')
		self.send_message('area3_TL31;')
		self.send_message('area4_W40;')
		self.send_message('area4_TL41;')
		self.send_message('hallway1_WK10;')
		self.send_message('hallway1_TLK11;')
		self.send_message('hallway2_WK20;')
		self.send_message('hallway2_TLK21;')

	def reset_out(self, message):
		if settings.outs[message]:
			self.send_message(f'{message}1;')
		else:
			self.send_message(f'{message}0;')

class Game:
	def __init__(self) -> None:
		data = {}
		with open('data.txt') as json_file:
			data = json.load(json_file)
		settings.time = data['time']
		self.set_main_time()
		self.set_stage_time()
		settings.numberOfStage = data['scripts_map'][0]['numberOfStage']
		settings.scriptsMap = data['scripts_map'][0]['id']

		self.gs = GameServer()
		threading.Thread(target=self.gs.start_server, daemon=True).start()

	def set_main_time(self):
		settings.mainTime = settings.time[0]['mainTime']
		settings.addedTime = 0
	def set_stage_time(self):
		settings.stageTime = settings.time[0]['t5']

	def reset_out(self, message):
		self.gs.reset_out(message)

	def emergency_on(self):
		self.gs.emergency_on()
	def emergency_off(self):
		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def check_timers(self):
		if settings.mainTimer:
			if self.check_time(settings.startMainTime):
				if settings.gameStatus:
					self.stop_game_script()
				else:
					self.start_game_script()
		if settings.stageTimer1:
			if self.check_time(settings.startStageTime1):
				self.start_stage_script()
		if settings.stageTimer0:
			if self.check_time(settings.startStageTime0):
				self.stop_stage_script()
		if settings.soundTimer:
			if self.check_time(settings.startSoundTime):
				self.sound_script()
		if settings.emergencyTimer:
			if self.check_time(settings.startEmergencyTime):
				self.emergency_script()

	def check_time(self, timer):
		return time.time() - timer >= 2 and time.time() - timer < 4

	def start_game_script(self):
		settings.mainTimer = False
		if settings.readyToStart:
			settings.initStatus = True
			settings.event = True
		elif settings.initStatus:
			settings.gameStatus = True
			settings.event = True

	def stop_game_script(self):
		settings.mainTimer = False
		settings.readyToStart = False
		settings.initStatus = False
		settings.gameStatus = False
		settings.event = True

	def start_stage_script(self):
		settings.stageTimer1 = False
		if not settings.stageStatus and settings.gameStatus:
			settings.startStageEvent = True

	def stop_stage_script(self):
		settings.stageTimer0 = False
		if settings.stageStatus and settings.gameStatus:
			settings.stopStageEvent = True

	def sound_script(self):
		settings.soundTimer = False
		if settings.volume:
			settings.volume = 0
		else:
			settings.volume = 100
		settings.volumeEvent = True

	def emergency_script(self):
		settings.emergencyTimer = False
		settings.emergencyEvent = True

	def check_to_start(self):
		for status in settings.settingsToStart:
			if not settings.settingsToStart[status]:
				settings.readyToStart = False
				return settings.readyToStart
		if not settings.gameStatus and not settings.initStatus:
			settings.readyToStart = True
		return settings.readyToStart

	def change_volume(self):
		self.gs.send_message(f'volume{int(settings.volume)};')

	def play_music(self, music, type_ = 'track'):
		music = f"{type_}/{music}"
		self.gs.send_message(f'play{music};')

	def pause_music(self, music, type_ = 'track'):
		music = f"{type_}/{music}"
		self.gs.send_message(f'pause{music};')

	def stop_music(self, music, type_ = 'track'):
		music = f"{type_}/{music}"
		self.gs.send_message(f'stop{music};')

	def play_four_min(self):
		self.play_music(12)

	def stop_fon_track(self):
		self.stop_music(18)

	def end_stage_music_event(self):
		threading.Thread(target = self.end_stage_music, daemon = True).start()

	def end_game_music_event(self):
		threading.Thread(target = self.end_game_music, daemon = True).start()

	def end_game_music(self):
		settings.currentStage = 0
		red = settings.getCount('red')
		blue = settings.getCount('blue')
		time.sleep(3)
		self.play_music(3)
		time.sleep(4.5)
		self.play_music(red, type_ = 'up')
		time.sleep(1.5)
		self.play_music(blue, type_ = 'down')
		time.sleep(1.5)
		settings.counters['mainСounterRed'] = 0
		settings.counters['mainСounterBlue'] = 0
		if red > blue:
			self.play_music(4)
		elif red < blue:
			self.play_music(5)
		time.sleep(3)
		self.play_music(6)

	def end_stage_music(self):
		self.stop_fon_track()
		self.play_music(13)
		time.sleep(3)
		if settings.check_end():
			pass
		elif not settings.currentStage%2: #если прошел 1 подэтап
			self.play_music(14)
			time.sleep(4)
		else:
			#проверка следующего этапа
			stage_name = settings.getNextStageName()
			if 'Death match' in stage_name:
				pass
			elif 'Контрольная точка' in stage_name or\
			'Штурм' in stage_name:
				self.play_music(15)
			elif 'Бомба' in stage_name:
				self.play_music(16)


	def init_settings(self):
		settings.outs = {
		'tableButton': settings.HIGHT,
		'ARed': settings.HIGHT,
		'ABlue': settings.HIGHT,
		'BRed': settings.HIGHT,
		'BBlue': settings.HIGHT,
		'AdminLight': settings.HIGHT,
		'area1_W1': settings.LOW,
		'area1_TL1': settings.HIGHT,
		'area2_W2': settings.LOW,
		'area2_TL2': settings.HIGHT,
		'area3_W3': settings.LOW,
		'area3_TL3': settings.HIGHT,
		'area4_W4': settings.LOW,
		'area4_TL4': settings.HIGHT,
		'hallway1_WK1': settings.LOW,
		'hallway1_TLK1': settings.HIGHT,
		'hallway2_WK2': settings.LOW,
		'hallway2_TLK2': settings.HIGHT,
		'give_LK1': settings.HIGHT,
		'medicBag_A': settings.LOW,
		'medicBag_B': settings.LOW
	}
		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def init_game(self):
		settings.outs['hallway1_WK1'] = settings.HIGHT
		settings.outs['give_LK1'] = settings.LOW
		settings.outs['AdminLight'] = settings.LOW
		self.play_music(1)

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def start_game(self):
		settings.outs['tableButton'] = settings.LOW
		settings.outs['hallway1_WK1'] = settings.LOW
		settings.outs['give_LK1'] = settings.HIGHT
		#settings.outs['AdminLight'] = settings.HIGHT
		self.play_music(2)

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def stop_game(self):
		self.stop_fon_track()
		self.init_settings()

	def init_stage(self):
		settings.outs['area1_W1'] = settings.HIGHT
		settings.outs['area3_W3'] = settings.HIGHT
		if not settings.currentStage%2:
			settings.outs['ARed'] = settings.LOW
			settings.outs['BBlue'] = settings.LOW
		else:
			settings.outs['BRed'] = settings.LOW
			settings.outs['ABlue'] = settings.LOW
		self.play_music(17)

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

		time.sleep(5.5)
		stage_name = settings.getStageName()
		if stage_name in "Death match +":
			self.play_music(7)
			time.sleep(8)
		elif stage_name in "Контрольная точка +":
			self.play_music(8)
			time.sleep(6)
		elif stage_name in "Штурм +":
			self.play_music(9)
			time.sleep(6)
		elif stage_name in "Бомба +":
			self.play_music(10)
			time.sleep(6)
		else:#if stage_name in "Без сценария +":
			self.play_music(11)
			time.sleep(5)

	def start_stage(self):
		print(f'WOWWOWOWOW {settings.wowEffects}')
		self.init_stage()
		self.play_music(18)
		if not settings.currentStage%2:
			settings.outs['ARed'] = settings.HIGHT
			settings.outs['BBlue'] = settings.HIGHT
		else:
			settings.outs['BRed'] = settings.HIGHT
			settings.outs['ABlue'] = settings.HIGHT
		if not settings.wowEffects:
			settings.outs['area1_W1'] = settings.LOW
			settings.outs['area3_W3'] = settings.LOW
		else:
			settings.outs['area1_W1'] = settings.HIGHT
			settings.outs['area1_TL1'] = settings.LOW
			settings.outs['area2_W2'] = settings.HIGHT
			settings.outs['area2_TL2'] = settings.LOW
			settings.outs['area3_W3'] = settings.HIGHT
			settings.outs['area3_TL3'] = settings.LOW
			settings.outs['area4_W4'] = settings.HIGHT
			settings.outs['area4_TL4'] = settings.LOW
			settings.outs['hallway1_WK1'] = settings.HIGHT
			settings.outs['hallway1_TLK1'] = settings.LOW
			settings.outs['hallway2_WK2'] = settings.HIGHT
			settings.outs['hallway2_TLK2'] = settings.LOW
			settings.outs['give_LK1'] = settings.HIGHT

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def stop_stage(self):
		if settings.wowEffects:
			self.play_music(17)
			settings.outs['area1_W1'] = settings.LOW
			settings.outs['area1_TL1'] = settings.HIGHT
			settings.outs['area2_W2'] = settings.LOW
			settings.outs['area2_TL2'] = settings.HIGHT
			settings.outs['area3_W3'] = settings.LOW
			settings.outs['area3_TL3'] = settings.HIGHT
			settings.outs['area4_W4'] = settings.LOW
			settings.outs['area4_TL4'] = settings.HIGHT
			settings.outs['hallway1_WK1'] = settings.LOW
			settings.outs['hallway1_TLK1'] = settings.HIGHT
			settings.outs['hallway2_WK2'] = settings.LOW
			settings.outs['hallway2_TLK2'] = settings.HIGHT
			settings.outs['give_LK1'] = settings.LOW

			if not settings.emergencyStatus:
				for out in settings.outs:
					self.reset_out(out)
