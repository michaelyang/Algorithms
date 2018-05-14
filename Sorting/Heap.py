#[0, 1, 2, 3,4, 5,6, 7,8,9,10, 11,12,13,14, ...]
class Heap(object):
	def __init__(self):
		self.heap = []
		self.size = 0

	def heapify(self, i):
		while i < self.size:
			leftChild = 2*i+1
			rightChild = leftChild+1
			if rightChild < self.size and self.heap[rightChild] > self.heap[i] and self.heap[rightChild] > self.heap[leftChild]:
				self.heap[rightChild], self.heap[i] = self.heap[i], self.heap[rightChild]
				i = rightChild
			elif leftChild < self.size and self.heap[leftChild] > self.heap[i]:
				self.heap[leftChild], self.heap[i] = self.heap[i], self.heap[leftChild]
				i = leftChild
			else:
				return

	def buildMaxHeap(self, A):
		self.heap = A
		self.size = len(A)
		for i in range(self.size/2,-1,-1):
			self.heapify(i)

	def extractMax(self):
		if self.heap:
			self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
			max = self.heap.pop()
			self.size -= 1
			self.heapify(0)
			return max
		else:
			return None

	def push(self, value):
		self.__heap.append(value)