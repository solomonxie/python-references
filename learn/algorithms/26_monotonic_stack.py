"""
Maintains elements in increasing or decreasing order using a stack.
This pattern is used to find the next greater or smaller element in O(n) time.
"""


def next_greater_element(nums):
    res = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res
