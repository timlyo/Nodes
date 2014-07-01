import pygame

from widget import Widget
from container import Container

class Gui:
	def __init__(self, variables, window):
		self.mainFont = pygame.font.Font(None, 24)
		self.elements = {}
		self.containers = {}
		self.variables = variables
		self.window = window
		self.grid = self.window.getGrid()

		#initial variable values
		self.variables["scale"] = 1.0

		self.createElements()
		self.createContainers()
		print("Created gui")

	def drawAll(self, surface):
		for widget in self.elements:
			item = self.elements[widget]
			surface.blit(item.surface, item.coords)

	def createElements(self):
		self.elements["fps"] = Widget("fps: ", self.mainFont, (0, 0), self.variables["clock"].get_fps(), True)
		self.elements["scale"] = Widget("scale: ", self.mainFont, (0, self.elements["fps"].height), self.variables["scale"], True)

		#info box stuff


	def createContainers(self):
		self.containers["infoBox"] = Container(self.window, [0, 0], [5, 5])
		self.containers["infoBox"].addElement(self.elements["scale"])
		self.containers["infoBox"].addElement(self.elements["fps"])
		self.containers["infoBox"].setPosition("right")


	def updateVariable(self, key, value):
		self.elements[key].variable = value

	def updateElements(self):
		for item in self.elements:
			if self.elements[item].changes:
				self.elements[item].render()
		for item in self.containers:
			self.containers[item].move()
			self.containers[item].updateWidth()
			self.containers[item].updateHeight()
			self.containers[item].updatePosition()
			self.containers[item].positionElements()
