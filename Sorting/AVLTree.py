#[0, 1, 2, 3,4, 5,6, 7,8,9,10, 11,12,13,14, ...]
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class AVLTree:
	def __init__(self):
		self.node = None
		self.height = -1

	def insert(self, value):
		if self.node == None:
			self.node = Node(value)
			self.node.left = AVLTree()
			self.node.right = AVLTree()
		elif value <= self.node.value:
			self.node.left.insert(value)
		elif value > self.node.value:
			self.node.right.insert(value)

		self.height = 1 + max(self.node.left.height, self.node.right.height)
		
		self.balance()

	def balance(self):
		balance = self.node.left.height - self.node.right.height
		if self.node.left.node != None:
			lbalance = self.node.left.node.left.height - self.node.left.node.right.height
		else:
			lbalance = 0
		if self.node.right.node != None:
			rbalance = self.node.right.node.left.height - self.node.right.node.right.height
		else:
			rbalance = 0
		if balance > 1 and lbalance > 0:
			self.rightRotate()
		elif balance > 1 and lbalance < 0:
			self.node.left.leftRotate()
			self.rightRotate()
		elif balance < 1 and rbalance < 0:
			self.leftRotate()
		elif balance < 1 and rbalance > 0:
			self.node.right.rightRotate()
			self.leftRotate()

	def leftRotate(self):
		newNode = self.node.right.node
		newLeftNode = self.node
		newLeftNode.right.node = newNode.left.node
		newNode.left.node = newLeftNode
		self.node = newNode
		self.updateHeights()

	def rightRotate(self):
		newNode = self.node.left.node
		newRightNode = self.node
		newRightNode.left.node = newNode.right.node
		newNode.right.node = newRightNode
		self.node = newNode
		self.updateHeights()

	def updateHeights(self):
		if self.node == None:
			self.height = -1
		else:
			if self.node.left != None:
				self.node.left.updateHeights()
			if self.node.right != None:
				self.node.right.updateHeights()
			self.height = 1 + max(self.node.left.height, self.node.right.height)

	def inOrderList(self, sortedList):
		if self.node == None:
			return
		self.node.left.inOrderList(sortedList)
		sortedList.append(self.node.value)
		self.node.right.inOrderList(sortedList)

	def sortedList(self):
		result = []
		self.inOrderList(result)
		return result

	def display(self, level=0, dir = ""):
		if(self.node != None):
			print '\t' * level, dir, self.node.value, "[h: " + str(self.height) + "]"
			if self.node.left != None: 
				self.node.left.display(level + 1, '/')
			if self.node.left != None:
				self.node.right.display(level + 1, '\\')
