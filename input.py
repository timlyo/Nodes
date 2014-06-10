from pygame import *

class MouseInput:
	mouseButtonDown = False
	def __init__(self):
		print("Mouse input started")
		self.mousePositions = [[0,0],[0,0]] #current and previous positions

	def mouseDown(self,position):
		print("Mouse Button Down at ", position)
		self.mouseButtonDown = True

	def mouseUp(self,position):
		self.mouseButtonDown = False

	def getMouseMovement(self):
		self.mousePositions[1] = self.mousePositions[0]
		self.mousePositions[0] = mouse.get_pos()
		return (self.mousePositions[0][0]-self.mousePositions[1][0],
				self.mousePositions[0][1]-self.mousePositions[1][1])

	def mouseClicked(self):
		return self.mouseButtonDown