"""
Finds the Minimum Spanning Tree (MST) of a weighted undirected graph.
It greedily adds the cheapest edge that connects a new vertex to the growing MST.
"""

import heapq


def prims(graph, start_node):
    mst = []
    visited = {start_node}
    edges = [(cost, start_node, to) for to, cost in graph[start_node]]
    heapq.heapify(edges)
    while edges:
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            for next_v, next_cost in graph[v]:
                if next_v not in visited:
                    heapq.heappush(edges, (next_cost, v, next_v))
    return mst
