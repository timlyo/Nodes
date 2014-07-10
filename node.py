import random


class Node:
	def __init__(self, coords, value=None, type=None):
		print("node created")
		if value is not None:
			self.value = random.choice((True, False))
		else:
			self.value = value

		if type is not None:
			self.type = type
		else:
			self.type = "default"

		self.connection = [None, None]  # 0 is right 1 is down
		self.coords = coords
		self.changed = True

	def changeType(self):
		if self.isDefault():
			self.becomeInput()
		elif self.isInput():
			self.becomeOutput()
		elif self.isOutput():
			self.becomeDefault()

	def becomeInput(self):
		self.type = "input"

	def becomeDefault(self):
		self.type = "default"

	def becomeOutput(self):
		self.type = "output"

	def isInput(self):
		if self.type == "input":
			return True
		return False

	def isOutput(self):
		if self.type == "output":
			return True
		return False

	def isDefault(self):
		if self.type == "default":
			return True
		return False

	def getValue(self):
		return self.value

	def connect(self, index, node):
		assert 0 <= index <= 1
		self.connection[index] = node

	def disConnect(self, connection):
		self.connection[connection] = None

	#function called by other nodes when they pass data through
	def input(self, value, connection):
		self.changed = True
		if self.isOutput():
			self.value = value
		self.connection[connection].input(value)

	#called when an input node is updated
	#passes value to  connections
	#def passData(self):
