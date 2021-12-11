import asyncio
import time


async def sleeper() -> None:
    print("Start")
    time.sleep(1)
    print("Stop")


async def main(await_task: bool):
    print("Eric")
    task = asyncio.create_task(sleeper())
    if await_task:
        await task
    print("Rizzi")


asyncio.run(main(await_task=False))
asyncio.run(main(await_task=True))
