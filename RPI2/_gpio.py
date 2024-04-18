import RPi.GPIO as GPIO
import time

class PiHandler():
	def __init__(self):
		self.initGPIO()
		self.inputs = {}

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


	def area1_W11(self):
		GPIO.output(7, GPIO.HIGH)
	def area1_W10(self):
		GPIO.output(7, GPIO.LOW)
	def area1_TL11(self):
		GPIO.output(11, GPIO.HIGH)
	def area1_TL10(self):
		GPIO.output(11, GPIO.LOW)
	def area2_W21(self):
		GPIO.output(13, GPIO.HIGH)
	def area2_W20(self):
		GPIO.output(13, GPIO.LOW)
	def area2_TL21(self):
		GPIO.output(15, GPIO.HIGH)
	def area2_TL20(self):
		GPIO.output(15, GPIO.LOW)
	def area3_W31(self):
		GPIO.output(19, GPIO.HIGH)
	def area3_W30(self):
		GPIO.output(19, GPIO.LOW)
	def area3_TL31(self):
		GPIO.output(21, GPIO.HIGH)
	def area3_TL30(self):
		GPIO.output(21, GPIO.LOW)
	def area4_W41(self):
		GPIO.output(23, GPIO.HIGH)
	def area4_W40(self):
		GPIO.output(23, GPIO.LOW)
	def area4_TL41(self):
		GPIO.output(29, GPIO.HIGH)
	def area4_TL40(self):
		GPIO.output(29, GPIO.LOW)
	def hallway1_WK11(self):
		GPIO.output(31, GPIO.HIGH)
	def hallway1_WK10(self):
		GPIO.output(31, GPIO.LOW)
	def hallway1_TLK11(self):
		GPIO.output(33, GPIO.HIGH)
	def hallway1_TLK10(self):
		GPIO.output(33, GPIO.LOW)
	def hallway2_WK21(self):
		GPIO.output(35, GPIO.HIGH)
	def hallway2_WK20(self):
		GPIO.output(35, GPIO.LOW)
	def hallway2_TLK21(self):
		GPIO.output(37, GPIO.HIGH)
	def hallway2_TLK20(self):
		GPIO.output(37, GPIO.LOW)
	def give_LK11(self):
		GPIO.output(8, GPIO.HIGH)
	def give_LK10(self):
		GPIO.output(8, GPIO.LOW)
	def medicBag_A1(self):
		GPIO.output(10, GPIO.HIGH)
	def medicBag_A0(self):
		GPIO.output(10, GPIO.LOW)
	def medicBag_B1(self):
		GPIO.output(12, GPIO.HIGH)
	def medicBag_B0(self):
		GPIO.output(12, GPIO.LOW)
