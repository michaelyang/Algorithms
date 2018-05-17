#!/usr/bin/python
'''
Given an array of integers, for each index, find product of all elements except for the one at that index. No division. 
[1]*[2]*[3]*[4] [0]*[2]*[3]*[4] [0]*[1]*[3]*[4] [0]*[1]*[2]*[3]
'''
import sys
import os
import argparse

def productExceptItem(list):
	n = len(list)
	res = [0]*n
	'''
	forward = [1]
	backward = [1]
	for i in range(1, n):
		forward.append(forward[i-1]*list[i-1])
		backward.append(backward[i-1]*list[-1*i])
	return [forward[i]*backward[-1*i-1] for i in range(n)]
	'''
	p = 1
	for i in range(n):
		res[i] = p
		p *= list[i]

	p = 1
	for i in range(n):
		res[n-1-i] *= p
		p *= list[n-1-i]
	return res


def main():
	testCases = [[1, 7, 3, 4], [0,4,1,3], [1,2,3,4], [0, 0]]
	results = []
	for testCase in testCases:
		results.append(productExceptItem(testCase))
	for result in results:
		print result

if __name__ == '__main__':
	main()