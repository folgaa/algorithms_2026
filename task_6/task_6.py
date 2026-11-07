from graph import Graph, Vertex


def create_graph_from_input():
    n = int(input())
    v = [Vertex() for _ in range(n)]
    vertex, adj_vertex, weight = map(int, input().split())
    while vertex != -1:
        v[vertex].adj.append((adj_vertex, weight))
        vertex, adj_vertex, weight = map(int, input().split())
    g = Graph(v)
    return g

graph = create_graph_from_input()
graph.ford(0)

# 5
# 0 1 6
# 0 2 7
# 1 2 8
# 1 4 5
# 4 1 -2
# 3 4 7
# 2 3 9
# 2 4 -3
# 1 3 -4
# 3 0 2
# -1 0 0