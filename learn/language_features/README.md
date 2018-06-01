# Python Language Features

A collection of key Python language features and concepts, demonstrating modern Python capabilities from basic syntax to advanced metaprogramming and concurrency.

## Core Language Features
Fundamental tools and syntax for writing efficient Python code.

- [Comprehensions](./01_comprehensions.py) - Concise syntax for creating lists, sets, and dictionaries.
- [Context Managers](./02_context_managers.py) - Resource management using the `with` statement and `__enter__`/`__exit__`.
- [Decorators](./03_decorators.py) - Functions that modify the behavior of another function or class.
- [Generators](./04_generators.py) - Memory-efficient iterators using the `yield` keyword for lazy evaluation.
- [Typing Hints](./08_typing_hints.py) - Static type annotations for improved code clarity and tool support.

## Concurrency & Parallelism
Techniques for executing multiple tasks efficiently.

- [GIL & Multiprocessing](./05_gil_and_multiprocessing.py) - Understanding the Global Interpreter Lock and bypassing it with processes.
- [Asyncio](./06_asyncio.py) - Single-threaded concurrent code using `async`/`await` coroutines.

## Advanced Concepts
Deep-level Python features for framework development and metaprogramming.

- [Metaclasses](./07_metaclasses.py) - The "classes of classes," allowing for custom class creation logic.
