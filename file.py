from os.path import isfile
from reference import Reference
from reference import Objects


class File:
	@staticmethod
	def loadFile():
		"""
		Loads the file named in references add changes the node list to it's value
		:return: None
		"""
		if isfile(Reference.saveFile):
			file = open(Reference.saveFile, "r")
		else:
			print(Reference.saveFile, " not found")
			return

		for line in file:
			if line is not "\n":
				line = line.replace("\n", "").split(" ")
				xCord = line[0].replace(",", "").split(".")[0]
				yCord = line[1].split(".")[0]
				coords = (int(xCord), int(yCord))
				Objects.grid.addNode(coords, line[2], line[4])

		file.close()

	@staticmethod
	def saveFile(nodes):
		"""
		saves the list of nodes to the filename in references
		:param nodes: the nodes to be saved
		:return: None
		"""
		assert isinstance(nodes, dict)
		file = open(Reference.saveFile, "w")
		print("Saving to ", Reference.saveFile )
		if len(nodes) is 0:
			file.close()
			return
		for nodeIndex in nodes:
			node = nodes[nodeIndex]
			coords = str(nodeIndex).replace("(", "").replace(")", "")
			value = str(node.value).replace("[", "").replace("]", "").replace(",", "")
			line = coords + " " + value + " " + node.type + "\n"
			file.write(line)
		file.write("\n")
		file.close()
