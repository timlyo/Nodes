import node as Node

import pygame

class Grid:
	def __init__(self, scale, baseGridSize):
		print("Created Grid")
		self.nodes = {}
		self.scale = scale
		self.baseGridSize = baseGridSize

		self.colour = (150, 150, 150)

	def updateScale(self, scale):
		self.scale = scale

	def addNode(self, coords):
		self.nodes[coords] = Node.Node()
		self.setAllNodes()

	def deleteNode(self, coords):
		if coords in self.nodes:
			del self.nodes[coords]

	#prints all nodes to console on their own line
	def printNodes(self):
		print("Nodes:")
		for item in self.nodes:
			print(" ", item)

	#draws all nodes to the surface that is passed to it
	def drawNodes(self, surface, displacement):
		for item in self.nodes:
			xCord = int((item[0]*50+25)*self.scale) + displacement[0]
			yCord = int((item[1]*50+25)*self.scale) + displacement[1]
			pygame.draw.circle(surface, self.colour, (xCord, yCord), int(20*self.scale))

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
		print("Clicked at ", (xCord, yCord))
		return(xCord, yCord)

	#checks every node and changes it's type if needed
	def setAllNodes(self):
		for node in self.nodes:
			print(node)