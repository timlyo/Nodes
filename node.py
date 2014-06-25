class Node:
	def __init__(self):
		print("node created")
		self.type = "default"
		self.value = False

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

	def getValue(self):
		return self.value