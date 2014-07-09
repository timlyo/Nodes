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

		#initial variable values, only required for some that are created after the element
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

		#node info box stuff(prefix with an n)
		self.elements["nPos"] = Widget("Position: ", self.mainFont, (0, 0))
		self.elements["nValue"] = Widget("Value: ", self.mainFont, (0, 0))

		#output box(prefix with o)
		self.elements["oInput"]  = Widget("    Input: ", self.mainFont, (0, 0), self.variables["input"], True)
		self.elements["oOutput"] = Widget("Output: ", self.mainFont, (0, 0), self.variables["output"], True)

	def createContainers(self):
		self.containers["feedback"] = Container(self.window, [0, 0], [5, 5])
		self.containers["feedback"].addElement(self.elements["scale"])
		self.containers["feedback"].addElement(self.elements["fps"])
		self.containers["feedback"].setPosition("topRight")

		self.containers["nodeBox"] = Container(self.window, [0, 0], [5, 5])
		self.containers["nodeBox"].addElement(self.elements["nPos"])
		self.containers["nodeBox"].addElement(self.elements["nValue"])
		self.containers["nodeBox"].setPosition("right")
		self.containers["nodeBox"].hide()

		self.containers["outputBox"] = Container(self.window, [0, 0], [5, 5])
		self.containers["outputBox"].addElement(self.elements["oInput"])
		self.containers["outputBox"].addElement(self.elements["oOutput"])
		self.containers["outputBox"].setPosition("bottomRight")

	def updateVariable(self, key, value):
		assert isinstance(key, str)
		if key in self.elements:
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
