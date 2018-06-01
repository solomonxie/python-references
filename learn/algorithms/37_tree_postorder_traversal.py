"""
Performs a Postorder traversal (Left-Right-Root) of a binary tree.
It is commonly used for deleting trees or evaluating postfix expressions.
"""


def postorder(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]
