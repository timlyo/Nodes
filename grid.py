import node as Node

import pygame
from reference import colour


class Grid:
	def __init__(self, scale, baseGridSize):
		print("Created Grid")
		self.nodes = {}
		self.scale = scale
		self.baseGridSize = baseGridSize
		self.mainFont = pygame.font.Font(None, 24)
		self.activeNode = None

		self.iterator = 100  # used for node connection animations

	# sets the active node variable that is used for the node info box
	def activateNode(self, node):
		#assert isinstance(node, Node)
		self.activeNode = node
		print(node, " is now active")

	def getActiveNode(self):
		return self.activeNode

	def updateScale(self, scale):
		self.scale = scale

	def addNode(self, coords):
		if not self.getNode(coords):
			self.nodes[coords] = Node.Node(coords)
			#self.setAllNodes()
			self.connectNodes()
			self.getValueString("output")
			return True
		return False

	def deleteNode(self, coords):
		if coords in self.nodes:
			del self.nodes[coords]
			#self.setAllNodes()
			self.connectNodes()
			return True
		return False

	def updateNodes(self):
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if node.isInput():
				pass

	#draws all nodes to the surface that is passed to it
	def drawNodes(self, surface, displacement):
		#draw circles
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			nodePosition = self.getNodePosition(nodeIndex, displacement)  # on screen node coordinates

			nodeColour = colour.grey
			if node.isInput():
				nodeColour = colour.blue
			elif self.nodes[nodeIndex].isOutput():
				nodeColour = colour.green

			#circle
			radius = int(20 * self.scale)
			pygame.draw.circle(surface, nodeColour, nodePosition, radius)

		#draw connecting lines
		if self.iterator > 1:
			self.iterator -= 2
		else:
			self.iterator = 100
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			nodePosition = self.getNodePosition(nodeIndex, displacement)  # on screen node coordinates
			#connections
			if node.connection[0] is not None:
				otherNodePosition = self.getNodePosition(node.connection[0].coords, displacement)
				pygame.draw.aaline(surface, colour.blue, nodePosition, otherNodePosition, 2)

				dotPos = [0, 0]
				dotPos[0] = int(otherNodePosition[0] - (otherNodePosition[0] - nodePosition[0]) * (self.iterator / 100))
				dotPos[1] = nodePosition[1]
				surface.set_at(dotPos, colour.white)

			if node.connection[1] is not None:
				otherNodePosition = self.getNodePosition(node.connection[1].coords, displacement)
				pygame.draw.aaline(surface, colour.blue, nodePosition, otherNodePosition, 2)

				dotPos = [0, 0]
				dotPos[0] = nodePosition[0]
				dotPos[1] = int(otherNodePosition[1] - (otherNodePosition[1] - nodePosition[1]) * (self.iterator / 100))
				surface.set_at(dotPos, colour.white)

		#draw value of node
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			nodePos = self.getNodePosition(nodeIndex, displacement)  # on screen node coordinates
			#value
			if node.isOutput() or node.isInput():
				if node.getValue():
					nodeValue = "1"
				else:
					nodeValue = "0"

				nodeText = self.mainFont.render(nodeValue, 1, colour.white)
				surface.blit(nodeText, (nodePos[0] - int(nodeText.get_width() / 2), nodePos[1] - int(nodeText.get_height() / 2)))

	#handles a click within the grid, returns true if a node is added
	def gridClick(self, position, button):  # position includes displacement
		clickCoord = self.getClickCoord(position)
		if button == 1:
			if self.addNode(clickCoord):
				return True
			else:
				return False
		elif button == 3:
			self.deleteNode(clickCoord)

	#calculates the position of a click in grid coordinates
	def getClickCoord(self, position):
		xCord = position[0] // (self.baseGridSize * self.scale)
		yCord = position[1] // (self.baseGridSize * self.scale)
		return xCord, yCord

	#checks every node and changes it's type if needed(depreciated)
	def DsetAllNodes(self):
		right = (1, 0)
		left = (-1, 0)
		above = (0, -1)
		below = (0, 1)
		for node in self.nodes:  # This may be changed later
			self.nodes[node].becomeDefault()
			if not self.isNode(left, node) and not self.isNode(above, node):
				self.getNode(node).becomeInput()
			if not self.isNode(above, node):
				if self.isNode(left, node) and self.getNode(left, node).isInput():
					self.getNode(node).becomeInput()
			if not self.isNode(left, node):
				if self.isNode(above, node) and self.getNode(above, node).isInput():
					self.getNode(node).becomeInput()
			if self.isNode(left, node) and self.getNode(left, node).isDefault():
				if not self.isNode(right, node):
					self.getNode(node).becomeOutput()
			if self.isNode(above, node) and self.getNode(above, node).isDefault():
				if not self.getNode(below, node):
					self.getNode(node).becomeOutput()

	#connects each node to the one below and to the right of it
	def connectNodes(self):
		right = (1, 0)
		below = (0, 1)
		for node in self.nodes:
			if self.isNode(below, node):
				if self.getNode(below, node).isDefault():
					self.getNode(node).connect(1, self.getNode(below, node))
				if self.getNode(node).isDefault() and self.getNode(below, node).isOutput():
					self.getNode(node).connect(1, self.getNode(below, node))
			if self.isNode(right, node):
				if self.getNode(right, node).isDefault():
					self.getNode(node).connect(0, self.getNode(right, node))
		self.pruneConnections()

	#removes unneeded connections from grid
	def pruneConnections(self):
		right = (1, 0)
		below = (0, 1)

		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if not self.isNode(right, nodeIndex):
				node.disConnect(0)
			if not self.isNode(below, nodeIndex):
				node.disConnect(1)

			if node.isInput():
				if node.connection[0] is not None:
					if node.connection[0].isInput():
						node.disConnect(0)
				if node.connection[1] is not None:
					if node.connection[1].isInput():
						node.disConnect(1)
			if node.isOutput():
				if node.connection[0] is not None:
					if node.connection[0].isOutput():
						node.disConnect(0)
				if node.connection[1] is not None:
					if node.connection[1].isOutput():
						node.disConnect(1)

	#check if node is at coords
	#if a node is passed then the coords are relative to that
	def isNode(self, coords, node=None):
		if node is not None:
			pos = (coords[0] + node[0], coords[1] + node[1])
		else:
			pos = coords
		if pos in self.nodes:
			return True
		return False

	#checks if a node exists and then returns it
	def getNode(self, coords, node=None):
		if node is not None:
			pos = (coords[0] + node[0], coords[1] + node[1])
		else:
			pos = coords
		if self.isNode(pos):
			return self.nodes[pos]
		return None

	# work out the on screen coordinates of a node from it's grid coordinates
	def getNodePosition(self, coords, displacement):
		xCord = int((coords[0] * 50 + 25) * self.scale) + displacement[0]
		yCord = int((coords[1] * 50 + 25) * self.scale) + displacement[1]
		return (xCord, yCord)

	def getNodes(self, type="default"):
		nodeList = []
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if type is "input":
				if node.isInput():
					nodeList.append(nodeIndex)
			elif type is "output":
				if node.isOutput():
					nodeList.append(nodeIndex)
			else:
				nodeList.append(nodeIndex)

		nodeList.sort()
		print(type, " nodes = ", nodeList)
		return nodeList

	def getValueString(self, type):
		assert isinstance(type, str)
		nodeList = self.getNodes(type)
		value = ""

		if len(nodeList) is 0:
			return value

		for nodeIndex in nodeList:
			node = self.getNode(nodeIndex)
			if node.getValue() is True:
				value += "1"
			else:
				value += "0"

		print(type, "String:", value)
		return value

	def changeNodeType(self, node):
		node.changeType()
		self.connectNodes()
