import RPi.GPIO as GPIO
import time

class PiHandler():
	def __init__(self):
		self.initGPIO()
		self.inputs = {
			'game_button': GPIO.input(7),
			'bomb_planted': GPIO.input(8),
			'bomb_activated': GPIO.input(10),
			'start_stage': GPIO.input(11),
			'stop_stage': GPIO.input(13),
			'sound_button': GPIO.input(15),
			'light_button': GPIO.input(19),
			'signal_R': GPIO.input(21),
			'signal_G': GPIO.input(23),
			'signal_B': GPIO.input(29),
			'takeFlag_A': GPIO.input(31),
			'takeFlag_B': GPIO.input(33),
			'giveFlag_A': GPIO.input(35),
			'giveFlag_B': GPIO.input(37)

		}

	@staticmethod
	def get_inputs():
		inputs = {
			'game_button': GPIO.input(7),
			'bomb_planted': GPIO.input(8),
			'bomb_activated': GPIO.input(10),
			'start_stage': GPIO.input(11),
			'stop_stage': GPIO.input(13),
			'sound_button': GPIO.input(15),
			'light_button': GPIO.input(19),
			'signal_R': GPIO.input(21),
			'signal_G': GPIO.input(23),
			'signal_B': GPIO.input(29),
			'takeFlag_A': GPIO.input(31),
			'takeFlag_B': GPIO.input(33),
			'giveFlag_A': GPIO.input(35),
			'giveFlag_B': GPIO.input(37)
		}
		return inputs

	def sensors_loop(self):
		while True:
			try:
				if GPIO.input(7) != self.inputs['game_button']:
					self.inputs['game_button'] = GPIO.input(7)
					if self.inputs['game_button']:
						self.game_button1()
					else:
						self.game_button0()

				if GPIO.input(8) != self.inputs['bomb_planted']:
					self.inputs['bomb_planted'] = GPIO.input(8)
					if self.inputs['bomb_planted']:
						self.bomb_planted1()
					else:
						self.bomb_planted0()

				if GPIO.input(10) != self.inputs['bomb_activated']:
					self.inputs['bomb_activated'] = GPIO.input(10)
					if self.inputs['bomb_activated']:
						self.bomb_activated1()
					else:
						self.bomb_activated0()

				if GPIO.input(11) != self.inputs['start_stage']:
					self.inputs['start_stage'] = GPIO.input(11)
					if self.inputs['start_stage']:
						self.start_stage1()
					else:
						self.start_stage0()

				if GPIO.input(13) != self.inputs['stop_stage']:
					self.inputs['stop_stage'] = GPIO.input(13)
					if self.inputs['stop_stage']:
						self.stop_stage1()
					else:
						self.stop_stage0()

				if GPIO.input(15) != self.inputs['sound_button']:
					self.inputs['sound_button'] = GPIO.input(15)
					if self.inputs['sound_button']:
						self.sound_button1()
					else:
						self.sound_button0()

				if GPIO.input(19) != self.inputs['light_button']:
					self.inputs['light_button'] = GPIO.input(19)
					if self.inputs['light_button']:
						self.light_button1()
					else:
						self.light_button0()

				if GPIO.input(21) != self.inputs['signal_R']:
					self.inputs['signal_R'] = GPIO.input(21)
					if self.inputs['signal_R']:
						self.signal_R1()
					else:
						self.signal_R0()

				if GPIO.input(23) != self.inputs['signal_G']:
					self.inputs['signal_G'] = GPIO.input(23)
					if self.inputs['signal_G']:
						self.signal_G1()
					else:
						self.signal_G0()

				if GPIO.input(29) != self.inputs['signal_B']:
					self.inputs['signal_B'] = GPIO.input(29)
					if self.inputs['signal_B']:
						self.signal_B1()
					else:
						self.signal_B0()

				if GPIO.input(31) != self.inputs['takeFlag_A']:
					self.inputs['takeFlag_A'] = GPIO.input(31)
					if self.inputs['takeFlag_A']:
						self.takeFlag_A1()
					else:
						self.takeFlag_A0()

				if GPIO.input(33) != self.inputs['takeFlag_B']:
					self.inputs['takeFlag_B'] = GPIO.input(33)
					if self.inputs['takeFlag_B']:
						self.takeFlag_B1()
					else:
						self.takeFlag_B0()

				if GPIO.input(35) != self.inputs['giveFlag_A']:
					self.inputs['giveFlag_A'] = GPIO.input(35)
					if self.inputs['giveFlag_A']:
						self.giveFlag_A1()
					else:
						self.giveFlag_A0()

				if GPIO.input(37) != self.inputs['giveFlag_B']:
					self.inputs['giveFlag_B'] = GPIO.input(37)
					if self.inputs['giveFlag_B']:
						self.giveFlag_B1()
					else:
						self.giveFlag_B0()

				time.sleep(0.1)
			except:
				pass

	def initGPIO(self):
		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(29, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(31, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(33, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(35, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(37, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

		GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)


	def tableButton1(self):
		GPIO.output(12, GPIO.HIGH)
	def tableButton0(self):
		GPIO.output(12, GPIO.LOW)
	def ARed1(self):
		GPIO.output(16, GPIO.HIGH)
	def ARed0(self):
		GPIO.output(16, GPIO.LOW)
	def ABlue1(self):
		GPIO.output(18, GPIO.HIGH)
	def ABlue0(self):
		GPIO.output(18, GPIO.LOW)
	def BRed1(self):
		GPIO.output(22, GPIO.HIGH)
	def BRed0(self):
		GPIO.output(22, GPIO.LOW)
	def BBlue1(self):
		GPIO.output(24, GPIO.HIGH)
	def BBlue0(self):
		GPIO.output(24, GPIO.LOW)
	def AdminLight1(self):
		GPIO.output(26, GPIO.HIGH)
	def AdminLight0(self):
		GPIO.output(26, GPIO.LOW)


	def game_button1(self):
		pass
	def game_button0(self):
		pass
	def start_stage1(self):
		pass
	def start_stage0(self):
		pass
	def stop_stage1(self):
		pass
	def stop_stage0(self):
		pass
	def sound_button1(self):
		pass
	def sound_button0(self):
		pass
	def light_button1(self):
		pass
	def light_button0(self):
		pass
	def signal_R1(self):
		pass
	def signal_R0(self):
		pass
	def signal_G1(self):
		pass
	def signal_G0(self):
		pass
	def signal_B1(self):
		pass
	def signal_B0(self):
		pass
	def takeFlag_A1(self):
		pass
	def takeFlag_A0(self):
		pass
	def takeFlag_B1(self):
		pass
	def takeFlag_B0(self):
		pass
	def giveFlag_A1(self):
		pass
	def giveFlag_A0(self):
		pass
	def giveFlag_B1(self):
		pass
	def giveFlag_B0(self):
		pass
	def bomb_activated1(self):
		pass
	def bomb_activated0(self):
		pass
	def bomb_planted1(self):
		pass
	def bomb_planted0(self):
		pass
