from reference import Objects


class Node:
	def __init__(self, coords, value=None, nodeType=None):
		if value is not None:
			self.value = [True, True]
		else:
			self.value = [value, value]  # 2nd index only used for a default node

		if nodeType is not None:
			self.type = nodeType
		else:
			self.type = "default"

		self.connections = [None, None]  # 0 is right 1 is down
		self.changed = True  # tracks if the value has changed
		self.coords = coords
		self.brightness = 255

		self.connectionTypes = ["xor", "xor"]

	def update(self):
		if self.brightness > 0:
			self.brightness -= 15
		if self.brightness < 1:
			self.brightness = 0

		self.passData()

	def changeType(self):
		if self.isDefault():
			self.becomeInput()
		elif self.isInput():
			self.becomeOutput()
		elif self.isOutput():
			self.becomeDefault()
		Objects.grid.connectNodes()

	def changeConnection(self, connection, nodeType):
		self.connectionTypes[connection] = nodeType

	def getConnectionType(self, connection):
		assert isinstance(connection, int)
		assert 0 <= connection <= 1
		return self.connectionTypes[connection]

	def changeConnectionType(self, connection, connectionType):
		assert isinstance(connection, int)
		assert 0 <= connection <= 1
		assert isinstance(connectionType, str)
		assert connectionType in self.connectionTypes
		self.connectionTypes[connection] = connectionType

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
		if self.isInput() or self.isOutput():
			return self.value[0]
		else:
			return self.value

	def getConnectionTypes(self):
		return self.connectionTypes

	def changeValue(self, value=None):
		self.changed = True
		if value is not None:
			self.value[0] = value
			self.value[1] = value
		else:
			self.value[0] = not self.value[0]
			self.value[1] = not self.value[1]

	def connect(self, index, node):
		assert 0 <= index <= 1
		self.connections[index] = node

	def disConnect(self, connection):
		self.connections[connection] = None

	#called when a node is updated
	#passes value to connected nodes
	def passData(self):
		if self.changed:
			self.changed = False
			if self.isInput():
				if self.connections[0] is not None:
					self.connections[0].receive(self.value[0], 0)
				if self.connections[1] is not None:
					self.connections[1].receive(self.value[1], 1)
			else:
				if self.connections[0] is not None:
					data = self.processData(self.connectionTypes[0])
					self.connections[0].receive(data, 0)
				if self.connections[1] is not None:
					data = self.processData(self.connectionTypes[1])
					self.connections[1].receive(data, 1)

	#called by other nodes when a node receives input
	def receive(self, data, connection):
		self.brightness = 255
		if self.value[connection] != data:
			self.changed = True
			self.value[connection] = data
			if self.isInput() or self.isOutput():
				self.value[1-connection] = data

	#function called by other nodes on a default or output node
	#collect input, set value
	#process inputs and calculate outputs
	#pass outputs onto other nodes
	def input(self, value, connection):
		assert isinstance(connection, int)
		self.brightness = 255
		if self.isOutput():
			if self.value[0] != value:
				self.value[0] = value
			return
		if self.connections[0] is not None:
			data = self.processData(self.connectionTypes[0])
			self.value[0] = data
			self.connections[0].input(data, connection)
		if self.connections[1] is not None:
			data = self.processData(self.connectionTypes[1])
			self.value[1] = data
			self.connections[1].input(data, connection)

	#carries out the binary operation on the two connections and returns the value
	def processData(self, operation):
		if operation == "xor":
			return self.value[0] != self.value[1]
		elif operation == "and":
			return self.value[0] and self.value[1]
