"""
Common bit manipulation tricks for setting, clearing, and toggling bits.
These operations are fundamental for low-level optimizations and bitmasking.
"""


def bit_tricks(n):
    set_bit = n | (1 << 0)
    clear_bit = n & ~(1 << 0)
    toggle_bit = n ^ (1 << 0)
    is_power_of_two = n > 0 and (n & (n - 1)) == 0
    return set_bit, clear_bit, toggle_bit, is_power_of_two
