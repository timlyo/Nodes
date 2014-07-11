from pygame import *
from reference import Objects


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

		#list of rects where clicky things happen
		self.clickFields = []

	def addClickField(self, field, function, index=None):
		if index is None:
			index = len(self.clickFields)
		self.clickFields.insert(index, (field, function))
		return index

	def isInClickField(self, pos):
		for item in self.clickFields:
			if item[0].collidepoint(pos):
				return item[1]
		return False

	def mouseDown(self, position):
		self.mouseDownPosition = position
		self.mouseButtonDown = True

	def mouseUp(self, position, displacement, button):
		self.mouseButtonDown = False
		self.mouseUpPosition = position
		if self.isClick():
			if button == 1:
				clickObject = self.isInClickField(position)
				if clickObject:
					print(clickObject)
					clickObject(Objects.grid)
					return

			self.displacedPosition(displacement)
			if self.grid.gridClick(self.displacedMousePos, button):  # if a node is added
				self.window.updateGrid()
			else:  # select node and draw and draw info into box
				coords = self.grid.getGridCoord(self.displacedMousePos)
				node = self.grid.getNode(coords)
				if button == 1:
					self.grid.activateNode(node)
				elif button == 2:
					self.grid.changeNodeType(node)
				self.window.updateGrid()

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
