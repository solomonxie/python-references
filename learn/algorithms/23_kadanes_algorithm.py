"""
Kadane's algorithm is used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
It is an O(n) approach that maintains the maximum sum ending at the current position.
"""


def kadane(arr):
    max_so_far = arr[0]
    current_max = arr[0]
    for x in arr[1:]:
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)
    return max_so_far


if __name__ == "__main__":
    print(f"Max Subarray Sum: {kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")
