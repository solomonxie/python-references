"""
Efficiently calculates hash values for sliding windows in a string.
This technique is used in the Rabin-Karp algorithm for fast pattern matching.
"""


def rolling_hash(s, window_size):
    base, mod = 31, 10**9 + 7
    h, p = 0, 1
    for i in range(window_size):
        h = (h * base + ord(s[i])) % mod
        if i > 0:
            p = (p * base) % mod
    res = [h]
    for i in range(window_size, len(s)):
        h = (h - ord(s[i - window_size]) * p) % mod
        h = (h * base + ord(s[i])) % mod
        res.append(h)
    return res
