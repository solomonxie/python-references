"""
Identifies bridges in an undirected graph using Depth First Search.
A bridge is an edge whose removal increases the number of connected components.
"""


def find_bridges(n, adj):
    timer = 0
    tin, low = [-1] * n, [-1] * n
    bridges = []

    def dfs(v, p=-1):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to in adj[v]:
            if to == p:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((v, to))

    for i in range(n):
        if tin[i] == -1:
            dfs(i)
    return bridges
