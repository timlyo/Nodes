import pygame

from widget import Widget
from reference import Objects


class Button(Widget):
	def __init__(self, text, font, coords=(0, 0), dimensions=(0, 0)):
		super(Button, self).__init__(text, font)
		self.dimensions = (self.getWidth(), self.getHeight())
		clickField = pygame.Rect(coords, self.dimensions)
		self.index = Objects.mouseInput.addClickField(clickField, self)

	def click(self):
		Objects.grid.clear()
		Objects.window.updateGrid()
