"""
The Sliding Window pattern involves maintaining a sub-segment of data as it moves through a larger collection.
It is commonly used to find subarrays or substrings that satisfy specific conditions, like the maximum sum of k consecutive elements.
"""


def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == "__main__":
    print(f"Max Sum: {max_sum_subarray([2, 1, 5, 1, 3, 2], 3)}")
