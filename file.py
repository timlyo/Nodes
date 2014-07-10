from os.path import isfile
from reference import Reference

class File:
	@staticmethod
	def loadFile(grid):
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
				grid.addNode(coords, line[2], line[3])

		file.close()


	@staticmethod
	def saveFile(nodes):
		if len(nodes) is 0:
			return
		assert isinstance(nodes, dict)
		file = open(Reference.saveFile, "w")
		print("Saving to ", Reference.saveFile )
		print(nodes)
		for nodeIndex in nodes:
			node = nodes[nodeIndex]
			coords = str(nodeIndex).replace("(", "").replace(")", "")
			line = coords + " " + str(node.value) + " " + node.type + "\n"
			file.write(line)
		file.close()
