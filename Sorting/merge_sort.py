#!/usr/bin/python
import sys
import os
import argparse

_defaultTestFile = 'test.txt'

def mergeSort(unsortedList):
	if len(unsortedList) <= 1:
		return unsortedList
	else:
		mid = len(unsortedList)/2
		return merge(mergeSort(unsortedList[:mid]),mergeSort(unsortedList[mid:]))

def merge(listA, listB):
	i,j = 0,0
	res = []
	while (i < len(listA) and j < len(listB)):
		if listA[i] < listB[j]:
			res.append(listA[i])
			i+=1
		else:
			res.append(listB[j])
			j+=1
	res.extend(listA[i:len(listA)]+listB[j:len(listB)])
	return res

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
	#python merge_sort.py -f test.txt
	parser = argparse.ArgumentParser(description='provide test file')
	parser.add_argument('--file', '-f', type=str, help='name of the file containing test cases', default=_defaultTestFile)
	args = parser.parse_args()
	#file = args.file
	testCases = translateFile(args.file)
	results = []
	for testCase in testCases:
		results.append(mergeSort(testCase))
	for result in results:
		print result

if __name__ == '__main__':
	main()