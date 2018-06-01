"""
18. LRU Cache: Least Recently Used cache implementation.
It discards the least recently used items first when the cache reaches its capacity.
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(f"Get 1: {lru.get(1)}")
lru.put(3, 3)
print(f"Get 2 (should be -1): {lru.get(2)}")
