"""
Performs a Preorder traversal (Root-Left-Right) of a binary tree.
This traversal is often used to create a copy of the tree or for prefix notation.
"""


def preorder(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
