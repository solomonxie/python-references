"""
Generators are functions that return an iterator using the 'yield' keyword instead of 'return'.
They allow for lazy evaluation, meaning they generate values on the fly and are highly memory-efficient for processing large streams of data.
"""


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


# Usage
for num in count_up_to(3):
    print(num)
