"""
The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.
It uses composition instead of inheritance to separate responsibility into different class hierarchies.
"""


class Device:
    def turn_on(self): pass


class TV(Device):
    def turn_on(self): return "TV is ON"


class Radio(Device):
    def turn_on(self): return "Radio is ON"


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def press_power(self):
        return self.device.turn_on()


# Usage
tv_remote = RemoteControl(TV())
radio_remote = RemoteControl(Radio())
print(tv_remote.press_power())
print(radio_remote.press_power())
