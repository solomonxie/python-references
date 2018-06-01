"""
Backtracking is a refined brute-force approach that builds a solution incrementally and removes those that fail to satisfy constraints.
It is widely used for combinatorial problems like generating permutations or solving the N-Queens puzzle.
"""


def permutations(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        m = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in permutations(remaining):
            result.append([m] + p)
    return result


if __name__ == "__main__":
    print(f"Permutations: {permutations([1, 2, 3])}")
