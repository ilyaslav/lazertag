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
		if mes == 'r1i11':
			settings.inputs['r1i1'] = settings.HIGHT
			start_main_timer()
		elif mes == 'r1i10':
			settings.inputs['r1i1'] = settings.LOW
			stop_main_timer()
		elif mes == 'r1i21':
			settings.inputs['r1i2'] = settings.HIGHT
			start_stage_timer1()
		elif mes == 'r1i20':
			settings.inputs['r1i2'] = settings.LOW
			stop_stage_timer1()
		if mes == 'r1i31':
			settings.inputs['r1i3'] = settings.HIGHT
			start_stage_timer0()
		elif mes == 'r1i30':
			settings.inputs['r1i3'] = settings.LOW
			stop_stage_timer0()
		if mes == 'r1i41':
			settings.inputs['r1i4'] = settings.HIGHT
			start_sound_timer()
		elif mes == 'r1i40':
			settings.inputs['r1i4'] = settings.LOW
			stop_sound_timer()
		if mes == 'r1i51':
			settings.inputs['r1i5'] = settings.HIGHT
			start_emergency_timer()
		elif mes == 'r1i50':
			settings.inputs['r1i5'] = settings.LOW
			stop_emergency_timer()
		if mes[:-1] in settings.inputs.keys():
			if mes[-1] == '1':
				settings.inputs[mes[:-1]] = settings.HIGHT
			else:
				settings.inputs[mes[:-1]] = settings.LOW
		settings.diagnosticEvent = True
		#elif mes == 'signal_R0':
		#	settings.inputs['r1i6'] = settings.LOW
		#if mes == 'signal_G1':
		#	settings.inputs['r1i7'] = settings.HIGHT
		#elif mes == 'signal_G0':
		#	settings.inputs['r1i7'] = settings.LOW
		#if mes == 'signal_B1':
		#	settings.inputs['r1i8'] = settings.HIGHT
		#elif mes == 'signal_B0':
		#	settings.inputs['r1i8'] = settings.LOW
		#if mes == 'takeFlag_A1':
		#	settings.inputs['r1i9'] = settings.HIGHT
		#elif mes == 'takeFlag_A0':
		#	settings.inputs['r1i9'] = settings.LOW
		#if mes == 'takeFlag_B1':
		#	settings.inputs['r1i10'] = settings.HIGHT
		#elif mes == 'takeFlag_B0':
		#	settings.inputs['r1i10'] = settings.LOW
		#if mes == 'giveFlag_A1':
		#	settings.inputs['r1i11'] = settings.HIGHT
		#elif mes == 'giveFlag_A0':
		#	settings.inputs['r1i11'] = settings.LOW
		#if mes == 'giveFlag_B1':
		#	settings.inputs['r1i12'] = settings.HIGHT
		#elif mes == 'giveFlag_B0':
		#	settings.inputs['r1i12'] = settings.LOW
		#if mes == 'bomb_activated1':
		#	settings.inputs['r1i13'] = settings.HIGHT
		#elif mes == 'bomb_activated0':
		#	settings.inputs['r1i13'] = settings.LOW
		#if mes == 'bomb_planted1':
		#	settings.inputs['r1i14'] = settings.HIGHT
		#elif mes == 'bomb_planted0':
		#	settings.inputs['r1i14'] = settings.LOW

	def init_settings(self):
		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)
		else:
			self.emergency_on()

	def emergency_on(self):
		self.send_message('r2o70;')
		self.send_message('r2081;')
		self.send_message('r2o90;')
		self.send_message('r2o101;')
		self.send_message('r2o110;')
		self.send_message('r2o121;')
		self.send_message('r2o130;')
		self.send_message('r2o141;')
		self.send_message('r2o150;')
		self.send_message('r2o161;')
		self.send_message('r2o170;')
		self.send_message('r2o181;')

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
		if message not in settings.static_outs:
			settings.diagnosticEvent = True
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
		if False in list(settings.settingsToStart.values()):
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
		if settings.check_game_score:
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
		'r1o1': settings.HIGHT,
		'r1o2': settings.HIGHT,
		'r1o3': settings.HIGHT,
		'r1o4': settings.HIGHT,
		'r1o5': settings.HIGHT,
		'r1o6': settings.HIGHT,
		'r2o7': settings.LOW,
		'r2o8': settings.HIGHT,
		'r2o9': settings.LOW,
		'r2o10': settings.HIGHT,
		'r2o11': settings.LOW,
		'r2o12': settings.HIGHT,
		'r2o13': settings.LOW,
		'r2o14': settings.HIGHT,
		'r2o15': settings.LOW,
		'r2o16': settings.HIGHT,
		'r2o17': settings.LOW,
		'r2o18': settings.HIGHT,
		'r2o19': settings.HIGHT,
		'r2o20': settings.LOW,
		'r2o21': settings.LOW
	}
		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def init_game(self):
		settings.outs['r2o15'] = settings.HIGHT
		settings.outs['r2o19'] = settings.LOW
		settings.outs['r1o6'] = settings.LOW
		self.play_music(1)

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def start_game(self):
		settings.outs['r1o1'] = settings.LOW
		settings.outs['r2o15'] = settings.LOW
		settings.outs['r2o19'] = settings.HIGHT
		#settings.outs['AdminLight'] = settings.HIGHT
		self.play_music(2)

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def stop_game(self):
		self.stop_fon_track()
		self.init_settings()

	def init_stage(self):
		settings.outs['r2o7'] = settings.HIGHT
		settings.outs['r2o11'] = settings.HIGHT
		if settings.currentStage%2:
			settings.outs['r1o2'] = settings.LOW
			settings.outs['r1o5'] = settings.LOW
		else:
			settings.outs['r1o4'] = settings.LOW
			settings.outs['r1o3'] = settings.LOW
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
		self.init_stage()
		self.play_music(18)
		if settings.currentStage%2:
			settings.outs['r1o2'] = settings.HIGHT
			settings.outs['r1o5'] = settings.HIGHT
		else:
			settings.outs['r1o4'] = settings.HIGHT
			settings.outs['r1o3'] = settings.HIGHT
		if not settings.wowEffects:
			settings.outs['r2o7'] = settings.LOW
			settings.outs['r2o11'] = settings.LOW
		else:
			settings.outs['r2o7'] = settings.HIGHT
			settings.outs['r2o8'] = settings.LOW
			settings.outs['r2o9'] = settings.HIGHT
			settings.outs['r2o10'] = settings.LOW
			settings.outs['r2o11'] = settings.HIGHT
			settings.outs['r2o12'] = settings.LOW
			settings.outs['r2o13'] = settings.HIGHT
			settings.outs['r2o14'] = settings.LOW
			settings.outs['r2o15'] = settings.HIGHT
			settings.outs['r2o16'] = settings.LOW
			settings.outs['r2o17'] = settings.HIGHT
			settings.outs['r2o18'] = settings.LOW
			settings.outs['r2o19'] = settings.HIGHT

		if not settings.emergencyStatus:
			for out in settings.outs:
				self.reset_out(out)

	def stop_stage(self):
		if settings.wowEffects:
			self.play_music(17)
			settings.outs['r2o7'] = settings.LOW
			settings.outs['r2o8'] = settings.HIGHT
			settings.outs['r2o9'] = settings.LOW
			settings.outs['r2o10'] = settings.HIGHT
			settings.outs['r2o11'] = settings.LOW
			settings.outs['r2o12'] = settings.HIGHT
			settings.outs['r2o13'] = settings.LOW
			settings.outs['r2o14'] = settings.HIGHT
			settings.outs['r2o15'] = settings.LOW
			settings.outs['r2o16'] = settings.HIGHT
			settings.outs['r2o17'] = settings.LOW
			settings.outs['r2o18'] = settings.HIGHT
			settings.outs['r2o19'] = settings.LOW

			if not settings.emergencyStatus:
				for out in settings.outs:
					self.reset_out(out)
