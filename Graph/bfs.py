#!/usr/bin/python
import sys
import os
import argparse
from Graph import *

_defaultTestFile = 'test.txt'

def bfs(graph, v):
	currentLevel = 0
	level = { v: currentLevel }
	frontier = v.neighbors
	while frontier:
		currentLevel+=1
		nextFrontier = []
		for v in frontier:
			if v not in level:
				level[v] = currentLevel
				for n in v.neighbors:
					if n not in level and n not in frontier:
						nextFrontier.append(n)
		frontier = nextFrontier
	return level

def translateFile(file = _defaultTestFile):
	res = []
	if not os.path.isfile(file):
		print("No such file: {}".format(file))
		sys.exit()
	with open(file) as f:
		while True:
			g = Graph()
			vLine = f.readline()
			eLine = f.readline()
			if not eLine:
				break
			verticies = map(str, vLine.rstrip().split(' '))
			edges = map(str, eLine.rstrip().split(', '))
			for v in verticies:
				g.addVertex(v)
			for e in edges:
				el = e.split()
				g.addEdge(el[0], el[1])
			res.append(g)
	return res

def main():
	#python insertion_sort.py -f test.txt
	parser = argparse.ArgumentParser(description='provide test file')
	parser.add_argument('--file', '-f', type=str, help='name of the file containing test cases', default=_defaultTestFile)
	args = parser.parse_args()
	file = args.file
	testGraphs = translateFile(args.file)
	results = []
	for testGraph in testGraphs:
		verticies = testGraph.getVerticies()
		print "-"*10
		for v in verticies:
			print v.key + " : " + ', '.join(map(str,v.neighbors))
		results.append(bfs(testGraph, verticies[0]))
	print "--Results--"
	for result in results:
		print result

if __name__ == '__main__':
	main()