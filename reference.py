import pygame


class Reference:
	version = "0.1"
	saveFile = "save.dat"
	mainFont = None


class Colour:
	white = (255, 255, 255)
	black = (0, 0, 0)
	grey = (150, 150, 150)
	transparent = (0, 0, 0, 0)
	blue = (0, 0, 200)
	green = (0, 200, 0)


class Objects:
	grid = None
	window = None
	gui = None
	mouseInput = None
