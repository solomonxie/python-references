"""
The Fast and Slow Pointers pattern (also known as Floyd's cycle-finding algorithm) uses two pointers moving at different speeds.
It is primarily used to detect cycles in linked lists or other sequences.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    head.next.next.next = head.next  # Cycle
    print(f"Has cycle: {has_cycle(head)}")
