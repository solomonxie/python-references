"""
26. ChainMap: Class for creating a single view of multiple mappings.
Useful for managing configuration and scopes.
"""

from collections import ChainMap

# Basic setup: three dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

# Create a ChainMap
cm = ChainMap(dict1, dict2, dict3)
print(f"ChainMap: {cm}")

# Accessing a key will look it up in the dictionaries in order
print(f"a (from dict1): {cm['a']}")
print(f"b (from dict1, shadow dict2): {cm['b']}")
print(f"c (from dict2, shadow dict3): {cm['c']}")
print(f"d (from dict3): {cm['d']}")

# Updates affect only the first mapping (dict1)
cm["e"] = 7
print(f"After setting 'e': {cm}")
print(f"dict1: {dict1}")

# ChainMap as a scope (e.g., local > global > builtin)
local_scope = {"x": 100}
global_scope = {"x": 10, "y": 20}
scope = ChainMap(local_scope, global_scope)
print(f"Scope: {scope}")
print(f"x: {scope['x']}, y: {scope['y']}")
