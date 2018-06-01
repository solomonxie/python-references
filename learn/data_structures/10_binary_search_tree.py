"""
10. Binary Search Tree (BST): Binary tree where left < parent < right.
This property allows for efficient searching, insertion, and deletion.
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for k in keys:
    root = insert(root, k)

print(f"BST Root: {root.key}, Left: {root.left.key}, Right: {root.right.key}")
