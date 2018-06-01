"""
Depth-First Search (DFS) explores as far as possible along each branch before backtracking.
It uses a stack (or recursion) to explore the graph and is useful for detecting cycles and topological sorting.
"""


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    result = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result


if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'],
             'C': ['F'], 'D': [], 'E': [], 'F': []}
    print(f"DFS: {dfs(graph, 'A')}")
