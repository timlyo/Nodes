import node as Node

import pygame

class Grid:
	def __init__(self, scale, baseGridSize):
		print("Created Grid")
		self.nodes = {}
		self.scale = scale
		self.baseGridSize = baseGridSize


	def updateScale(self, scale):
		self.scale = scale

	def addNode(self, coords):
		self.nodes[coords] = Node.Node()
		self.setAllNodes()

	def deleteNode(self, coords):
		if coords in self.nodes:
			del self.nodes[coords]
			self.setAllNodes()

	#prints all nodes to console on their own line
	def printNodes(self):
		print("Nodes:")
		for item in self.nodes:
			print(" ", item)

	#draws all nodes to the surface that is passed to it
	def drawNodes(self, surface, displacement):
		for node in self.nodes:
			colour = (150, 150, 150)
			if self.nodes[node].isInput():
				colour = (50, 50, 255)
			elif self.nodes[node].isOutput():
				colour = (50, 255, 50)
			elif self.nodes[node].isInvalid():
				colour = (255, 50, 50)

			xCord = int((node[0]*50+25)*self.scale) + displacement[0]
			yCord = int((node[1]*50+25)*self.scale) + displacement[1]
			radius = int(20*self.scale)
			pygame.draw.circle(surface, colour, (xCord, yCord), radius)

			if self.nodes[node].isOutput() or self.nodes[node].isInput():
				if self.nodes[node].getValue():
					nodeValue = "1"
				else:
					nodeValue = "0"

				self.mainFont = pygame.font.Font(None, 24)

				nodeText = self.mainFont.render(nodeValue, 1, (255, 255, 255))
				surface.blit(nodeText, (xCord - int(nodeText.get_width()/2), yCord - int(nodeText.get_height()/2)))

	def gridClick(self, position, button):  # position includes displacement
		clickCoord = self.getClickCoord(position)
		if button == 1:
			self.addNode(clickCoord)
		elif button == 3:
			self.deleteNode(clickCoord)

	#calculates the position of a click in grid coordinates
	def getClickCoord(self,position):
		xCord = position[0] // self.baseGridSize
		yCord = position[1] // self.baseGridSize
		return(xCord, yCord)

	#checks every node and changes it's type if needed
	def setAllNodes(self):
		right = (1, 0)
		left = (-1, 0)
		above = (0, -1)
		below = (0, 1)
		for node in self.nodes:
			self.nodes[node].becomeDefault()
			if not self.isNode(left, node) or not self.isNode(above, node):
				if self.isNode(below, node) or self.isNode(right, node):
					self.getNode(node).becomeInput()


	#connects each node to the one below and to the right of it
	#WIP
	def connectNodes(self):
		for node in self.nodes:
			if (node[0] - 1, node[1]) in self.nodes:  # node left
				self.nodes[node].connect()
			elif (node[0], node[1] - 1) not in self.nodes:  # node above
				self.nodes[node].becomeInput()
			elif (node[0] + 1, node[1]) not in self.nodes:  # node below
				self.nodes[node].becomeOutput()
			elif (node[0], node[1] + 1) not in self.nodes:  # node right
				self.nodes[node].becomeOutput()
			else:
				self.nodes[node].becomeDefault()

	#check if node is at coords
	#if a node is passed then the coords are relative to that
	def isNode(self, coords, node=None):
		if node != None:
			pos = (coords[0] + node[0], coords[1] + node[1])
		else:
			pos = coords
		if pos in self.nodes:
			return True
		return False

	#checks if a node exists and then returns it
	def getNode(self, coords, node=None):
		if node != None:
			pos = (coords[0] + node[0], coords[1] + node[1])
		else:
			pos = coords
		if self.isNode(pos, node):
			return self.nodes[pos]
		return None
