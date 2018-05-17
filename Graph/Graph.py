#[0, 1, 2, 3,4, 5,6, 7,8,9,10, 11,12,13,14, ...]
class Vertex:
	def __init__(self, key):
		self.key = key
		self.neighbors = []

	def addNeighbor(self, neighbor):
		self.neighbors.append(neighbor)

	def getNeighbors(self):
		return self.neighbors

	def __repr__(self):
		return self.key

	def __str__(self):
		return self.key

	def __lt__(self, other):
         return self.key < other.key

class Graph:
	def __init__(self):
		self.verticies = {}

	def addVertex(self, key):
		self.verticies[key] = Vertex(key)

	def addEdge(self, a, b, undirected = True):
		if a not in self.verticies:
			self.addVertex(a)
		if b not in self.verticies:
			self.addVertex(b)
		self.verticies[a].addNeighbor(self.verticies[b])
		if a != b and undirected:
			self.verticies[b].addNeighbor(self.verticies[a])

	def getVerticies(self):
		return sorted(self.verticies.values())

	def size(self):
		return len(self.verticies)