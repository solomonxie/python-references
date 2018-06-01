"""
Traverses a tree level by level using a queue for Breadth-First Search.
It processes all nodes at the current depth before moving to the next level.
"""

from collections import deque


def level_order(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
