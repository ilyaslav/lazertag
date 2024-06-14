from datetime import datetime
LOW = True
HIGHT = False

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
check_game_score = True
delayTime = 5

def check_last():
	return stages.count(True) == 1

def check_end():
	return stages.count(True) == 0

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
volumeStatus = True
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

diagnosticEvent = False

settingsToStart = {
	'scriptsMap': False,
	'players': False,
	'celebrant': False,
	'instructors': False
}

settingsToWrite = {
	'scriptsMap': '',
	'synchronization': 'Нет',
	'scheduleStart': None,
	'players': '',
	'celebrant': '',
	'instructors': '',
	'initGame': None,
	'startGame': None,
	'giveTime': None,
	'brifTime': None,
	'gameTime': None,
	'downtime': None,
	'fullDowntime': None,
	'fullGameTime': None,
	'stageTime': [],
	'stopGame': None
}

def getPlayers():
	return settingsToWrite['players']

def getScriptsMap():
	return settingsToWrite['scriptsMap']

def getSynchronization():
	return settingsToWrite['synchronization']

def getInitGame():
	return settingsToWrite['initGame']

def getGiveTime():
	return settingsToWrite['giveTime']

def getGiveTimeRatio():
	return settingsToWrite['giveTime'].total_seconds()/settingsToWrite['players']

def getFullGameTime():
	return settingsToWrite['fullGameTime']

def getStopGame():
	return settingsToWrite['stopGame']

def getInstructors():
	return settingsToWrite['instructors']

def getDowntimeRatio():
	return settingsToWrite['fullDowntime'].total_seconds() * 100 / settingsToWrite['fullGameTime'].total_seconds()

def getBrifTime():
	time_format = "%H:%M:%S"
	settingsToWrite['brifTime'] = \
		datetime.strptime(settingsToWrite['stageTime'][0], time_format)-\
			datetime.strptime(settingsToWrite['startGame'], time_format)
	return settingsToWrite['brifTime']

def getGameTime():
	j = 0
	t = None
	t1 = "00:00:00"
	time_format = "%H:%M:%S"
	res = datetime.strptime(t1, time_format)
	for i in settingsToWrite['stageTime']:
		j+=1
		if j % 2:
			t = i
		else:
			res += datetime.strptime(i, time_format) - datetime.strptime(t, time_format)
	settingsToWrite['gameTime'] = res
	return res

def getDowntime():
	j = 0
	t = None
	t1 = "00:00:00"
	time_format = "%H:%M:%S"
	res = datetime.strptime(t1, time_format)
	for i in settingsToWrite['stageTime']:
		j+=1
		if j % 2 and j > 1:
			res += datetime.strptime(i, time_format) - datetime.strptime(t, time_format)
		else:
			t = i
	settingsToWrite['downtime'] = res
	return res

def getFullDowntime():
	time_format = "%H:%M:%S"
	t1 = "00:00:00"
	settingsToWrite['fullDowntime'] = \
		settingsToWrite['giveTime']+\
			settingsToWrite['brifTime']+\
				settingsToWrite['downtime']-\
				datetime.strptime(t1, time_format)
	print(settingsToWrite['fullDowntime'])
	return settingsToWrite['fullDowntime']

def getStageNames():
	res = ''
	for stage in stageNames:
		res+= stage
	return res

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
	'r1o1': HIGHT,
	'r1o2': HIGHT,
	'r1o3': HIGHT,
	'r1o4': HIGHT,
	'r1o5': HIGHT,
	'r1o6': HIGHT,
	'r2o7': LOW,
	'r2o8': HIGHT,
	'r2o9': LOW,
	'r2o10': HIGHT,
	'r2o11': LOW,
	'r2o12': HIGHT,
	'r2o13': LOW,
	'r2o14': HIGHT,
	'r2o15': LOW,
	'r2o16': HIGHT,
	'r2o17': LOW,
	'r2o18': HIGHT,
	'r2o19': HIGHT,
	'r2o20': LOW,
	'r2o21': LOW
}
static_outs = []
def clear_static_outs():
	for out in static_outs:
		outs[out] = not outs[out]
	static_outs.clear()

inputs = {
	'r1i1': LOW,
	'r1i2': LOW,
	'r1i3': LOW,
	'r1i4': LOW,
	'r1i5': LOW,
	'r1i6': LOW,
	'r1i7': LOW,
	'r1i8': LOW,
	'r1i9': LOW,
	'r1i10': LOW,
	'r1i11': LOW,
	'r1i12': LOW,
	'r1i13': LOW,
	'r1i14': LOW
}

music4 = 0

if __name__ == '__main__':
	pass
