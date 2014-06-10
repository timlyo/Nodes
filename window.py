import pygame
from pygame.locals import *

import random

class Window():
	def __init__(self):
		self.window = pygame.display.set_mode((0,0),RESIZABLE)
		self.size = self.window.get_size()

		self.scale = 1.0
		self.gridSize = 50

		self.gridSurface = pygame.Surface(self.size)

		print("Creating Window")

	def clear(self):
		self.window.fill((0,0,0))

	def update(self):
		pygame.display.update()

	def resize(self,newSizeX,newSizeY):
		pygame.display.set_mode((newSizeX,newSizeY),RESIZABLE)
		self.size = self.window.get_size()
		print("Window resized to ", newSizeX, "x", newSizeY)

	def blit(self, source, dest=(0,0)):
		self.window.blit(source,dest)

	def zoomOut(self):
		if(self.scale > 0.11):
			self.scale -= 0.1
		print("Scale changed:", self.scale)

	def zoomIn(self):
		if(self.scale < 5):
			self.scale += 0.1
		print("Scale changed:", self.scale)
	
	def drawGrid(self,displacement):
		self.gridSurface.fill((0,0,0))
		rects = []
		gridSize = int(self.gridSize * self.scale)

		for x in range(0,self.size[0]//self.gridSize+1):
			for y in range(0,self.size[1]//self.gridSize+1):
				rects.append(Rect(x*self.gridSize+displacement[0],y*self.gridSize+displacement[1],
									self.gridSize,self.gridSize))
		for item in rects:
			pygame.draw.rect(self.gridSurface, (0,0,random.randint(255,255)), item, 1)

		self.blit(self.gridSurface)