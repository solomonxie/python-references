"""
The Command pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests and support undoable operations.
It decouples the object that invokes the operation from the one that knows how to perform it.
"""


class Light:
    def on(self): print("Light is ON")


class Command:
    def execute(self): pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


# Usage
light = Light()
command = LightOnCommand(light)
command.execute()
