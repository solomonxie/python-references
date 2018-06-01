"""
The Boyer-Moore Voting Algorithm is an efficient way to find the majority element in a sequence.
It works in O(n) time and O(1) space by maintaining a candidate and a counter.
"""


def majority_element(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate


if __name__ == "__main__":
    print(f"Majority: {majority_element([2, 2, 1, 1, 1, 2, 2])}")
