"""
Finds the lowest common ancestor (LCA) in a Binary Search Tree.
It leverages the BST property to navigate towards the ancestor efficiently.
"""


def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
