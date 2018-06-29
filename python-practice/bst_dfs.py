class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def BFSBinary(root, seach_item):
	stack = [root]
	counter = len(stack)

	while len(stack) > 0:

		if stack[0] == search_item:
			return True
		else:
			next_level = False
			node = stack.pop(0)
			if node.right:
				stack.insert(0, node.right)
				next_level = True
			if node.left:
				stack.insert(0, node.left)
				next_level = True
		if next_level:
			counter += 1

	return False



# def reverse(txt):

# 	if len(txt) <= 1:
# 		return txt
# 	else:
# 		return reverse(txt[1:]) + reverse(txt[0])
