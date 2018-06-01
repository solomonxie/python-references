"""
15. Disjoint Set (Union-Find): Keeps track of elements partitioned into disjoint sets.
It provides operations to find which set an element belongs to and to union two sets.
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


ds = DisjointSet(5)
ds.union(0, 2)
ds.union(4, 2)
print(f"Parent array after unions: {ds.parent}")
print(f"Is 0 connected to 4? {ds.find(0) == ds.find(4)}")
