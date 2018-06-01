"""
07. Priority Queue: Elements are served based on priority.
This is commonly implemented using a heap, where the highest priority element is at the root.
"""

import heapq

pq = []
# heapq implements a min-heap by default
heapq.heappush(pq, (2, "Task 2"))
heapq.heappush(pq, (1, "Task 1"))
heapq.heappush(pq, (3, "Task 3"))

print(f"Priority Queue: {pq}")
print(f"Popping highest priority (lowest number): {heapq.heappop(pq)}")
