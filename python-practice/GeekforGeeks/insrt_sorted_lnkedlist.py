class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		return str(self.val)

class LinkedList(object):
	def __init__(self):
		self.root = None
		self.last = None
		self.size = 0

	def add_node(self, node):
		if self.root is None:
			self.root = node
		else:
			current_node = self.root
			previous_node = None

			stop = False

			while current_node and not stop:
				if current_node.val < node.val:
					if not current_node.next:
						current_node.next = node
						stop = True
					else:
						previous_node = current_node
						current_node = current_node.next
				elif current_node.val >= node.val:
					node.next = current_node
					if previous_node:
						previous_node.next = node
					else:
						self.root = node
					stop=True
		
		return self.root

	def __str__(self):
		if not self.root:
			return None

		temp = []

		node = self.root
		
		while node:
			temp.append(node.val)
			node = node.next

		return "->".join([str(x) for x in temp])

mylist = LinkedList()
new_node = Node(17)
mylist.add_node(new_node)
mylist.add_node(Node(15))
mylist.add_node(Node(21))
mylist.add_node(Node(19))
mylist.add_node(Node(16))
print(str(mylist))
