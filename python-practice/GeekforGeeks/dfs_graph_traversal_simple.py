class Graph(object):

	def __init__(self):
		self.nodes = {}

	def add_edge(self, from_node, to_node):
		self.nodes.setdefault(from_node, []).append(to_node)


def DFS(graph, root):
	
	visited = [False] * len(graph.nodes)

	stack = []
	stack.append(root)

	while stack != []:
		current_node = stack.pop()
		print('{}, '.format(current_node))
		visited[current_node] = True
		for i in range(1, len(graph.nodes[current_node])+1):
			item = graph.nodes[current_node][-1*i]
			if not visited[item]:
				stack.append(item)

	return 


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.nodes)

DFS(g, 2)