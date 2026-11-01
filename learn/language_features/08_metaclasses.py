"""
Metaclasses are the 'classes of classes', defining how classes themselves are created and behave.
They allow for deep customization of class creation, such as automatically registering subclasses or enforcing API constraints at class definition time.
"""


class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Meta):
    pass


# Usage
obj = MyClass()
