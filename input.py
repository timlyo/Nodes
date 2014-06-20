from pygame import *

class MouseInput:
	mouseButtonDown = False
	def __init__(self):
		print("Mouse input started")
		self.mousePosition = [0, 0]
		self.previousMousePosition = [0, 0]
		self.clickPos = [0, 0]

	def mouseDown(self, position):
		self.mouseButtonDown = True

	def mouseUp(self, position, displacement):
		self.mouseButtonDown = False
		if self.getMouseMovement()[0] + self.getMouseMovement()[1] < 5:
			self.displacedPosition(displacement)

	def isMouseClicked(self):
		return self.mouseButtonDown

	def getMouseMovement(self):
		self.previousMousePosition = self.mousePosition
		self.mousePosition = mouse.get_pos()
		return (self.mousePosition[0] - self.previousMousePosition[0],
				self.mousePosition[1] - self.previousMousePosition[1])

	def displacedPosition(self, displacement):
		self.clickPos[0] = self.previousMousePosition[0] + displacement[0]
		self.clickPos[1] = self.previousMousePosition[1] + displacement[1]
		print("Click at ", self.clickPos)
