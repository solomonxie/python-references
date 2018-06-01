"""
Finds the kth smallest or largest element in an unordered list.
It uses a partitioning logic similar to quicksort to achieve average O(n) time.
"""

import random


def quickselect(nums, k):
    if not nums:
        return None
    pivot = random.choice(nums)
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))
