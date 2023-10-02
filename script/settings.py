time = {}
mainTime = 0
stageTime = 0
addedTime = 0

startMainTime = 0
startStageTime1 = 0
startStageTime0 = 0
startSoundTime = 0
startEmergencyTime = 0
mainTimer = False
stageTimer1 = False
stageTimer0 = False
soundTimer = False
emergencyTimer = False

def check_last():
	return stages.count(True) == 1

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

volume = 100
volumeEvent = False

scriptsMap = 0

currentStage = 0
stages = [False, False, False, False, False, False, False, False, False, False]
stageNames = ['Сценарий не выбран','Сценарий не выбран','Сценарий не выбран','Сценарий не выбран','Сценарий не выбран']
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

def getStageName():
	return stageNames[int((currentStage-1)/2)]

def getNextStageName():
	print(f'currentStage {currentStage}')
	return stageNames[int(currentStage/2)]

def findCounter(color):
	if color == 'red':
		if currentStage == 1:
			return counters[(1,'red')]
		elif currentStage == 2:
			return counters[(2,'red')]
		elif currentStage == 3:
			return counters[(3,'red')]
		elif currentStage == 4:
			return counters[(4,'red')]
		elif currentStage == 5:
			return counters[(5,'red')]
		elif currentStage == 6:
			return counters[(6,'red')]
		elif currentStage == 7:
			return counters[(7,'red')]
		elif currentStage == 8:
			return counters[(8,'red')]
		elif currentStage == 9:
			return counters[(9,'red')]
		elif currentStage == 10:
			return counters[(10,'red')]
		else:
			return counters['mainСounterRed']
	else:
		if currentStage == 1:
			return counters[(1,'blue')]
		elif currentStage == 2:
			return counters[(2,'blue')]
		elif currentStage == 3:
			return counters[(3,'blue')]
		elif currentStage == 4:
			return counters[(4,'blue')]
		elif currentStage == 5:
			return counters[(5,'blue')]
		elif currentStage == 6:
			return counters[(6,'blue')]
		elif currentStage == 7:
			return counters[(7,'blue')]
		elif currentStage == 8:
			return counters[(8,'blue')]
		elif currentStage == 9:
			return counters[(9,'blue')]
		elif currentStage == 10:
			return counters[(10,'blue')]
		else:
			return counters['mainСounterBlue']

def getCount(color):
	return findCounter(color)

def setCount(color, count):
	counter = findCounter(color)
	counter = count

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

if __name__ == '__main__':
	pass