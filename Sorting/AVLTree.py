#[0, 1, 2, 3,4, 5,6, 7,8,9,10, 11,12,13,14, ...]
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.height = 0
		self.parent = None

class AVLTree:
	def __init__(self):
		self.root = None

	def setRoot(self, value):
		self.root = Node(value)

	def insert(self, value):
		if self.root == None:
			self.setRoot(value)
		else:
			self.insertNode(self.root,value)

	def insertNode(self, curNode, value):
		if curNode.value <= value:
			if curNode.left == None:
				curNode.left = Node(value)
			else:
				self.insertNode(curNode.left, value)
		elif curNode.value > value:
			if curNode.right == None:
				curNode.right = Node(value)
			else:
				self.insertNode(curNode.right, value)
		curNode.height = 1 + max(self.getHeight(curNode.left), self.getHeight(curNode.right))


	def getHeight(self, node):
		if not node:
			return 0
		else:
			return node.height

	def getHeight(self, node):


	def leftRotate(self, node):
		newRoot = node.rightChild
		newLeftChild = node
		if node.leftChild is not None:
			 newLeftChild.rightChild = node.leftChild




	def inOrderList(self, node, sortedList):
		if node == None:
			return
		self.inOrderList(node.right, sortedList)
		sortedList.append(node.value)
		self.inOrderList(node.left, sortedList)

	def sortedList(self):
		result = []
		self.inOrderList(self.root, result)
		return result