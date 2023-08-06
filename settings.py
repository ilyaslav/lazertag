time = {}
mainTime = 0
stageTime = 0
addedTime = 0

def get_hours(time):
	hours = int(time / 3600)
	if hours < 10:
		return f'0{hours}'
	else:
		return f'{hours}'

def get_minutes(time):
	minutes = int((time % 3600) / 60)
	if minutes < 10:
		return f'0{minutes}'
	else:
		return f'{minutes}'

def get_seconds(time):
	seconds = time % 60
	if seconds < 10:
		return f'0{seconds}'
	else:
		return f'{seconds}'

gameStatus = False
initStatus = False
readyToStart = False
event = False

emergencyStatus = False
emergencyEvent = False

scriptsMap = 0

currentStage = 0
stages = [False, False, False, False, False, False, False, False, False, False]
numberOfStage = 0
startStageEvent = False
stopStageEvent = False
restartStageEvent = False
excludeStageEvent = False
includeStageEvent = False
stageStatus = False
changeStageEvent = False
wowEffects = False
stageTimer = 'increasing' #'decreasing'


settingsToStart = {
	'scriptsMap': False,
	'players': True,
	'selebrant': True,
	'instructors': True
}


counters = {
	'mainСounterRed': 0,
	'mainСounterBlue': 0,
	(1,'red'): 0,
	(1,'blue'): 0,
	(2,'red'): 0,
	(2,'blue'): 0,
	(3,'red'): 0,
	(3,'blue'): 0,
	(4,'red'): 0,
	(4,'blue'): 0,
	(5,'red'): 0,
	(5,'blue'): 0,
	(6,'red'): 0,
	(6,'blue'): 0,
	(7,'red'): 0,
	(7,'blue'): 0,
	(8,'red'): 0,
	(8,'blue'): 0,
	(9,'red'): 0,
	(9,'blue'): 0,
	(10,'red'): 0,
	(10,'blue'): 0
}


outs = {
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


inputs = {
	'game_button': False,
	'start_stage': False,
	'stop_stage': False,
	'sound_button': False,
	'light_button': False,
	'signal_R': False,
	'signal_G': False,
	'signal_B': False,
	'takeFlag_A': False,
	'takeFlag_B': False,
	'giveFlag_A': False,
	'giveFlag_B': False,
	'bomb_activated': False,
	'bomb_planted': False
}