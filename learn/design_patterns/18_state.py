"""
The State pattern allows an object to alter its behavior when its internal state changes.
The object will appear to change its class, providing a clean way to manage state-dependent logic.
"""


class State:
    def handle(self): pass


class StateA(State):
    def handle(self): return "State A handling"


class StateB(State):
    def handle(self): return "State B handling"


class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        return self.state.handle()


# Usage
ctx = Context(StateA())
print(ctx.request())
ctx.state = StateB()
print(ctx.request())
