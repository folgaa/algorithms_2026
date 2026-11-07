class Vertex:
    def __init__(self):
        self.label = float('inf')
        self.adj = []

class Graph:
    def __init__(self, v):
        self.v = v

    def ford(self, s):
        len_v = len(self.v)
        self.v[s].label = 0
        for _ in range(len_v - 1):
            for j in range(len_v):
                for k in range(len(self.v[j].adj)):
                    adj_vertex = self.v[j].adj[k][0]
                    weight = self.v[j].adj[k][1]
                    self.v[adj_vertex].label = min(self.v[adj_vertex].label, self.v[j].label + weight)

        for j in range(len_v):
            if self.v[j].label == float('inf'):
                continue
            for adj_vertex, weight in self.v[j].adj:
                if self.v[j].label + weight < self.v[adj_vertex].label:
                    print("Negative cycle!")
                    return

        for i in range(len_v):
            print(i, " -> ", self.v[i].label)



