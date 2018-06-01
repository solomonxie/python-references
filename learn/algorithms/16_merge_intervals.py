"""
Merge Intervals is a technique used to combine overlapping ranges into a single continuous range.
It is essential for scheduling problems and handling intervals in various data processing tasks.
"""


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged


if __name__ == "__main__":
    print(f"Merged: {merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])}")
