#!/usr/bin/env python2.7
import sys, os
import argparse

_defaultTestFile = 'test.txt'

def quickSort(unsortedList):
	if len(unsortedList) > 1:
		pivot = unsortedList[-1]
		leftList = []
		rightList = []
		for a in unsortedList[:-1]:
			if a <= pivot:
				leftList.append(a)
			else:
				rightList.append(a)
		return quickSort(leftList) + [pivot] + quickSort(rightList)
	else:
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
	#python quick_sort.py -f test.txt
	parser = argparse.ArgumentParser(description='provide test file')
	parser.add_argument('--file', '-f', type=str, help='name of the file containing test cases', default=_defaultTestFile)
	args = parser.parse_args()
	#file = args.file
	testCases = translateFile(args.file)
	results = []
	for testCase in testCases:
		results.append(quickSort(testCase))
	for result in results:
		print result

if __name__ == '__main__':
	main()