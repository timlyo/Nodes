import node as Node

import pygame

class Grid:
	def __init__(self, scale, baseGridSize):
		print("Created Grid")
		self.nodes = {}
		self.scale = scale
		self.baseGridSize = baseGridSize

		self.addNode((0,0))
		self.addNode((0,1))
		self.addNode((1,0))
		self.addNode((1,1))
		self.addNode((5,13))


		self.printNodes()

		self.colour = (150,150,150)

	def updateScale(self, scale):
		self.scale = scale

	def addNode(self,coords):
		self.nodes[coords] = Node.Node()

	def printNodes(self):
		print("Nodes:")
		for item in self.nodes:
			print(" ", item)

	def drawNodes(self, surface, displacement):
		for item in self.nodes:
			xCord = int((item[0]*50+25)*self.scale) + displacement[0]
			yCord = int((item[1]*50+25)*self.scale) + displacement[1]
			pygame.draw.circle(surface, self.colour, (xCord, yCord), int(20*self.scale))
