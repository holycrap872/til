import asyncio

"""
Example program that runs three `hello()` functions simultaneously
then those three functions sequentially.

`gather` is used to basically do `create_task` and get the result
for each of the tasks.
"""


# `async` creates a wrapper around the function making it a
# co-routine. In order to execute a co-routine, you need to
# `await` it.
# NB: to use the "await" keyword, though, it has to be inside
# a async function....
async def hello() -> None:
    print("Hello")
    await asyncio.sleep(3)
    print("World")


async def main() -> None:
    await asyncio.gather(hello(), hello(), hello())


if __name__ == "__main__":
    asyncio.run(main())

    # `asyncio.run` basically is a sequential -> asynch adapter
    asyncio.run(hello())
    asyncio.run(hello())
    asyncio.run(hello())

