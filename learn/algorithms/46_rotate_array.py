"""
Rotates an array to the right by k steps in O(n) time and O(1) space.
The algorithm reverses parts of the array to achieve the rotation in-place.
"""


def rotate(nums, k):
    n = len(nums)
    k %= n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums
