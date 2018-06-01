"""
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
It is commonly used for implementing distributed event handling systems or reactive programming.
"""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print(f"Received: {message}")


# Usage
subject = Subject()
obs1 = Observer()
subject.attach(obs1)
subject.notify("Hello Observers!")
