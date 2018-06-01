"""
21. Deque (Double-Ended Queue): Fast appends and pops from both ends.
Useful for stacks, queues, and sliding window problems.
Time complexity: O(1) for appends and pops from both ends.
"""

from collections import deque

# Create a deque
d = deque([1, 2, 3])
print(f"Original deque: {d}")

# Append and pop from the right (standard queue/stack behavior)
d.append(4)
print(f"After appending 4: {d}")
d.pop()
print(f"After popping from right: {d}")

# Append and pop from the left
d.appendleft(0)
print(f"After appending 0 to the left: {d}")
d.popleft()
print(f"After popping from left: {d}")

# Rotate deque (n > 0: right rotation, n < 0: left rotation)
d.rotate(1)
print(f"After rotating right by 1: {d}")
d.rotate(-1)
print(f"After rotating left by 1: {d}")
