"""
13. Graph (Adjacency List): Collection of nodes with edges stored as lists.
Each node (or vertex) has a list of all other nodes it is connected to.
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Graph (Adjacency List):")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
