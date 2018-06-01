"""
Breadth-First Search (BFS) explores all neighbors at the present depth before moving to the next level.
It uses a queue to keep track of nodes to be visited and is ideal for finding shortest paths in unweighted graphs.
"""

from collections import deque


def bfs(graph, start):
    visited, queue = {start}, deque([start])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'],
             'C': ['F'], 'D': [], 'E': [], 'F': []}
    print(f"BFS: {bfs(graph, 'A')}")
