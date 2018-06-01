"""
Topological Sort orders the vertices of a directed acyclic graph (DAG) such that for every edge uv, u comes before v.
Kahn's algorithm uses in-degrees and a queue to produce this linear ordering.
"""

from collections import deque


def topological_sort(nodes, edges):
    in_degree = {u: 0 for u in nodes}
    graph = {u: [] for u in nodes}
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([u for u in nodes if in_degree[u] == 0])
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return result if len(result) == len(nodes) else None


if __name__ == "__main__":
    print(f"Order: {topological_sort(['A', 'B', 'C', 'D'], [
          ('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'D')])}")
