"""
09. Binary Tree: Hierarchical structure where each node has at most two children.
It consists of a root node and left and right subtrees.
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(f"Root: {root.val}, Left: {root.left.val}, Right: {root.right.val}")
