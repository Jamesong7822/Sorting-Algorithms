from BaseSorter import BaseSorter

class SelectionSort(BaseSorter):

	def __init__(self):
		BaseSorter.__init__(self, "SelectionSort", "sample.txt")
		
	def sort(self):
		length = len(self.data)
		sortedArray = self.data.copy()
		
		if length == 1:
			return self.data
		else:
			minIndex = 0
			for i in range(length-1):
				for j in range(i, length):
					if sortedArray[j] < sortedArray[minIndex]:
						minIndex = j
						
				sortedArray = self.swap(sortedArray, minIndex, i)
				
		print (sortedArray)
				
						
	def swap(self, sortedArray, minIndex, currentIndex):
		toSwap = sortedArray[currentIndex]
		sortedArray[currentIndex] = sortedArray[minIndex]
		sortedArray[minIndex] = toSwap
		return sortedArray
		
		
def main():
	a = SelectionSort()
	a.sort()
	
if __name__ == "__main__":
	import cProfile
	cProfile.run("main()")