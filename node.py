import random


class Node:
	def __init__(self, coords, value=None, nodeType=None):
		if value is not None:
			self.value = random.choice((True, False))
		else:
			self.value = value

		if nodeType is not None:
			self.type = nodeType
		else:
			self.type = "default"

		self.connection = [None, None]  # 0 is right 1 is down
		self.changed = True  # tracks if the value has changed
		self.connectionType = ["xor", "xor"]
		self.coords = coords
		self.brightness = 255

	def update(self):
		if self.brightness > 0:
			self.brightness -= 15
		if self.brightness < 1:
			self.brightness = 0

		if self.isInput() and self.changed:
			if self.connection[0] is not None:
				self.passData(0)
			elif self.connection[1] is not None:
				self.passData(1)

	def changeType(self):
		if self.isDefault():
			self.becomeInput()
		elif self.isInput():
			self.becomeOutput()
		elif self.isOutput():
			self.becomeDefault()

	def changeConnection(self, connection, nodeType):
		self.connectionType[connection] = nodeType

	def getConnectionType(self, connection):
		assert isinstance(connection, int)
		assert 0 <= connection <= 1
		return self.connectionType[connection]

	def changeValue(self, value=None):
		self.changed = True
		if value is not None:
			self.value = value
		else:
			self.value = not self.value

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
		self.brightness = 255
		if self.isOutput():
			self.value = value
		if self.connection[connection] is not None:
			self.connection[connection].input(value, connection)

	#called when an input node is updated
	#passes value to  connections
	def passData(self, connection):
		assert isinstance(connection, int)
		assert 0 <= connection <= 1
		self.connection[connection].input(self.value, connection)
		self.changed = False
