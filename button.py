import pygame

from widget import Widget
from reference import Objects


class Button(Widget):
	def __init__(self, text, font, function, coords=(0, 0), dimensions=(0, 0)):
		super(Button, self).__init__(text, font)
		self.dimensions = (self.getWidth(), self.getHeight())
		self.function = function
		clickField = pygame.Rect(coords, self.dimensions)
		self.index = Objects.mouseInput.addClickField(clickField, self.function)

	def update(self):
		self.dimensions = (self.getWidth(), self.getHeight())
		clickField = pygame.Rect(self.coords, self.dimensions)
		Objects.mouseInput.addClickField(clickField, self.function, self.index)
