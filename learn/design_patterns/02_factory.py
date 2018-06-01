"""
The Factory pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
This pattern decouples the client code from the concrete classes it needs to instantiate, promoting flexibility and scalability.
"""


class Dog:
    def speak(self): return "Woof!"


class Cat:
    def speak(self): return "Meow!"


def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()


# Usage
animal = animal_factory("dog")
print(animal.speak())
