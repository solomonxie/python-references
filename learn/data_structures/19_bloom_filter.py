"""
19. Bloom Filter: Space-efficient probabilistic data structure.
It is used to test whether an element is a member of a set, allowing false positives but not false negatives.
"""

import hashlib


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size, self.hash_count = size, hash_count
        self.bit_array = [0] * size

    def add(self, item):
        for i in range(self.hash_count):
            index = int(hashlib.md5((item + str(i)).encode()
                                    ).hexdigest(), 16) % self.size
            self.bit_array[index] = 1

    def is_present(self, item):
        for i in range(self.hash_count):
            index = int(hashlib.md5((item + str(i)).encode()
                                    ).hexdigest(), 16) % self.size
            if self.bit_array[index] == 0:
                return False
        return True


bf = BloomFilter(100, 3)
bf.add("test")
print(f"Is 'test' present? {bf.is_present('test')}")
print(f"Is 'other' present? {bf.is_present('other')}")
