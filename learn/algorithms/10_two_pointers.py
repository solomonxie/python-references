"""
The Two Pointers pattern uses two indices to traverse a data structure, often from both ends.
It is highly effective for solving problems related to sorted arrays or linked lists, such as finding a pair with a specific sum.
"""


def pair_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


if __name__ == "__main__":
    print(f"Pair: {pair_sum([1, 2, 3, 4, 6], 6)}")
