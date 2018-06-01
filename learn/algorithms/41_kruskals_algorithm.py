"""
Finds the Minimum Spanning Tree (MST) using the Union-Find data structure.
It sorts all edges by weight and adds them if they don't form a cycle.
"""


def kruskals(n, edges):
    parent = list(range(n))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    edges.sort(key=lambda x: x[2])
    mst, count = [], 0
    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
            count += 1
            if count == n - 1:
                break
    return mst
