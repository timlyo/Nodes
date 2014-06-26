import pygame

class Gui:
	def __init__(self, variables, window):
		self.mainFont = pygame.font.Font(None, 24)
		self.elements = {}
		self.containers = {}
		self.variables = variables
		self.window = window

		#initial variable values
		self.variables["scale"] = 1.0

		self.createElements()
		print ("Created gui")

	def drawAll(self, surface):
		for widget in self.elements:
			item = self.elements[widget]
			surface.blit(item.surface, item.coords)

	def createElements(self):
		self.elements["fps"] = Widget("fps: ", self.mainFont, (0, 0), self.variables["clock"].get_fps(), True)
		self.elements["scale"] = Widget("scale: ", self.mainFont, (0, self.elements["fps"].height), self.variables["scale"], True)
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
			self.containers[item].updateWidth()
			self.containers[item].updateHeight()
			self.containers[item].updatePosition()
			self.containers[item].positionElements()

#holds references to elements and adjust their position to fit into a container
class Container:
	def __init__(self, window, coords=[0, 0], spacing=[0, 5], width=0, height=0):
		self.elements = []
		self.window = window
		self.position = "left"
		self.coords = coords
		self.spacing = spacing
		self.width = width
		self.height = height

	def addElement(self, element):
		self.elements.append(element)

	def setPosition(self, position):
		self.position = position

	def updatePosition(self):
		if self.position == "left":
			self.coords[0] = 0
		elif self.position == "top":
			self.coords[1] = 0
		elif self.position == "right":
			self.coords[0] = self.window.get_width() - self.width
		elif not isinstance(position, str):
			print("Position of type ", type(position), " not recognised")
			return

	#sets the container width to the width of the widest element
	def updateWidth(self):
		width = 0
		for item in self.elements:
			if item.getWidth() > width:
				width = item.getWidth()
		self.width = width

	#sets the container height to the total height of all elements
	def updateHeight(self):
		height = 0
		for item in self.elements:
			height += item.getHeight()
		self.height = height

	#position the container's elements
	def positionElements(self):
		for index in range(len(self.elements)):
			element = self.elements[index]
			spacing = self.spacing
			if self.position is "left":
				spacing[0] = self.spacing[0]
			elif self.position is "right":
				spacing[0] = - abs(self.spacing[0])
			if index is 1:
				element.setCoords((self.coords[0] + spacing[0], self.coords[1] + spacing[1]))
			else:
				previousElement = self.elements[index - 1]
				newYPos = previousElement.getYCoords() + previousElement.getHeight() + spacing[1]
				self.elements[index].setCoords((self.coords[0] + spacing[0], newYPos))


class Widget:
	def __init__(self, text, font, coords, variable="", changes=False):
		self.text = text
		self.font = font
		self.coords = coords
		self.variable = variable
		self.changes = changes
		self.height = 0
		self.width = 0
		
		self.render()

	def render(self):
		self.finalText = self.text + str(round(self.variable, 2))
		self.surface = self.font.render(self.finalText, 1, (255, 255, 255))
		self.height = self.surface.get_height()

	def getHeight(self):
		self.height = self.surface.get_height()
		return self.height

	def getWidth(self):
		self.width = self.surface.get_width()
		return self.width

	def setCoords(self, coords):
		self.coords = coords

	def getYCoords(self):
		return self.coords[1]
