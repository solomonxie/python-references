"""
Finds the top k most frequent or largest elements using a heap.
This approach is more efficient than sorting the entire list when k is small.
"""

import heapq
from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
