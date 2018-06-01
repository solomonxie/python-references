"""
The Template Method pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
It lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
"""


class AbstractClass:
    def template_method(self):
        self.step1()
        self.step2()

    def step1(self): pass
    def step2(self): pass


class ConcreteClass(AbstractClass):
    def step1(self): print("Step 1 executed")
    def step2(self): print("Step 2 executed")


# Usage
obj = ConcreteClass()
obj.template_method()
