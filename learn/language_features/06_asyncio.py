"""
asyncio is a library to write concurrent code using the async/await syntax.
It provides a single-threaded event loop that manages tasks, allowing for efficient I/O-bound concurrency without the overhead of threads.
"""

import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print("Start")
    await say_after(0.1, "World")
    print("End")

if __name__ == "__main__":
    asyncio.run(main())
