"""
Bubble sort repeatedly swaps adjacent elements if they are in the wrong order.
It is one of the simplest sorting algorithms, though not very efficient for large datasets.
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Sorted: {bubble_sort(test_arr)}")
