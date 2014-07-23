class Reference:
	"""
	General data for the program
	"""
	version = "0.1"
	saveFile = "save.dat"
	logFile = "log.dat"
	mainFont = None


class Colour:
	"""
	Stores a series of colours that are used throughout the program
	"""
	white = (255, 255, 255)
	black = (0, 0, 0)
	grey = (150, 150, 150)
	transparent = (0, 0, 0, 0)
	blue = (0, 0, 200)
	green = (0, 200, 0)
	yellow = (200, 200, 0)


class Objects:
	"""
	References to objects that are created in other sections of the program
	"""
	grid = None
	window = None
	gui = None
	mouseInput = None
