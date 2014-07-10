import pygame

class Widget:
	def __init__(self, text, font, coords, variable="", changes=False):
		self.text = text
		self.finalText = ""
		self.font = font
		self.coords = coords
		self.variable = variable
		self.changes = changes
		self.height = 0
		self.width = 0
		self.surface = pygame.Surface((0, 0))

		self.isShown = True

		self.render()

	def render(self):
		if self.isShown:
			if self.variable is not "":
				if isinstance(self.variable, float): # only round some types
					round(self.variable, 2)
				self.finalText = self.text + str(self.variable)
			else:
				self.finalText = self.text
			self.surface = self.font.render(self.finalText, 1, (255, 255, 255))
			self.height = self.surface.get_height()
		else:
			self.surface = pygame.Surface((0, 0))

	def getHeight(self):
		try:
			self.height = self.surface.get_height()
			return self.height
		except AttributeError:
			return 0

	def getWidth(self):
		try:
			self.width = self.surface.get_width()
			return self.width
		except AttributeError:
			return 0

	def setCoords(self, coords):
		self.coords = coords

	def getYCoords(self):
		return self.coords[1]

	def hide(self):
		self.isShown = False

	def show(self):
		self.isShown = True
