from os.path import isfile

from reference import Objects
from reference import Reference


class Logging:
	def __init__(self):
		print("started logger")
		Objects.logging = self

	def saveGridData(self, gridInput, gridOutput):
		assert isinstance(gridInput, str)
		assert isinstance(gridOutput, str)

		file = open(Reference.logFile, "w")
		print("Writing log to", Reference.logFile)

		line = gridInput + " " + gridOutput + "\n"
		print(repr(line))
		file.write(line)
