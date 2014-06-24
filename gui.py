import pygame

class Gui:
	def __init__(self,variables):
		self.mainFont = pygame.font.Font(None, 24)
		self.elements = {}
		self.variables = variables

		#initial variable values
		self.variables["scale"] = 1.0

		self.createElements()
		print ("Created gui")

	def draw(self, surface):
		for widget in self.elements:
			item = self.elements[widget]
			surface.blit(item.surface, item.position)

	def createElements(self):
		self.elements["fps"] = Widget("fps: ", self.mainFont, (0,0), self.variables["clock"].get_fps(), True)

		self.elements["scale"] = Widget("scale: ", self.mainFont, (0,self.elements["fps"].height), self.variables["scale"], True)

	def updateVariable(self, key, value):
		self.elements[key].variable = value

	def updateElements(self):
		for item in self.elements:
			if(self.elements[item].changes == True):
				self.elements[item].render()


class Widget:
	def __init__(self, text, font, position, variable="", changes=False):
		self.text = text
		self.font = font
		self.position = position
		self.variable = variable
		self.changes = changes
		self.height = 0
		
		self.render()

	def render(self):
		self.finalText = self.text + str(round(self.variable, 2))
		self.surface = self.font.render(self.finalText, 1, (255,255,255))
		self.height = self.surface.get_height()
