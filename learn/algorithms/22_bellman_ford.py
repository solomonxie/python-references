"""
Bellman-Ford algorithm finds the shortest path from a source to all vertices in a graph that may have negative edge weights.
It also detects negative cycles by checking if any distance can be further reduced after n-1 iterations.
"""


def bellman_ford(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "Negative cycle detected"
    return dist


if __name__ == "__main__":
    edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
             (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    print(f"Distances: {bellman_ford(edges, 5, 0)}")
