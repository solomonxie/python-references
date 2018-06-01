"""
Counts the number of set bits (1s) in an integer's binary representation.
Brian Kernighan's algorithm does this efficiently by clearing the least significant bit.
"""


def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
