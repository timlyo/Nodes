from pygame import *
from reference import Objects


class MouseInput:
	def __init__(self):
		print("Mouse input started")
		self.mouseButtonDown = False
		self.mousePosition = [0, 0]
		self.previousMousePosition = [0, 0]
		self.displacedMousePos = [0, 0]
		self.mouseDownPosition = [0, 0]
		self.mouseUpPosition = [0, 0]

		Objects.mouseInput = self

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
			if button == 1:  # pull out clicks on gui elements
				clickObject = self.isInClickField(position)
				if clickObject:
					print(clickObject)
					assert not isinstance(clickObject, bool)
					clickObject()
					return

			self.displacedPosition(displacement)
			if Objects.grid.gridClick(self.displacedMousePos, button):  # if a node is added
				Objects.window.updateGrid()
			else:  # select node and draw and draw info into box
				coords = Objects.grid.getGridCoord(self.displacedMousePos)
				node = Objects.grid.getNode(coords)
				if button == 1:
					if not Objects.grid.activateNode(node):
						print("Not activated")
				elif button == 2:
					Objects.grid.changeNodeType(node)
				Objects.window.updateGrid()

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


class KeyboardInput():
	def __init__(self):
		print("keyboard input started")

	def handleKey(self, pressedKey):
		activeNode = Objects.grid.getActiveNode()
		mods = key.get_mods()
		if activeNode is not None:
			if pressedKey == K_TAB:
				activeNode.changeValue()
			elif pressedKey == K_q:
				activeNode.changeType()

			moveKeys = (K_UP, K_DOWN, K_LEFT, K_RIGHT)
			if pressedKey in moveKeys:
				if mods & KMOD_LSHIFT:
					Objects.grid.moveActiveNode(pressedKey, True)

			nodeModKeys = (K_w, K_e, K_r, K_s, K_d, K_f)
			if pressedKey in nodeModKeys:
				if pressedKey == K_w:
					activeNode.changeConnectionType(0, "none")
				if pressedKey == K_e:
					activeNode.changeConnectionType(0, "xor")
				if pressedKey == K_r:
					activeNode.changeConnectionType(0, "not")
				if pressedKey == K_s:
					activeNode.changeConnectionType(1, "none")
				if pressedKey == K_d:
					activeNode.changeConnectionType(1, "xor")
				if pressedKey == K_f:
					activeNode.changeConnectionType(1, "not")
