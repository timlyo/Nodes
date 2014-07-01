class Widget:
	def __init__(self, text, font, coords, variable="", changes=False):
		self.text = text
		self.font = font
		self.coords = coords
		self.variable = variable
		self.changes = changes
		self.height = 0
		self.width = 0

		self.render()

	def render(self):
		self.finalText = self.text + str(round(self.variable, 2))
		self.surface = self.font.render(self.finalText, 1, (255, 255, 255))
		self.height = self.surface.get_height()

	def getHeight(self):
		self.height = self.surface.get_height()
		return self.height

	def getWidth(self):
		self.width = self.surface.get_width()
		return self.width

	def setCoords(self, coords):
		self.coords = coords

	def getYCoords(self):
		return self.coords[1]
