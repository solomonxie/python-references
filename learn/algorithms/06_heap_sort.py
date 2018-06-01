"""
Heap sort uses a binary heap data structure to sort elements.
It transforms the input into a max-heap and repeatedly extracts the largest element.
"""

import heapq


def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


if __name__ == "__main__":
    test_arr = [12, 11, 13, 5, 6, 7]
    print(f"Sorted: {heap_sort(test_arr)}")
