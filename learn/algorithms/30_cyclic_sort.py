"""
Sorts an array in O(n) time when elements are in a known range [1, n].
It works by swapping each element to its correct index until the array is sorted.
"""


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums
