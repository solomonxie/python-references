"""
The Floyd-Warshall algorithm finds the shortest paths between all pairs of nodes in a weighted graph.
It works by iteratively considering each node as an intermediate step for all pairs of other nodes.
"""


def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


if __name__ == "__main__":
    edges = [(0, 1, 5), (1, 2, 3), (0, 2, 10)]
    print(f"Matrix: {floyd_warshall(edges, 3)}")
