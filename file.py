class File:
	@staticmethod
	def loadFile():

		file = open("save.dat", "r")


	@staticmethod
	def saveFile(nodes):
		assert isinstance(nodes, dict)
		file = open("save.dat", "w")
		print("Saving")
		print(nodes)
		for nodeIndex in nodes:
			line = str(nodeIndex) + " " + nodes[nodeIndex].type + "\n"
			file.write(line)
