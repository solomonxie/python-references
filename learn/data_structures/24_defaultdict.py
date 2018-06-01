"""
24. Defaultdict: Dictionary subclass that calls a factory function to supply missing values.
Useful for grouping data or avoiding KeyErrors when initializing dictionary values.
"""

from collections import defaultdict

# Grouping items by their first character
words = ["apple", "banana", "cherry", "avocado", "blueberry"]
grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)

print(f"Grouped words: {grouped_words}")

# Use an integer as the default value (starting with 0)
char_count = defaultdict(int)
for char in "hello world":
    char_count[char] += 1

print(f"Character count: {char_count}")

# Accessing a key that doesn't exist
print(f"Default value for 'z': {char_count['z']}")
