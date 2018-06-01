"""
Union-Find (or Disjoint Set Union) is a data structure that tracks elements partitioned into disjoint sets.
It provides efficient operations for merging sets (Union) and finding the representative of a set (Find).
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 2)
    uf.union(4, 2)
    uf.union(3, 1)
    print(f"Find(0): {uf.find(0)}, Find(4): {uf.find(4)}")
