from math import inf
from heapq import heappush, heappop

class Dijkstra:
    def __init__(self, g, start):
        self.distances = [inf] * len(g.adj)  # One per vertex
        self.dijkstra(g, start)

    def dijkstra(self, g, start):
        pq = []  # Priority queue
        self.distances[start] = 0
        heappush(pq, (0, start))
        while pq:
            (_, v) = heappop(pq)
            for w in g.adj[v]:
                if self.distances[v] + self.adj[v][w] < self.distances[w]:
                    self.distances[w] = self.distances[v] + self.adj[v][w]
                    heappush(pq, (self.distances[w], w))
