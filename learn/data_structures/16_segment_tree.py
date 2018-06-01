"""
16. Segment Tree: Tree used for storing information about intervals or segments.
It allows for efficient range queries (e.g., sum, min, max) and point updates.
"""


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r):
        res, l, r = 0, l + self.n, r + self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


st = SegmentTree([1, 2, 3, 4])
print(f"Segment Tree sum range [1, 3): {st.query(1, 3)}")  # elements 2 and 3
