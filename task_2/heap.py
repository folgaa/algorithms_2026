class BinaryHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self, v):
        if v == 0:
            return
        while v != 0:
            p = v // 2
            if self.heap[v][0] > self.heap[p][0]:
                self.heap[v], self.heap[p] = self.heap[p], self.heap[v]
                v = p
            else:
                return

    def sift_down(self, v):
        n = len(self.heap)
        if 2 * v > n:
            return
        while 2 * v < n:
            s = 2 * v
            if 2 * v + 1 < n and self.heap[2 * v + 1][0] > self.heap[s][0]:
                s = 2 * v + 1
            if self.heap[s][0] > self.heap[v][0]:
                self.heap[s], self.heap[v] = self.heap[v], self.heap[s]
                v = s
            else:
                return
            
    def insert(self, elem):
        self.heap.append(elem)
        self.sift_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0] if self.heap else None

    def extract_max(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_elem = self.heap.pop()
        self.sift_down(0)
        return max_elem

    def build_heap(self, arr):
        self.heap = arr
        for i in  range(len(arr) - 1, -1, -1):
            self.sift_down(i)
        

    