"""
11. AVL Tree: Self-balancing binary search tree.
It ensures that the height difference between left and right subtrees is at most one.
"""


class Node:
    def __init__(self, key):
        self.key, self.left, self.right, self.height = key, None, None, 1


def get_height(node): return node.height if node else 0


def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
# Simple visualization of height property
print(f"AVL Node {root.key} height: {root.height}")
