#!/usr/bin/python
import sys
import os
import argparse
from Graph import *

_defaultTestFile = 'test.txt'

def dfs(graph):
	visited = []
	verticies = graph.getVerticies()
	def dfsVisit(graph, v, visited):
		neighbors = v.getNeighbors()
		visited.append(v)
		for n in neighbors:
			if n not in visited:
				dfsVisit(graph, n, visited)
	for v in verticies:
		if v not in visited:
			dfsVisit(graph, v, visited)
	return visited

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
		results.append(dfs(testGraph))
	print "--Results--"
	for result in results:
		print result

if __name__ == '__main__':
	main()