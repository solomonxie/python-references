"""
Maintains the median of a data stream using a min-heap and a max-heap.
The max-heap stores the smaller half and the min-heap stores the larger half.
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap
        self.large = []  # min-heap

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
