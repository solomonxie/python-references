"""
The Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
It decouples the traversal logic from the collection itself.
"""


class AlphabeticalIterator:
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()


# Usage
items = ["A", "B", "C"]
it = AlphabeticalIterator(items)
print(next(it))
print(next(it))
