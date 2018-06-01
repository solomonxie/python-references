"""
The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
It is useful when an object requires many optional parameters and a stepwise initialization.
"""


class Computer:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        return f"Computer with: {', '.join(self.parts)}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self):
        self.computer.add("CPU")
        return self

    def add_memory(self):
        self.computer.add("Memory")
        return self

    def add_gpu(self):
        self.computer.add("GPU")
        return self

    def build(self):
        return self.computer


# Usage
builder = ComputerBuilder()
computer = builder.add_cpu().add_memory().add_gpu().build()
print(computer)
