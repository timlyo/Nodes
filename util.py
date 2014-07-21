class Util:
	@staticmethod
	def removeFromString(string, items):
		""" Removes a list of strings from the string passed to it
		:param string: The string that the characters are to be removed from
		:param items: the characters that are to be removed
		:return: the modified string
		"""
		string = str(string)

		for item in items:
			string = string.replace(item, "")

		return string

	@staticmethod
	def addLists(tuple1, tuple2):
		result = []
		for index in range(len(tuple1)):
			if index >= len(tuple2):
				return result
			result.append(tuple1[index] + tuple2[index])

		return tuple(result)
