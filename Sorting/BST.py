#[0, 1, 2, 3,4, 5,6, 7,8,9,10, 11,12,13,14, ...]
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST:
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
		if value <= curNode.value:
			if curNode.left == None:
				curNode.left = Node(value)
			else:
				self.insertNode(curNode.left, value)
		elif value > curNode.value:
			if curNode.right == None:
				curNode.right = Node(value)
			else:
				self.insertNode(curNode.right, value)

	def inOrderList(self, node, sortedList):
		if node == None:
			return
		self.inOrderList(node.left, sortedList)
		sortedList.append(node.value)
		self.inOrderList(node.right, sortedList)

	def sortedList(self):
		result = []
		self.inOrderList(self.root, result)
		return result