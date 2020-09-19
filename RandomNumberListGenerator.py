"""
AUTHOR: Jamesong7822

This file generates a *.txt file of random numbers.

"""

import random
import argparse
import cProfile

parser = argparse.ArgumentParser(description="Generate a list of random numbers")
# parser.add_argument("minimum", type=int, help="Minimum integer number to generate")
# parser.add_argument("maximum", type=int, help="Maximum integer number to generate")
parser.add_argument("number", type=int, help="Number of integer numbers to generate")

def main():
	args = parser.parse_args()
	# minimum = args.minimum
	# maximum = args.maximum
	number = args.number
	minimum = 1
	maximum = number + 1
	# assert(number < maximum-minimum+1)
	randList = generateNumber(minimum, maximum, number)
	writeToFile(randList, "sample.txt")
	
	
def generateNumber(minimum, maximum, number):
	randList = random.sample(range(minimum, maximum), number)
	return randList
	
def writeToFile(data, filePath):
	with open(filePath, "w+") as f:
		for number in data:
			f.write(str(number))
			f.write("\n")


if __name__ == "__main__":
	cProfile.run("main()")
