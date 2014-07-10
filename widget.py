import pygame
from reference import colour


class Widget:
	def __init__(self, text, font, coords=(0, 0), variable="", padding=5):
		self.text = text
		self.finalText = ""
		self.font = font
		self.coords = coords
		self.variable = variable
		self.height = 0
		self.width = 0
		self.surface = pygame.Surface((0, 0))
		self.background = colour.transparent
		self.padding = padding

		self.isShown = True

		self.render()

	def render(self):
		if self.isShown:
			#string
			if self.variable is not "":
				if isinstance(self.variable, float):  # only round some types
					round(self.variable, 2)
				self.finalText = self.text + str(self.variable)
			else:
				self.finalText = self.text
			self.surface = self.font.render(self.finalText, 1, (255, 255, 255))
			self.height = self.surface.get_height()
			self.width = self.surface.get_width()

			#background
			background = pygame.Surface((self.width+(self.padding*2), self.height+(self.padding*2)))
			background.fill(self.background)
			background.blit(self.surface, (self.padding, self.padding))
			self.surface = background
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

	def setBackground(self, colour):
		assert isinstance(colour, tuple)
		self.background = colour
		print(self, " background is now ", colour)
