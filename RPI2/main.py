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
		if mes[:2] == 'r2':
			gh.reset_out(mes[:-1], bool(mes[-1]))
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
