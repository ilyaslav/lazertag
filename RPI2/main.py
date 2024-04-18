from _client import Client
from _gpio import PiHandler
from _music import Music
import threading

class GameHandler(PiHandler):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)


class GameClient(Client):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def messageHandler(self, mes):
		if mes == 'area1_W11':
			gh.area1_W11()
		elif mes == 'area1_TL11':
			gh.area1_TL11()
		elif mes == 'area1_TL11':
			gh.area1_TL11()
		elif mes == 'area2_W21':
			gh.area2_W21()
		elif mes == 'area2_TL21':
			gh.area2_TL21()
		elif mes == 'area3_W31':
			gh.area3_W31()
		elif mes == 'area3_TL31':
			gh.area3_TL31()
		elif mes == 'area4_W41':
			gh.area4_W41()
		elif mes == 'area4_TL41':
			gh.area4_TL41()
		elif mes == 'hallway1_WK11':
			gh.hallway1_WK11()
		elif mes == 'hallway1_TLK11':
			gh.hallway1_TLK11()
		elif mes == 'hallway2_WK21':
			gh.hallway2_WK21()
		elif mes == 'hallway2_TLK21':
			gh.hallway2_TLK21()
		elif mes == 'give_LK11':
			gh.give_LK11()
		elif mes == 'medicBag_A1':
			gh.medicBag_A1()
		elif mes == 'medicBag_B1':
			gh.medicBag_B1()

		elif mes == 'area1_W10':
			gh.area1_W10()
		elif mes == 'area1_TL10':
			gh.area1_TL10()
		elif mes == 'area1_TL10':
			gh.area1_TL10()
		elif mes == 'area2_W20':
			gh.area2_W20()
		elif mes == 'area2_TL20':
			gh.area2_TL20()
		elif mes == 'area3_W30':
			gh.area3_W30()
		elif mes == 'area3_TL30':
			gh.area3_TL30()
		elif mes == 'area4_W40':
			gh.area4_W40()
		elif mes == 'area4_TL40':
			gh.area4_TL40()
		elif mes == 'hallway1_WK10':
			gh.hallway1_WK10()
		elif mes == 'hallway1_TLK10':
			gh.hallway1_TLK10()
		elif mes == 'hallway2_WK20':
			gh.hallway2_WK20()
		elif mes == 'hallway2_TLK20':
			gh.hallway2_TLK20()
		elif mes == 'give_LK10':
			gh.give_LK10()
		elif mes == 'medicBag_A0':
			gh.medicBag_A0()
		elif mes == 'medicBag_B0':
			gh.medicBag_B0()

		elif mes[:4] == 'play':
			gm.play(mes[4:])
		elif mes[:4] == 'stop':
			gm.stop(mes[4:])
		elif mes[:5] == 'pause':
			gm.pause(mes[5:])
		elif mes[:6] == 'volume':
			gm.change_volume(int(mes[6:]))

	def send_inputs(self):
		inputs = PiHandler.get_inputs()


gc = GameClient()
gh = GameHandler()
gm = Music()


def main():
	#threading.Thread(target=gc.clientFunction, daemon=True).start()
	#gh.sensors_loop()
	gc.clientFunction()


if __name__ == '__main__':
	main()
