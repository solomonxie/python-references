"""
The Mediator pattern reduces direct dependencies between objects by making them communicate through a mediator object.
This promotes loose coupling by preventing objects from referring to each other explicitly.
"""


class Mediator:
    def notify(self, sender, event): pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self.c1 = component1
        self.c1.mediator = self
        self.c2 = component2
        self.c2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self.c2.do_c()


class Component:
    def __init__(self, mediator=None):
        self.mediator = mediator

    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_c(self):
        print("Component 2 does C.")


# Usage
c1 = Component()
c2 = Component()
mediator = ConcreteMediator(c1, c2)
c1.do_a()
