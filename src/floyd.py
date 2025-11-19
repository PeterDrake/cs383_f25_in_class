from weighted_digraph import WeightedDigraph
from math import inf

class Floyd:
    def __init__(self, graph):
        v = len(graph.adj)
        self.distances = [[inf] * v for _ in range(v)]
        self.floyd_warshall(graph)

    def floyd_warshall(self, graph):
        # Put 0s along the diagonal
        v = len(graph.adj)
        for i in range(v):
            self.distances[i][i] = 0
        # Put in weights of edges
        for i in range(v):
            for j in graph.adj[i]:
                self.distances[i][j] = graph.adj[i][j]
        # Run the loop to reduce these distances
        for i in range(v):
            for j in range(v):
                for k in range(v):
                    if self.distances[j][i] + self.distances[i][k] < self.distances[j][k]:
                        self.distances[j][k] = self.distances[j][i] + self.distances[i][k]

graph = WeightedDigraph(4)
graph.add_edge(0, 1, 10)
graph.add_edge(1, 2, 20)
graph.add_edge(2, 3, 30)
graph.add_edge(0, 3, 70)
f = Floyd(graph)
print(f.distances)
