"""
Binary search finds the position of a target value within a sorted array.
It compares the target value to the middle element and halves the search space in each step.
"""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    test_arr = [2, 3, 4, 10, 40]
    print(f"Index: {binary_search(test_arr, 10)}")
