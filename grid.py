from save import File
import node as Node

import pygame
from pygame.locals import *
import random

from reference import Colour
from reference import Objects

from util import Util


class Grid:
	def __init__(self, scale, baseGridSize, window):
		print("Created Grid")
		Objects.grid = self
		self.nodes = {}
		File.loadFile()
		self.scale = scale
		self.baseGridSize = baseGridSize
		self.mainFont = pygame.font.Font(None, 24)
		self.activeNode = None

		self.window = window

		self.iterator = 100  # used for node connection animations

	def getNodeList(self):
		return self.nodes

	# sets the active node variable that is used for the node info box
	def activateNode(self, node):
		if self.activeNode is not node:
			if self.activeNode is not None:
				self.activeNode.active = False
			self.activeNode = node
			node.active = True
			self.window.showGuiContainer("nodeBox")
			return True
		return False

	def getActiveNode(self):
		return self.activeNode

	def changeActiveNode(self, node):
		print(node.coords, "is now active")
		self.activeNode.active = False
		self.activeNode = node
		self.activeNode.active = True

	def moveActiveNode(self, direction, create=False):
		left = (-1, 0)
		right = (1, 0)
		above = (0, -1)
		below = (0, 1)
		activeNode = self.activeNode
		coords = (0, 0)
		newNode = None
		if direction == K_UP:
			coords = Util.addLists(activeNode.coords, above)
			newNode = self.getNode(coords)
		elif direction == K_DOWN:
			coords = Util.addLists(activeNode.coords, below)
			newNode = self.getNode(coords)
		elif direction == K_LEFT:
			coords = Util.addLists(activeNode.coords, left)
			newNode = self.getNode(coords)
		elif direction == K_RIGHT:
			coords = Util.addLists(activeNode.coords, right)
			newNode = self.getNode(coords)

		if newNode is None:
			if create is True:
				self.addNode(coords)
				newNode = self.getNode(coords)
			else:
				return
		self.changeActiveNode(newNode)

	def updateScale(self, scale):
		self.scale = scale

	def addNode(self, coords, value=None, type=None):
		if not self.getNode(coords):
			self.nodes[coords] = Node.Node(coords, value, type)
			self.updateNodes()
			return True
		return False

	def deleteNode(self, coords):
		if coords in self.nodes:
			del self.nodes[coords]
			self.updateNodes()
			return True
		return False

	def updateNodes(self):
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if node.isInput():
				pass
			node.update()
		self.connectNodes()

	#draws all nodes to the surface that is passed to it
	def drawNodes(self, surface, displacement):
		#draw circles
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			nodePosition = self.getNodePosition(nodeIndex, displacement)  # on screen node coordinates

			nodeColour = Colour.grey
			if node.isInput():
				nodeColour = Colour.blue
			elif self.nodes[nodeIndex].isOutput():
				nodeColour = Colour.green

			#=outline circles
			radius = int(20 * self.scale)
			#change circle
			ringColour = (node.brightness, node.brightness, node.brightness, node.brightness)
			pygame.draw.circle(surface, ringColour, nodePosition, radius)
			#active circle
			if node.isActive():
				ringColour = Colour.yellow
				pygame.draw.circle(surface, ringColour, nodePosition, radius-1)
			pygame.draw.circle(surface, nodeColour, nodePosition, radius-2)

		#draw connecting lines
		if self.iterator > 1:
			self.iterator -= 2
		else:
			self.iterator = 100
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			nodePosition = self.getNodePosition(nodeIndex, displacement)  # on screen node coordinates
			#connections
			if node.connections[0][0] is not None:
				otherNodePosition = self.getNodePosition(node.connections[0][0].coords, displacement)
				pygame.draw.aaline(surface, Colour.blue, nodePosition, otherNodePosition, 2)

				dotPos = [0, 0]
				dotPos[0] = int(otherNodePosition[0] - (otherNodePosition[0] - nodePosition[0]) * (self.iterator / 100))
				dotPos[1] = nodePosition[1]
				surface.set_at(dotPos, Colour.white)

			if node.connections[1][0] is not None:
				otherNodePosition = self.getNodePosition(node.connections[1][0].coords, displacement)
				pygame.draw.aaline(surface, Colour.blue, nodePosition, otherNodePosition, 2)

				dotPos = [0, 0]
				dotPos[0] = nodePosition[0]
				dotPos[1] = int(otherNodePosition[1] - (otherNodePosition[1] - nodePosition[1]) * (self.iterator / 100))
				surface.set_at(dotPos, Colour.white)

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

				nodeText = self.mainFont.render(nodeValue, 1, Colour.white)
				surface.blit(nodeText, (nodePos[0] - int(nodeText.get_width() / 2), nodePos[1] - int(nodeText.get_height() / 2)))

	#handles a click within the grid, returns true if a node is added
	def gridClick(self, position, button):  # position includes displacement
		clickCoord = self.getGridCoord(position)
		if button == 1:
			if self.addNode(clickCoord):
				return True
			else:
				return False
		elif button == 3:
			self.deleteNode(clickCoord)

	def getGridCoord(self, position):
		"""calculates the position of a click in grid coordinates
		:param position: on screen position of click
		:return: grid position of click
		"""
		xCord = position[0] // (self.baseGridSize * self.scale)
		yCord = position[1] // (self.baseGridSize * self.scale)
		return xCord, yCord

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
				if self.getNode(node).isDefault and self.getNode(right, node).isOutput():
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
				if node.connections[0][0] is not None:
					if node.connections[0][0].isInput():
						node.disConnect(0)
				if node.connections[1][0] is not None:
					if node.connections[1][0].isInput():
						node.disConnect(1)
			if node.isOutput():
				if node.connections[0][0] is not None:
					if node.connections[0][0].isOutput():
						node.disConnect(0)
				if node.connections[1][0] is not None:
					if node.connections[1][0].isOutput():
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

	def getNodePosition(self, coords, displacement):
		"""
		Calculate the on screen position of a node from it's grid coordinates
		:param coords: coordinates of the node
		:param displacement: current displacement of the grid
		:return: tuple of the x and y position of the node
		"""
		xPos = int((coords[0] * 50 + 25) * self.scale) + displacement[0]
		yPos = int((coords[1] * 50 + 25) * self.scale) + displacement[1]
		return xPos, yPos

	def getNodes(self, type=None):
		"""
		Returns a sorted list of all the nodes
		:param type: determines the type of nodes to return, default=all nodes
		:return: sorted node list
		"""
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
		return nodeList

	def getValueString(self, type):
		"""
		Gets a string of all the input or output nodes within the grid
		:param type: input or output nodes
		:return: string for the value of the nodes
		"""
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

		return value

	def changeNodeType(self, node):
		node.changeType()
		self.connectNodes()

	def clear(self):
		self.nodes = {}
		Objects.window.updateGrid()

	def randomiseInput(self):
		"""
		Give all the input nodes random states and the default nodes
		"""
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if node.isInput():
				node.changeValue(random.choice([True, False]))

	def randomiseNodes(self):
		"""
		Give all the node's connections random states
		:return:
		"""
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if node.isDefault():
				node.changeConnectionType(0, random.choice(node.connectionTypes))
				node.changeConnectionType(1, random.choice(node.connectionTypes))

	def isDone(self):
		"""
		Checks if every node has passed it's data
		:return:
		"""
		for nodeIndex in self.nodes:
			node = self.getNode(nodeIndex)
			if node.changed is True:
				return False
