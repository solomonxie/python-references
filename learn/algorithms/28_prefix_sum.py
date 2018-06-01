"""
Precomputes cumulative sums of an array to allow O(1) range sum queries.
The sum of elements between indices i and j is prefix[j+1] - prefix[i].
"""


class PrefixSum:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def query(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]
