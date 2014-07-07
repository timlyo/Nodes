from pygame import *


class MouseInput:
	def __init__(self, window):
		print("Mouse input started")
		self.window = window
		self.grid = self.window.getGrid()

		self.mouseButtonDown = False
		self.mousePosition = [0, 0]
		self.previousMousePosition = [0, 0]
		self.displacedMousePos = [0, 0]
		self.mouseDownPosition = [0, 0]
		self.mouseUpPosition = [0, 0]

	def mouseDown(self, position):
		self.mouseDownPosition = position
		self.mouseButtonDown = True

	def mouseUp(self, position, displacement, button):
		self.mouseButtonDown = False
		self.mouseUpPosition = position
		if self.isClick():
			self.displacedPosition(displacement)
			if self.grid.gridClick(self.displacedMousePos, button):  # if a node is added
				self.window.updateGrid()
			else:  # select node and draw and draw info into box
				coords = self.grid.getClickCoord(self.displacedMousePos)
				node = self.grid.getNode(coords)
				self.window.updateGrid()
				print("drawing info:", node)

	def isMouseClicked(self):
		return self.mouseButtonDown

	# movement of the mouse per frame
	def getMouseMovement(self):
		self.previousMousePosition = self.mousePosition
		self.mousePosition = mouse.get_pos()
		return (self.mousePosition[0] - self.previousMousePosition[0],
			self.mousePosition[1] - self.previousMousePosition[1])

	#works out if the mouse has clicked or dragged(heuristic)
	def isClick(self):
		xMovement = self.mouseUpPosition[0] - self.mouseDownPosition[0]
		yMovement = self.mouseUpPosition[1] - self.mouseDownPosition[1]
		if abs(xMovement + yMovement) < 5:
			return True
		return False


	def displacedPosition(self, displacement):
		self.displacedMousePos[0] = self.previousMousePosition[0] - displacement[0]
		self.displacedMousePos[1] = self.previousMousePosition[1] - displacement[1]
