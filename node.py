class Node:
	def __init__(self):
		print("node created")
		self.type = "default"

	def becomeInput(self):
		self.type = "input"

	def becomeOutput(self):
		self.type = "output"