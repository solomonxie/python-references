"""
Context managers allow you to allocate and release resources precisely when you want to, typically using the 'with' statement.
They are defined using __enter__ and __exit__ methods, ensuring that setup and teardown logic (like closing files) is always executed.
"""


class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")


# Usage
with MyContext():
    print("Inside context")
