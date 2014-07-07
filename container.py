#holds references to elements and adjust their position to fit into a container
class Container:
	def __init__(self, window, coords=[0, 0], spacing=[0, 5], width=0, height=0):
		self.elements = []
		self.window = window
		self.position = "left"
		self.coords = coords
		self.target = coords
		self.speed = 5  # (coords - target)/speed therefore higher values are slower
		self.spacing = spacing
		self.width = width
		self.height = height

	def addElement(self, element):
		self.elements.append(element)

	def setPosition(self, position):
		self.position = position

	def updatePosition(self):
		if self.position == "left":
			self.coords[0] = 0
		elif self.position == "top":
			self.coords[1] = 0
		elif self.position == "right":
			self.coords[0] = self.window.getWidth() - self.width
		elif not isinstance(self.position, str):
			print("Position of type ", type(self.position), " not recognised")
			return

	#sets the container width to the width of the widest element
	def updateWidth(self):
		width = 0
		for item in self.elements:
			if item.getWidth() > width:
				width = item.getWidth()
		self.width = width

	#sets the container height to the total height of all elements
	def updateHeight(self):
		height = 0
		for item in self.elements:
			height += item.getHeight()
		self.height = height

	#position the container's elements
	def positionElements(self):
		for index in range(len(self.elements)):
			element = self.elements[index]
			spacing = self.spacing
			if self.position is "left":
				spacing[0] = self.spacing[0]
			elif self.position is "right":
				spacing[0] = - abs(self.spacing[0])
			if index is 1:
				element.setCoords((self.coords[0] + spacing[0], self.coords[1] + spacing[1]))
			else:
				previousElement = self.elements[index - 1]
				newYPos = previousElement.getYCoords() + previousElement.getHeight() + spacing[1]
				self.elements[index].setCoords((self.coords[0] + spacing[0], newYPos))

	def setTarget(self, target):
		print("target type :", type(target))
		self.target = target

	#moves the container towards the target at it's speed
	def move(self):
		if self.coords is not self.target:
			self.coords[0] += (self.coords[0] - self.target[0]) / self.speed
			self.coords[1] += (self.coords[1] - self.target[1]) / self.speed
