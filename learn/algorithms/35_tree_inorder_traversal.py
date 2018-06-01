"""
Performs an Inorder traversal (Left-Root-Right) of a binary tree.
In a Binary Search Tree, this traversal visits nodes in ascending order.
"""


def inorder(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res
