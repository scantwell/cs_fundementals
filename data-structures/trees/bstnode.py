class BSTNode(object):
	def __init__(self, left, right, value):
		self.lchild = left
		self.rchild = right
		self.value = value

	def add(self, value):
		if value > self.value:
			if self.rchild is None:
				self.rchild = BSTNode(None, None, value)
				return True
			else:
				self.rchild.add(value)
		elif value < self.value:
			if self.lchild is None:
				self.lchild = BSTNode(None,None,value)
				return True
			else:	
				self.lchild.add(value)
		else:
			return False

	def find(self, value):
		if value == self.value:
			return True
		elif value < self.value:
			if self.lchild == None:
				return False
			else:
				return self.lchild.find(value)
		elif value > self.value:
			if self.rchild == None:
				return False
			else:
				return self.rchild.find(value)
		else:
			return False
