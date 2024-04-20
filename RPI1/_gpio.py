import RPi.GPIO as GPIO
import time

class PiHandler():
	def __init__(self):
		self.initGPIO()
		self.inputs = {
			'r1i1': [GPIO.input(7), 7],
			'r1i2': [GPIO.input(8), 8],
			'r1i3': [GPIO.input(10), 10],
			'r1i4': [GPIO.input(11), 11],
			'r1i5': [GPIO.input(13), 13],
			'r1i6': [GPIO.input(15), 15],
			'r1i7': [GPIO.input(19), 19],
			'r1i8': [GPIO.input(21), 21],
			'r1i9': [GPIO.input(23), 23],
			'r1i10': [GPIO.input(29), 29],
			'r1i11': [GPIO.input(31), 31],
			'r1i12': [GPIO.input(33), 33],
			'r1i13': [GPIO.input(35), 35],
			'r1i14': [GPIO.input(37), 37]
		}
		self.outs = {
			'r1o1': 12,
			'r1o2': 16,
			'r1o3': 18,
			'r1o4': 22,
			'r1o5': 24,
			'r1o6': 26,
		}

	@staticmethod
	def get_inputs():
		inputs = {
			'r1i1': GPIO.input(7),
			'r1i2': GPIO.input(8),
			'r1i3': GPIO.input(10),
			'r1i4': GPIO.input(11),
			'r1i5': GPIO.input(13),
			'r1i6': GPIO.input(15),
			'r1i7': GPIO.input(19),
			'r1i8': GPIO.input(21),
			'r1i9': GPIO.input(23),
			'r1i10': GPIO.input(29),
			'r1i11': GPIO.input(31),
			'r1i12': GPIO.input(33),
			'r1i13': GPIO.input(35),
			'r1i14': GPIO.input(37)
		}
		return inputs

	def sensors_loop(self):
		while True:
			try:
				for input in self.inputs:
					status = GPIO.input(self.inputs[input][1])
					if self.inputs[input][0] != status:
						self.inputs[input][0] = status
						self.reset_input(input, int(status))
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

	def reset_out(self, out, status):
		if status:
			GPIO.output(self.outs[out], GPIO.HIGH)
		else:
			GPIO.output(self.outs[out], GPIO.LOW)

	def reset_input(self, input, status):
		pass
