from heap import BinaryHeap


class Relevance:
    def __init__(self, n, a, d, f):
        self.a = a # параметры
        self.f = f # признаки объектов
        self.relevance = [sum(a[j] * f[i][j] for j in range(n)) for i in range(d)]
        self.rel_heap = BinaryHeap()
        self.rel_heap.build_heap([(self.relevance[i], i) for i in range(d)])

    def update(self, i, j, v):
        self.relevance[i] += self.a[j] * (v - self.f[i][j])
        self.f[i][j] = v
        self.rel_heap.insert((self.relevance[i], i))

    def top(self, k):
        result = []
        while len(result) < k:
            rel, ind = self.rel_heap.extract_max()
            if rel == self.relevance[ind]:
                result.append((rel, ind))
        for val in result:
            self.rel_heap.insert(val)
        return result

