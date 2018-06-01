"""
Finds the lowest common ancestor (LCA) of two nodes in a binary tree.
The LCA is the deepest node that is an ancestor to both given nodes.
"""


def find_lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right
