import RPi.GPIO as GPIO
import time

class PiHandler():
	def __init__(self):
		self.initGPIO()
		self.inputs = {}
		self.outs = {
			'r2o7': 7,
			'r2o8': 11,
			'r2o9': 13,
			'r2o10': 15,
			'r2o11': 19,
			'r2o12': 21,
			'r2o13': 23,
			'r2o14': 29,
			'r2o15': 31,
			'r2o16': 33,
			'r2o17': 35,
			'r2o18': 37,
			'r2o19': 8,
			'r2o20': 10,
			'r2o21': 12,
		}

	@staticmethod
	def get_inputs():
		inputs = {}
		return inputs

	def sensors_loop(self):
		while True:
			try:
				time.sleep(0.1)
			except:
				pass

	def initGPIO(self):
		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(29, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(33, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(37, GPIO.OUT, initial=GPIO.HIGH)

	def reset_out(self, out, status):
		if status:
			GPIO.output(self.outs[out], GPIO.HIGH)
		else:
			GPIO.output(self.outs[out], GPIO.LOW)
