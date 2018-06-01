"""
20. Skip List: Probabilistic data structure that allows fast search within an ordered sequence.
It consists of several layers of linked lists, each skipping over some elements.
"""

import random


class SkipNode:
    def __init__(self, key, level):
        self.key, self.forward = key, [None] * (level + 1)


class SkipList:
    def __init__(self, max_level):
        self.max_level, self.header = max_level, SkipNode(-1, max_level)
        self.level = 0

    def insert(self, key):
        new_node = SkipNode(key, random.randint(0, self.max_level))
        curr = self.header
        for i in range(self.max_level, -1, -1):
            while curr.forward[i] and curr.forward[i].key < key:
                curr = curr.forward[i]
            if i <= len(new_node.forward) - 1:
                new_node.forward[i] = curr.forward[i]
                curr.forward[i] = new_node


sl = SkipList(3)
sl.insert(10)
sl.insert(20)
sl.insert(30)
print("Skip List: Inserted 10, 20, 30. First level points to:",
      sl.header.forward[0].key)
