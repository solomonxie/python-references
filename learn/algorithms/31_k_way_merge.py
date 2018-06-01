"""
Merges k sorted lists into a single sorted list using a min-heap.
It efficiently handles multiple sorted streams with O(n log k) complexity.
"""

import heapq


def k_way_merge(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    res = []
    while heap:
        val, list_idx, val_idx = heapq.heappop(heap)
        res.append(val)
        if val_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][val_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, val_idx + 1))
    return res
