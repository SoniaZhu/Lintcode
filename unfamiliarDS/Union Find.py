class DSU:

    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.size = [0 for _ in range(N+1)]

    def find(self, x):
        if x != self.parent[x]:
            # Path Compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] > self.size[root_y]:
            self.size[root_x] += self.size[root_y]
            self.parent[root_y] = root_x
        else:
            self.size[root_y] += self.size[root_x]
            self.parent[root_x] = root_y


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(N = len(edges))
        for edge in edges:
            u, v = edge[0], edge[1]
            if dsu.find(u) == dsu.find(v):
                return edge
            else:
                dsu.union(u, v)
