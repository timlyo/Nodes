import pygame
from pygame.locals import *

import gui as Gui
import grid as Grid

import random

class Window():
	def __init__(self,variables):
		self.window = pygame.display.set_mode((0,0),RESIZABLE)
		self.size = self.window.get_size()

		self.scale = 1.0
		self.baseGridSize = 50

		#surfaces
		self.gridSurface = pygame.Surface(self.size)
		self.guiSurface  = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
		print("Creating Window")

		self.grid = Grid.Grid(self.scale, self.baseGridSize)
		self.gui = Gui.Gui(variables)
		self.gridChanged = True

	def clear(self):
		self.window.fill((0,0,0))

	def update(self):
		self.gui.updateVariable("scale", self.scale)
		pygame.display.update()

	def resize(self,newSizeX,newSizeY):
		pygame.display.set_mode((newSizeX,newSizeY),RESIZABLE)
		self.size = self.window.get_size()
		self.gridChanged = True
		print("Window resized to ", newSizeX, "x", newSizeY)

	def blit(self, source, dest=(0,0)):
		self.window.blit(source,dest)

	def zoomOut(self):
		if(self.scale > 0.51):
			self.scale -= 0.1
			self.grid.updateScale(self.scale)
			self.gridChanged = True

	def zoomIn(self):
		if(self.scale < 3):
			self.scale += 0.1
			self.grid.updateScale(self.scale)
			self.gridChanged = True

	def updateGrid(self):
		self.gridChanged = True
	
	def drawGridLines(self,displacement):
		if self.gridChanged:
			self.gridSurface.fill((0,0,0))
			self.gridSize = int(self.baseGridSize * self.scale)
			rects = []

			#to stop grid rendering at top left edge
			if displacement[0] > 0:
				xAdjustment = 0
			else:
				xAdjustment = self.gridSize

			if displacement[1] > 0:
				yAdjustment = 0
			else:
				yAdjustment = self.gridSize

			for x in range(0,self.size[0]//self.gridSize+1):
				for y in range(0,self.size[1]//self.gridSize+1):
					rects.append(Rect(x*self.gridSize+(displacement[0]%self.gridSize)-xAdjustment,
									  y*self.gridSize+(displacement[1]%self.gridSize)-yAdjustment,
										self.gridSize,self.gridSize))
			for item in rects:
				pygame.draw.rect(self.gridSurface, (0,0,200), item, 1)
			self.gridChanged = False

	def drawNodes(self,displacement):
		self.grid.drawNodes(self.gridSurface, displacement)

	def blitSurfaces(self):
		self.blit(self.gridSurface)
		self.blit(self.guiSurface)

	#GUI Functions
	def drawGui(self):
		self.gui.updateElements()
		self.guiSurface.fill((0,0,0,0))
		self.gui.draw(self.guiSurface)

	def updateGuiVariable(self, key, value):
		self.gui.updateVariable(key, value)

	#Other Functions
	def getGrid(self):
		return self.grid