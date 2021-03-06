import grid

from widget import Widget
from button import Button
from container import Container

from reference import Reference
from reference import Colour
from reference import Objects


class Gui:
	def __init__(self, variables):
		self.elements = {}
		self.containers = {}
		self.variables = variables
		self.window = Objects.window
		self.grid = Objects.grid

		#initial variable values, only required for some that are created after the element
		self.variables["scale"] = 1.0

	def create(self):
		self.createElements()
		self.createContainers()
		print("Created gui")

	def drawAll(self, surface):
		for widget in self.elements:
			item = self.elements[widget]
			surface.blit(item.surface, item.coords)

	def createElements(self):
		self.elements["clearButton"] = Button("Clear", Reference.mainFont, Objects.grid.clear)
		self.elements["clearButton"].setBackground(Colour.grey)
		self.elements["quitButton"] = Button("Quit", Reference.mainFont, Objects.window.quit)
		self.elements["quitButton"].setBackground(Colour.grey)
		self.elements["randomInBut"] = Button("Randomise Input", Reference.mainFont, Objects.grid.randomiseInput)
		self.elements["randomInBut"].setBackground(Colour.grey)
		self.elements["randomNodesBut"] = Button("Randomise Nodes", Reference.mainFont, Objects.grid.randomiseNodes)
		self.elements["randomNodesBut"].setBackground(Colour.grey)

		self.elements["fps"] = Widget("fps: ", Reference.mainFont, (0, 0), self.variables["clock"].get_fps())
		self.elements["scale"] = Widget("scale: ", Reference.mainFont, (0, 0), self.variables["scale"])
		self.elements["mousePos"] = Widget("mousePos: ", Reference.mainFont, (0, 0), self.variables["mousePos"])

		#node info box stuff(prefix with an n)
		self.elements["nValue"] = Widget("Value: ", Reference.mainFont, (0, 0), "")
		self.elements["nPos"] = Widget("Position: ", Reference.mainFont, (0, 0), "")
		self.elements["nConnectionX"] = Widget("x:", Reference.mainFont, (0, 0), self.variables["activeNodeX"])
		self.elements["nConnectionY"] = Widget("y: ", Reference.mainFont, (0, 0), self.variables["activeNodeY"])

		#output box(prefix with o)
		self.elements["oInput"] = Widget("    Input: ", Reference.mainFont, (0, 0), self.variables["input"])
		self.elements["oOutput"] = Widget("Output: ", Reference.mainFont, (0, 0), self.variables["output"])

	def createContainers(self):
		self.containers["feedback"] = Container([0, 0], [5, 5])
		self.containers["feedback"].addElement(self.elements["scale"])
		self.containers["feedback"].addElement(self.elements["fps"])
		self.containers["feedback"].addElement(self.elements["mousePos"])
		self.containers["feedback"].setPosition("topRight")

		self.containers["nodeBox"] = Container([0, 0], [5, 5])
		self.containers["nodeBox"].addElement(self.elements["nPos"])
		self.containers["nodeBox"].addElement(self.elements["nValue"])
		self.containers["nodeBox"].addElement(self.elements["nConnectionX"])
		self.containers["nodeBox"].addElement(self.elements["nConnectionY"])
		self.containers["nodeBox"].setPosition("right")
		self.containers["nodeBox"].hide()

		self.containers["outputBox"] = Container([0, 0], [5, 5])
		self.containers["outputBox"].addElement(self.elements["oInput"])
		self.containers["outputBox"].addElement(self.elements["oOutput"])
		self.containers["outputBox"].setPosition("bottomRight")

		self.containers["buttons"] = Container([0, 0], [5, 5])
		self.containers["buttons"].addElement(self.elements["clearButton"])
		self.containers["buttons"].addElement(self.elements["quitButton"])
		self.containers["buttons"].addElement(self.elements["randomInBut"])
		self.containers["buttons"].addElement(self.elements["randomNodesBut"])

	def updateVariable(self, key, value):
		assert isinstance(key, str)
		if key in self.elements:
			self.elements[key].variable = value

	def updateElements(self):
		activeNode = Objects.grid.getActiveNode()
		if activeNode is not None:
			pass
			if activeNode.isDefault():
				self.elements["nValue"].hide()
			elif activeNode.isInput():
				self.elements["nConnectionY"].hide()
				self.elements["nConnectionX"].hide()
		for item in self.elements:
			self.elements[item].update()
			self.elements[item].render()
		for item in self.containers:
			self.containers[item].update()

	#button functions
	def clear(self):
		Objects.grid.clear()
		Objects.window.updateGrid()
