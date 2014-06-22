from pygame import *

class MouseInput:
	mouseButtonDown = False
	def __init__(self, window):
		print("Mouse input started")
		self.window = window

		self.mousePosition = [0, 0]
		self.previousMousePosition = [0, 0]
		self.displacedMousePos = [0, 0]
		self.mouseDownPosition = [0, 0]

	def mouseDown(self, position):
		self.mouseDownPosition = mouse.get_pos()
		self.mouseButtonDown = True

	def mouseUp(self, position, displacement):
		self.mouseButtonDown = False
		if self.isClick():
			self.displacedPosition(displacement)

	def isMouseClicked(self):
		return self.mouseButtonDown

	#movement of the mouse per frame
	def getMouseMovement(self):
		self.previousMousePosition = self.mousePosition
		self.mousePosition = mouse.get_pos()
		return (self.mousePosition[0] - self.previousMousePosition[0],
				self.mousePosition[1] - self.previousMousePosition[1])

	#works out if the mouse has clicked of dragged(heuristic)
	def isClick(self):
		xMovement = self.mouseDownPosition[0] - self.mousePosition[0]
		yMovement = self.mouseDownPosition[1] - self.mousePosition[1]
		if abs(xMovement + yMovement) < 5:
			return True
		return False


	def displacedPosition(self, displacement):
		self.displacedMousePos[0] = self.previousMousePosition[0] + displacement[0]
		self.displacedMousePos[1] = self.previousMousePosition[1] + displacement[1]
		print("Screen click at " , self.mousePosition)
		print("Grid click at ", self.displacedMousePos)
