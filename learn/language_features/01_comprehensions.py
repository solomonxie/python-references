"""
Comprehensions provide a concise way to create lists, sets, and dictionaries in Python.
They are often more readable and efficient than using traditional loops for basic data processing and transformation.
"""

# List comprehension
squares = [x*x for x in range(5)]
# Set comprehension
unique_squares = {x*x for x in [-2, -1, 0, 1, 2]}
# Dictionary comprehension
square_dict = {x: x*x for x in range(3)}

print(f"List: {squares}")
print(f"Set: {unique_squares}")
print(f"Dict: {square_dict}")
