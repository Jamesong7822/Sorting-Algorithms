class BaseSorter:
	def __init__(self, name, filePath):
		self.name = name
		self.filePath = filePath
		self.readFile()
		
	def readFile(self):
		with open(self.filePath, "r") as f:
			self.data = [int(x.strip("\n")) for x in f.readlines()]
