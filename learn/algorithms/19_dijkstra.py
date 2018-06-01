"""
Dijkstra's algorithm finds the shortest path from a starting node to all other nodes in a weighted graph with non-negative edges.
It uses a priority queue to greedily expand the closest unvisited node.
"""

import heapq


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


if __name__ == "__main__":
    graph = {'A': {'B': 1, 'C': 4}, 'B': {
        'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}
    print(f"Distances: {dijkstra(graph, 'A')}")
