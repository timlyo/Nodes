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

		self.shown = True

		self.render()

	def render(self):
		if self.shown:
			if self.variable is not "":
				self.finalText = self.text + str(round(self.variable, 2))
			else:
				self.finalText = self.text
			self.surface = self.font.render(self.finalText, 1, (255, 255, 255))
			self.height = self.surface.get_height()

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
