"""
The Memento pattern captures and externalizes an object's internal state without violating encapsulation, so that the object can be restored to this state later.
It is commonly used for implementing undo mechanisms.
"""


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self, state):
        self._state = state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()


# Usage
orig = Originator("Initial State")
saved = orig.save()
orig._state = "Changed State"
print(f"Current State: {orig._state}")
orig.restore(saved)
print(f"Restored State: {orig._state}")
