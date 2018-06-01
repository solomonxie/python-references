"""
05. Queue: FIFO (First-In, First-Out) data structure.
Elements are added at the rear and removed from the front.
"""

from collections import deque

queue = deque(["Alice", "Bob", "Charlie"])
print(f"Queue: {list(queue)}")
queue.append("David")
print(f"Enqueued: David -> {list(queue)}")
print(f"Dequeued: {queue.popleft()}")
print(f"Queue after dequeue: {list(queue)}")
