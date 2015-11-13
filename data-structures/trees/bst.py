#! /usr/bin/python
# Binary Search Tree implementation
from bstnode import BSTNode
from random import randint


class BST(BSTNode):

	def __init__(self):
		super(BST, self).__init__(None, None, None)

	def add(self, value):
		if self.value == None:
			self.value = value
		else:
			super(BST, self).add(value)

# TRAVERSALS

def preorder(tree):
	if tree == None:
		return
	print tree.value
	preorder(tree.lchild)
	preorder(tree.rchild)	

def inorder(tree):
	if tree == None:
		return
	inorder(tree.lchild)
	print tree.value
	inorder(tree.rchild)

def postorder(tree):
	if tree == None:
		return
	postorder(tree.lchild)
	postorder(tree.rchild)
	print tree.value

if __name__ == '__main__':
	bst = BST()
	for i in [4, 10, 3, 2, 6, 20, 100]: #range(0, 1000):
		bst.add(i)
	#preorder(bst)
	#inorder(bst)
	postorder(bst)
	for i in [4, 10, 3, 2, 6, 20, 100]: #range(0, 1000):
		print bst.find(i)
	print bst.find(10)	
