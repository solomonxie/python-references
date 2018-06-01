"""
Maintains elements in a sliding window in a monotonic order.
This allows finding the maximum or minimum element in a window in O(1) time.
"""

from collections import deque


def max_sliding_window(nums, k):
    dq = deque()
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
