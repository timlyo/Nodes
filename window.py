import pygame
from pygame.locals import *

import gui as Gui

import random

class Window():
	def __init__(self,variables):
		self.window = pygame.display.set_mode((0,0),RESIZABLE)
		self.size = self.window.get_size()

		self.scale = 1.0
		self.baseGridSize = 50

		self.gridSurface = pygame.Surface(self.size)
		self.guiSurface = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
		print("Creating Window")

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
			self.gridChanged = True
			print("Scale changed:", self.scale)

	def zoomIn(self):
		if(self.scale < 3):
			self.scale += 0.1
			self.gridChanged = True
			print("Scale changed:", self.scale)
	
	def drawGrid(self,displacement):
		if self.gridChanged:
			self.gridSurface.fill((0,0,0))
			self.gridSize = int(self.baseGridSize * self.scale)
			rects = []

			for x in range(0,self.size[0]//self.gridSize+1):
				for y in range(0,self.size[1]//self.gridSize+1):
					rects.append(Rect(x*self.gridSize+displacement[0],
									  y*self.gridSize+displacement[1],
										self.gridSize,self.gridSize))
			for item in rects:
				pygame.draw.rect(self.gridSurface, (0,0,random.randint(255,255)), item, 1)
			self.gridChanged = False
			print("Grid recreated")

		self.blit(self.gridSurface)


	#GUI Functions
	def drawGui(self):
		self.gui.updateElements()
		self.guiSurface.fill((0,0,0,0))
		self.gui.draw(self.guiSurface)
		self.blit(self.guiSurface)

	def updateGuiVariable(self, key, value):
		self.gui.updateVariable(key, value)