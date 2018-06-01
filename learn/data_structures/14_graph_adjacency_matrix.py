"""
14. Graph (Adjacency Matrix): Collection of nodes with edges stored in a 2D array.
A cell (i, j) is 1 if there is an edge between vertex i and vertex j, else 0.
"""

# Representing a 3-node graph (0, 1, 2) with edges (0,1) and (1,2)
matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

print("Graph (Adjacency Matrix):")
for row in matrix:
    print(row)
