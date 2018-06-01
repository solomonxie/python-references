# Design Patterns in Python

A comprehensive collection of 20 common design patterns implemented in Python, illustrating various architectural solutions for software design. Patterns are categorized into Creational, Structural, and Behavioral groups.

## Creational Patterns
These patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

- [Singleton](./01_singleton.py) - Ensures that a class has only one instance and provides a global point of access to it.
- [Factory](./02_factory.py) - Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
- [Builder](./07_builder.py) - Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
- [Prototype](./08_prototype.py) - Creates new objects by copying an existing instance, also known as a prototype.

## Structural Patterns
These patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

- [Decorator](./05_decorator.py) - Allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.
- [Adapter](./06_adapter.py) - Allows incompatible interfaces to work together by acting as a bridge between them.
- [Bridge](./09_bridge.py) - Decouples an abstraction from its implementation so that the two can vary independently.
- [Composite](./10_composite.py) - Allows you to compose objects into tree structures to represent part-whole hierarchies.
- [Facade](./11_facade.py) - Provides a simplified interface to a larger body of code, such as a class library.
- [Flyweight](./12_flyweight.py) - Minimizes memory usage by sharing as much data as possible with similar objects.
- [Proxy](./13_proxy.py) - Provides a surrogate or placeholder for another object to control access to it.

## Behavioral Patterns
These patterns are concerned with algorithms and the assignment of responsibilities between objects.

- [Strategy](./03_strategy.py) - Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- [Observer](./04_observer.py) - Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- [Command](./14_command.py) - Encapsulates a request as an object, allowing for parameterization of clients and support for undoable operations.
- [Iterator](./15_iterator.py) - Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- [Mediator](./16_mediator.py) - Reduces direct dependencies between objects by making them communicate through a mediator object.
- [Memento](./17_memento.py) - Captures and externalizes an object's internal state so it can be restored to this state later.
- [State](./18_state.py) - Allows an object to alter its behavior when its internal state changes.
- [Template Method](./19_template_method.py) - Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
- [Visitor](./20_visitor.py) - Represents an operation to be performed on the elements of an object structure without changing the classes of the elements.
