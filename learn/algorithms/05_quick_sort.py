"""
Quick sort picks an element as a pivot and partitions the array around it.
It is highly efficient for large datasets and is often the default sorting algorithm in libraries.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"Sorted: {quick_sort(test_arr)}")
