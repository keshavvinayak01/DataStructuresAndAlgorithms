class Node(object):

	def __init__(self,data):
		self.data = data
		self.leftChild = None
		self.rightChild = None
		self.height = 0


class AVL(object):

	def __init__(self):
		self.root = None

	def calcHeight(self,node):
		if not node:
			return -1
		return node.height
	
	def calcBalance(self,node):
		
		return (self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild))


	def rightRotate(self,node):
		print("rotating {} to the right".format(node.data))
		tempLeftNode = node.leftChild
		t = tempLeftNode.rightChild

		tempLeftNode.rightChild = node
		node.leftChild = t
		
		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
		tempLeftNode.height = max (self.calcHeight(tempLeftNode.leftChild), self.calcHeight(tempLeftNode.rightChild))

		return tempLeftNode


	def leftRotate(self,node):
		print("rotating {} to the left".format(node.data))
		temprightNode = node.rightChild
		t = temprightNode.leftChild

		temprightNode.leftChild = node
		node.rightChild = t
		
		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
		temprightNode.height = max (self.calcHeight(temprightNode.leftChild), self.calcHeight(temprightNode.rightChild))

		return temprightNode

	def settleViolation(self,data,node):
		balance = self.calcBalance(node)

		if(balance > 1 and data < node.leftChild.data):
			print("doubly left heavy situation")
			return self.rightRotate(node)


		if(balance > 1 and data > node.leftChild.data):
			print("left right heavy situation")
			node.leftChild = self.leftRotate(node.leftChild)
			return self.rightRotate(node)


		if(balance <-1  and data > node.leftChild.data):
			print("doubly right heavy situation")
			return self.leftRotate(node)


		if(balance < -1 and data < node.leftChild.data):
			print("right left heavy situation")
			node.rightChild = self.rightRotate(node.rightChild)
			return self.leftRotate(node)

		return node
	def input(self,data):
		self.root = self.inputNode(data,self.root)

	def inputNode(self,data,node):

		if not node:
			return Node(data)

		if data < node.data:
				node.leftChild = self.inputNode(data,node.leftChild)

		if data > node.data:
				node.rightChild = self.inputNode(data,node.rightChild)
		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
		
		return self.settleViolation(data,node)
		


	def delete(self,data):
		if (self.root):
			self = self.deleteNode(self.root,data)
#recursive function to aid deletion
	def deleteNode(self,node,data):

		if(data < node.data):
			node.leftChild = self.deleteNode(node.leftChild,data)          #recursively finds the node
		
		elif(data > node.data):
			node.rightChild = self.deleteNode(node.rightChild, data)

		else:
			if (node.rightChild == None and node.leftChild == None):     #node has been found, now is been classified on whether:
				print ("deleting node with no children")				 # has two children, one children(left/right), or a leaf with no 
				del node                                                 #children
				return None

			elif(node.rightChild == None):
				print("deleting node with single leftChild")
				temp = node.leftChild
				del node
				return temp

			elif(node.leftChild == None):
				print("deleting node with single rightChild")
				temp = node.rightChild
				del node
				return temp

			else:
				print("deleting node with two children")
				temp = self.getDescendant(node.leftChild)
				node.data = temp.data
				node.leftChild = self.deleteNode(node.leftChild,temp.data)

		if not node:
			return node
		balance = self.calcBalance(node)

		if balance > 1 and self.calcBalance(node.leftChild) >= 0:
			return self.rightRotate(node)

		elif balance > 1 and self.calcBalance(node.leftChild < 0):
			node.leftChild = self.rightRotate(self.leftChild)
			return self.leftRotate(node)


		if balance < -1 and self.calcBalance(node.rightChild) <= 0:
			return self.leftRotate(node)

		elif balance < -1 and self.calcBalance(node.rightChild > 0):
			node.rightChild = self.leftRotate(self.rightChild)
			return self.rightRotate(node)

		return node

	def getDescendant(node):
		if(node.rightChild):
			return getDescendant(node.rightChild)

		return node 

	def traverse(self):
		if(self.root):
			self.traverseInorder(self.root)


	def traverseInorder(self,node):
		if(node.leftChild):
			self.traverseInorder(node.leftChild)

		print node.data

		if(node.rightChild):
			self.traverseInorder(node.rightChild)




avl = AVL()
avl.input(7)
avl.input(5)
avl.input(6)
avl.input(4)
avl.input(9)
avl.traverse()