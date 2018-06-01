"""
Finds the longest palindromic substring in an input string in O(n) time.
It uses symmetry and previously calculated palindrome lengths to avoid redundant work.
"""


def manachers(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(n):
        mirr = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirr])
        while i + 1 + p[i] < n and i - 1 - p[i] >= 0 and t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    max_len, center_idx = max((val, idx) for idx, val in enumerate(p))
    return s[(center_idx - max_len) // 2: (center_idx + max_len) // 2]
