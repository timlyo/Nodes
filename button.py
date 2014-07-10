from widget import Widget
from reference import objects


class Button(Widget):
	def __init__(self, text, font, coords=(0, 0), dimensions=(0, 0)):
		super(Button, self).__init__(text, font)
		self.dimensions = (self.getWidth(), self.getHeight())
		objects.mouseInput.addClickField(1)
