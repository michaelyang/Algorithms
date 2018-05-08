#!/usr/bin/python
import sys
import os
import argparse

_defaultTestFile = 'test.txt'

def insertionSort(unsortedList):
	for i in range(1,len(unsortedList)):
		j = i
		current = unsortedList[i]
		while j > 0 and current < unsortedList[j-1]:
			unsortedList[j] = unsortedList[j-1]
			j-=1
		unsortedList[j] = current
	return unsortedList

def translateFile(file = _defaultTestFile):
	if not os.path.isfile(file):
		print("No such file: {}".format(file))
		sys.exit()
	res = []
	with open(file) as f:
		for line in f:
			res.append(map(int,line.strip().split(' ')))
	return res

def main():
	#python insertion_sort.py -f test.txt
	parser = argparse.ArgumentParser(description='provide test file')
	parser.add_argument('--file', '-f', type=str, help='name of the file containing test cases', default=_defaultTestFile)
	args = parser.parse_args()
	#file = args.file
	testCases = translateFile(args.file)
	results = []
	for testCase in testCases:
		results.append(insertionSort(testCase))
	for result in results:
		print result

if __name__ == '__main__':
	main()