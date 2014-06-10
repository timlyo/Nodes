import pygame

class Window:
	height = 800
	width  = 600
	def __init__(self):
		print("Created Window")
		window = pygame.display.set_mode(width,height)
