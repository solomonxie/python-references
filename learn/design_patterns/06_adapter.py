"""
The Adapter pattern allows incompatible interfaces to work together by acting as a bridge between them.
It converts the interface of a class into another interface that clients expect, enabling classes to work together that couldn't otherwise.
"""


class OldSystem:
    def legacy_request(self):
        return "Legacy response"


class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.legacy_request()


# Usage
adapter = Adapter(OldSystem())
print(adapter.request())
