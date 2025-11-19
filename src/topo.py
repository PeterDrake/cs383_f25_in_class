from digraph import Digraph

def dfs(graph, v, visited=set()):  # TODO The set is only made once!
    result = []
    if v not in visited:
        for w in graph.neighbors(v):
            result += dfs(graph, w, visited)  # TODO Can this be done in constant time?
        result.append(v)
        visited.add(v)
    return result

def topo(graph):
    result = []
    for v in range(len(graph.adj)):
        vertices = dfs(graph, v)
        for w in vertices:
            result.append(w)
    return result[::-1]

g = Digraph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(0, 7)
g.add_edge(1, 7)
g.add_edge(6, 7)

print(topo(g))
