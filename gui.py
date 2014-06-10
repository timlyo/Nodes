import pygame

class Gui:
	def __init__(self):
		self.mainFont = pygame.font.Font(None, 24)
		self.elements = {}

		self.createElements()
		print ("created gui")

	def draw(self, surface):
		for item in self.elements:
			surface.blit(self.elements[item].surface,(0,0))

	def createElements(self):
		self.elements["fps"] = Widget("Hello World", self.mainFont, (0,0) )

class Widget:
	def __init__(self, text, font, position):
		self.surface = font.render(text ,1 , (255,255,255))
		self.position = position