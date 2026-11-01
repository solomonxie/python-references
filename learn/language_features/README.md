# Python Language Features

A collection of key Python language features and concepts, demonstrating modern Python capabilities from basic syntax to advanced metaprogramming and concurrency.

## Core Language Features
Fundamental tools and syntax for writing efficient Python code.

- [Comprehensions](./01_comprehensions.py) - Concise syntax for creating lists, sets, and dictionaries.
- [Context Managers](./02_context_managers.py) - Resource management using the `with` statement and `__enter__`/`__exit__`.
- [Decorators](./03_decorators.py) - Functions that modify the behavior of another function or class.
- [Generators](./04_generators.py) - Memory-efficient iterators using the `yield` keyword for lazy evaluation.
- [Typing Hints](./09_typing_hints.py) - Static type annotations for improved code clarity and tool support.

## Concurrency & Parallelism
Techniques for executing multiple tasks efficiently.

- [GIL](./05_gil.py) - Demonstrates how the Global Interpreter Lock stops threads from scaling CPU-bound work.
- [Threading & Multiprocessing](./06_threading_and_multiprocessing.py) - OS threads for I/O-bound concurrency (with `Lock` to avoid race conditions) vs. processes for true parallelism.
- [Asyncio](./07_asyncio.py) - Single-threaded concurrent code using `async`/`await` coroutines.

## Advanced Concepts
Deep-level Python features for framework development and metaprogramming.

- [Metaclasses](./08_metaclasses.py) - The "classes of classes," allowing for custom class creation logic.
