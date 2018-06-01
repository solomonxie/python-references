"""
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
It is useful when exactly one object is needed to coordinate actions across the system, such as a database connection or a configuration manager.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Usage
s1 = Singleton()
s2 = Singleton()
print(f"Are they the same instance? {s1 is s2}")
