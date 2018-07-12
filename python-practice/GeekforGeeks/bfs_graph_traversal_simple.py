class Graph(object):

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)


def BFS(graph, root):

    visited = [False] * len(graph.graph)

    queue = []
    queue.append(root)

    stringer = []

    while queue != []:
        node = queue.pop(0)
        stringer.append(node)
        visited[node] = True
        for i in graph.graph[node]:
            if not visited[i]:
                queue.append(i)

    print(" -> ".join([str(i) for i in stringer]))


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.graph)

BFS(g, 2)