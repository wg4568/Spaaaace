from helpers import translate
import sys

class PercentOutput:
	def __init__(self, minval=0, maxval=100, width=100):
		self.minval = minval
		self.maxval = maxval
		self.position = 0
		self.width = width
		self.val = self.minval

	def set(self, val):
		new = int(translate(val, self.minval, self.maxval, 0, 100))
		if not new == self.val:
			sys.stdout.write("\r" + str(new) + "% done")
			sys.stdout.flush()
		if new == 100:
			print "\n"

class LoadingBar:
	def __init__(self, minval=0, maxval=100, width=100):
		self.minval = minval
		self.maxval = maxval
		self.position = 0
		self.width = width
		self.val = self.minval

	def increase(self):
		self.val += 1
		loaded = ((self.val-1) * "=") + ">"
		notloaded = (self.width - self.val) * " "
		self.string = "[" + loaded + notloaded + "]"

	def set(self, val):
		new = int(translate(val, self.minval, self.maxval, 0, 100))
		if not new == self.val:
			self.increase()
			sys.stdout.write("\r" + self.string)
			sys.stdout.flush()
		if new == 100:
			print "\n"
