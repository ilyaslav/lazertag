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
		if mes == 'tableButton1':
			gh.tableButton1()
		elif mes == 'ARed1':
			gh.ARed1()
		elif mes == 'ABlue1':
			gh.ABlue1()
		elif mes == 'BRed1':
			gh.BRed1()
		elif mes == 'BBlue1':
			gh.BBlue1()
		elif mes == 'AdminLight1':
			gh.AdminLight1()
		
		if mes == 'tableButton0':
			gh.tableButton0()
		elif mes == 'ARed0':
			gh.ARed0()
		elif mes == 'ABlue0':
			gh.ABlue0()
		elif mes == 'BRed0':
			gh.BRed0()
		elif mes == 'BBlue0':
			gh.BBlue0()
		elif mes == 'AdminLight0':
			gh.AdminLight0()

		elif mes[:4] == 'play':
			gm.play(int(mes[4:]))
		elif mes[:4] == 'stop':
			gm.stop(int(mes[4:]))
		elif mes[:5] == 'pause':
			gm.pause(int(mes[5:]))
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