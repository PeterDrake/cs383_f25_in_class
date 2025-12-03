from digraph import Digraph

def topo(graph):
    result = []
    visited = set()
    def dfs(v):
        if v not in visited:
            visited.add(v)
            for w in graph.neighbors(v):
                dfs(w)
            result.append(v)
    for vertex in range(len(graph.adj)):
        dfs(vertex)
    return result[::-1]

if __name__ == '__main__':
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
    print(topo(g))

# def f(x=None):
#     if x is None:
#         x = []
#     x.append('!')
#     return x
#
# print(f())
# print(f())
# print(f([1, 2, 3]))
