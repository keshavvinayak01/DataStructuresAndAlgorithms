#every node of the tree
class Node(object):

	def __init__(self,data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

#the binary tree class
class BinarySearchTree(object):

	def __init__(self):
		self.root = None

#function to insert object according to binary search algorithm
	def insert(self,data):

		if(self.root == None):
			self.root = Node(data)
		else:
			self.insertNode(data,self.root)
#recursive function in continuation 
	def insertNode(self,data,node):

		if(data < node.data):
			if(node.leftChild):
				self.insertNode(data,node.leftChild)
			else:
				node.leftChild = Node(data)

		if(data > node.data):
			if(node.rightChild):
				self.insertNode(data,node.rightChild)
			else:
				node.rightChild = Node(data)
		


#function to display all the elements of BST in Order type traversal
	def traverse(self):
		if(self.root):
			self.traverseInOrder(self.root)
#recursive function to aid traversal
	def traverseInOrder(self,node):
		if(node.leftChild):
			self.traverseInOrder(node.leftChild)

		print (node.data)
		
		if(node.rightChild):
			self.traverseInOrder(node.rightChild)

#function call to delete the selected node
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

		return node
#function to get the largest child in the left subtree of node to be deletedn
	def getDescendant(self,node):
		if(node.rightChild):
			return self.getDescendant(node.rightChild)
		return node



bst = BinarySearchTree()
bst.insert(5)
bst.insert(1)
bst.insert(2)
bst.insert(6)
bst.insert(7)
bst.traverse()
bst.delete(5)
bst.traverse()