from os.path import isfile
from reference import Reference
from reference import Objects

from util import Util


class File:
	@staticmethod
	def saveFile():
		"""saves the list of nodes to the filename in references
		"""
		nodes = Objects.grid.getNodeList()
		file = open(Reference.saveFile, "w")
		print("Saving to ", Reference.saveFile)

		if len(nodes) is 0:
			file.close()
			return

		for nodeIndex in nodes:
			node = nodes[nodeIndex]
			coords = Util.removeFromString(nodeIndex, ["(", ")", ","])
			value = Util.removeFromString(node.value, ["[", "]", ","]).split(" ")
			line = coords + " " + value[0] + " " + node.type + "\n"
			print(repr(line))
			file.write(line)
		file.write("\n")
		file.close()

	@staticmethod
	def loadFile():
		"""Loads the file named in references and changes the node list to it's value
		"""
		if isfile(Reference.saveFile):
			file = open(Reference.saveFile, "r")
		else:
			print(Reference.saveFile, " not found")
			return

		for line in file:
			if line is not "\n":
				line = line.replace("\n", "").split(" ")
				xCord = line[0].split(".")[0]
				yCord = line[1].split(".")[0]
				coords = (int(xCord), int(yCord))
				if line[2] == "True":
					value = True
				else:
					value
				type = line[3]
				Objects.grid.addNode(coords, value, type)

		file.close()
