import pygame
from pygame.locals import *

import gui as Gui
import grid as Grid
from reference import Colour
from reference import Objects


class Window():
	def __init__(self, variables):
		Objects.window = self

		self.window = pygame.display.set_mode((0, 0), RESIZABLE)
		self.size = self.window.get_size()

		self.scale = 1.0
		self.baseGridSize = 50

		#surfaces
		self.gridSurface = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
		self.guiSurface = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
		print("Creating Window ", self.size)

		self.grid = Grid.Grid(self.scale, self.baseGridSize, self)
		self.gui = Gui.Gui(variables)
		Objects.grid = self.grid
		Objects.gui = self.gui
		self.gridChanged = True

		self.running = True

	def isRunning(self):
		return self.running

	def quit(self):
		print("Quit")
		self.running = False

	def clear(self):
		self.window.fill(Colour.black)

	def update(self):
		self.gui.updateVariable("scale", self.scale)
		pygame.display.update()

	def resize(self, newSizeX, newSizeY):
		pygame.display.set_mode((newSizeX, newSizeY), RESIZABLE)
		self.size = self.window.get_size()
		self.gridChanged = True
		print("Window resized to ", newSizeX, "x", newSizeY)

	def blit(self, source, dest=(0, 0)):
		self.window.blit(source, dest)

	def zoomOut(self):
		if self.scale > 0.51:
			self.scale -= 0.1
			self.grid.updateScale(self.scale)
			self.gridChanged = True

	def zoomIn(self):
		if self.scale < 3:
			self.scale += 0.1
			self.grid.updateScale(self.scale)
			self.gridChanged = True

	def updateGrid(self):
		self.gridChanged = True
	
	def drawGridLines(self, displacement):
		if self.gridChanged:
			self.gridSurface.fill(Colour.black)
			self.gridSize = int(self.baseGridSize * self.scale)
			rects = []

			for x in range(self.size[0]//self.gridSize+2):
				for y in range(self.size[1]//self.gridSize+2):
					width = x*self.gridSize+(displacement[0] % self.gridSize) - self.gridSize
					height = y*self.gridSize+(displacement[1] % self.gridSize) - self.gridSize
					rects.append(Rect(width, height, self.gridSize, self.gridSize))
			for item in rects:
				pygame.draw.rect(self.gridSurface, Colour.blue, item, 1)
			self.gridChanged = False

	def updateNodes(self):
		self.grid.updateNodes()

	def drawNodes(self, displacement):
		self.grid.drawNodes(self.gridSurface, displacement)

	def blitSurfaces(self):
		self.blit(self.gridSurface)
		self.blit(self.guiSurface)

	#GUI Functions
	def drawGui(self):
		"""
			draws all elements of the gui
		"""
		self.gui.updateElements()
		self.guiSurface.fill(Colour.transparent)
		self.gui.drawAll(self.guiSurface)

	def updateGuiVariable(self, key, value):
		self.gui.updateVariable(key, value)

	def showGuiContainer(self, container):
		assert isinstance(container, str)
		try:
			self.gui.containers[container].show()
		except KeyError:
			print(container, " is not a recognised container. Called from window.py-showGuiContainer()")

	#Data Functions
	def getGrid(self):
		return self.grid

	#window dimension functions
	def getSize(self):
		return self.size

	def getWidth(self):
		return self.window.get_width()

	def getHeight(self):
		return self.window.get_height()
