from digraph import Digraph
from topo import topo

def transpose(graph):
    n = len(graph.adj)
    result = Digraph(n)
    for v in range(n):
        for w in graph.adj[v]:
            result.add_edge(w, v)
    return result

def kosaraju(graph):
    order = topo(graph)
    t = transpose(graph)
    component = []
    visited = set()
    def dfs(v):
        if v not in visited:
            visited.add(v)
            for w in t.neighbors(v):
                dfs(w)
            component.append(v)
    final_result = []
    for v in order:
        if v not in visited:
            component = []
            dfs(v)
            final_result.append(component)
    return final_result

g = Digraph(8)
edges = ((0, 1), (1, 2), (2, 3), (3, 2), (3, 7), (2, 6), (1, 5), (1, 4), (4, 0), (4, 5), (5, 6), (6, 5), (6, 7), (7, 7))
for v, w in edges:
    g.add_edge(v, w)
print(kosaraju(g))
