"""
Type hints provide a way to statically indicate the types of variables, function parameters, and return values.
While not enforced at runtime by Python itself, they improve code clarity and enable powerful static analysis and IDE support.
"""

from typing import List, Dict


def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}


# Usage
result = process_items(["apple", "banana"])
print(result)
