"""
Selection sort divides the list into a sorted and an unsorted part.
It repeatedly selects the smallest element from the unsorted part and moves it to the sorted part.
"""


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    test_arr = [64, 25, 12, 22, 11]
    print(f"Sorted: {selection_sort(test_arr)}")
