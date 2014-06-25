import random

class Node:
	def __init__(self):
		print("node created")
		self.type = "default"
		self.value = random.choice((True, False))
		self.connections = []  # 0 is down 1 is right

	def becomeInput(self):
		self.type = "input"

	def becomeDefault(self):
		self.type = "default"

	def becomeOutput(self):
		self.type = "output"

	def becomeInvalid(self):
		self.type = "invalid"

	def isInput(self):
		if self.type == "input":
			return True
		return False

	def isOutput(self):
		if self.type == "output":
			return True
		return False

	def isInvalid(self):
		if self.type == "invalid":
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
		self.connections[index] = node
