"""
04. Stack: LIFO (Last-In, First-Out) data structure.
Elements are added and removed from the same end, typically called the top.
"""

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(f"Stack: {stack}")
print(f"Popped: {stack.pop()}")
print(f"Stack after pop: {stack}")
