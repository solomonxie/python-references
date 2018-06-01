"""
17. Fenwick Tree: Efficiently updates elements and calculates prefix sums.
Also known as a Binary Indexed Tree (BIT).
"""


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s, i = 0, i + 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


ft = FenwickTree(10)
ft.update(3, 5)
print(f"Fenwick Tree query up to index 3: {ft.query(3)}")
