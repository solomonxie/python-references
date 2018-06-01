"""
The Knuth-Morris-Pratt (KMP) algorithm is a string-searching algorithm that avoids redundant comparisons.
It uses a prefix function (LPS array) to skip characters that have already been matched.
"""


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0

    def compute_lps(p, m, lps):
        length = 0
        i = 1
        while i < m:
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1


if __name__ == "__main__":
    print(f"Pattern found at: {kmp_search(
        'ABABDABACDABABCABAB', 'ABABCABAB')}")
