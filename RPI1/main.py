from _client import Client
from _gpio import PiHandler
from _music import Music
import threading

class GameHandler(PiHandler):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def game_button1(self):
		gc.send_message('game_button1;')
	def game_button0(self):
		gc.send_message('game_button0;')
	def start_stage1(self):
		gc.send_message('start_stage1;')
	def start_stage0(self):
		gc.send_message('start_stage0;')
	def stop_stage1(self):
		gc.send_message('stop_stage1;')
	def stop_stage0(self):
		gc.send_message('stop_stage0;')
	def sound_button1(self):
		gc.send_message('sound_button1;')
	def sound_button0(self):
		gc.send_message('sound_button0;')
	def light_button1(self):
		gc.send_message('light_button1;')
	def light_button0(self):
		gc.send_message('light_button0;')
	def signal_R1(self):
		gc.send_message('signal_R1;')
	def signal_R0(self):
		gc.send_message('signal_R0;')
	def handRead1(self):
		gc.send_message('signal_G1;')
	def handRead0(self):
		gc.send_message('signal_G0;')
	def signal_B1(self):
		gc.send_message('signal_B1;')
	def signal_B0(self):
		gc.send_message('signal_B0;')
	def takeFlag_A1(self):
		gc.send_message('takeFlag_A1;')
	def takeFlag_A0(self):
		gc.send_message('takeFlag_A0;')
	def takeFlag_B1(self):
		gc.send_message('takeFlag_B1;')
	def takeFlag_B0(self):
		gc.send_message('takeFlag_B0;')
	def giveFlag_A1(self):
		gc.send_message('giveFlag_A1;')
	def giveFlag_A0(self):
		gc.send_message('giveFlag_A0;')
	def giveFlag_B1(self):
		gc.send_message('giveFlag_B1;')
	def giveFlag_B0(self):
		gc.send_message('giveFlag_B0;')
	def bomb_activated1(self):
		gc.send_message('bomb_activated1;')
	def bomb_activated0(self):
		gc.send_message('bomb_activated0;')
	def bomb_planted1(self):
		gc.send_message('bomb_planted1;')
	def bomb_planted0(self):
		gc.send_message('bomb_planted0;')


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
			gm.play(mes[4:])
		elif mes[:4] == 'stop':
			gm.stop(mes[4:])
		elif mes[:5] == 'pause':
			gm.pause(mes[5:])
		elif mes[:6] == 'volume':
			gm.change_volume(int(mes[6:]))

	def send_inputs(self):
		inputs = PiHandler.get_inputs()
		if inputs['game_button']:
			self.send_message('game_button1;')
		else:
			self.send_message('game_button0;')
		if inputs['start_stage']:
			self.send_message('start_stage1;')
		else:
			self.send_message('start_stage0;')
		if inputs['stop_stage']:
			self.send_message('stop_stage1;')
		else:
			self.send_message('stop_stage0;')
		if inputs['sound_button']:
			self.send_message('sound_button1;')
		else:
			self.send_message('sound_button0;')
		if inputs['light_button']:
			self.send_message('light_button1;')
		else:
			self.send_message('light_button0;')
		if inputs['signal_R']:
			self.send_message('signal_R1;')
		else:
			self.send_message('signal_R0;')
		if inputs['signal_G']:
			self.send_message('signal_G1;')
		else:
			self.send_message('signal_G0;')
		if inputs['signal_B']:
			self.send_message('signal_B1;')
		else:
			self.send_message('signal_B0;')
		if inputs['takeFlag_A']:
			self.send_message('takeFlag_A1;')
		else:
			self.send_message('takeFlag_A0;')
		if inputs['takeFlag_B']:
			self.send_message('takeFlag_B1;')
		else:
			self.send_message('takeFlag_B0;')
		if inputs['giveFlag_A']:
			self.send_message('giveFlag_A1;')
		else:
			self.send_message('giveFlag_A0;')
		if inputs['giveFlag_B']:
			self.send_message('giveFlag_B1;')
		else:
			self.send_message('giveFlag_B0;')
		if inputs['bomb_activated']:
			self.send_message('bomb_activated1;')
		else:
			self.send_message('bomb_activated0;')
		if inputs['bomb_planted']:
			self.send_message('bomb_planted1;')
		else:
			self.send_message('bomb_planted0;')


gc = GameClient()
gh = GameHandler()
gm = Music()


def main():
	threading.Thread(target=gc.clientFunction, daemon=True).start()
	gh.sensors_loop()


if __name__ == '__main__':
	main()
