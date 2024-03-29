import asyncio
from asyncio.events import AbstractEventLoop
import enum
import typing


class JobType(enum.Enum):
    _MUTATE = 0
    _SCORE = 1
    _PREP = 2
    _EXPLOIT = 3
    _VERIFY = 4


class Job(typing.NamedTuple):
    """
    :param kind: Type of analysis to do with this job
    :param orig_state: The state that is being analyzed
    :param check_state: A state that comes from orig_state
        ex. State after following a link or fuzzing the URL
    """
    kind: JobType
    orig_state: str


async def do_job(job_str: str) -> None:
    print(f"Waiting on {job_str}")
    await asyncio.sleep(1)


async def do_prep(work_loop: AbstractEventLoop, job: Job) -> None:
    for i in range(0, 4):
        new_job = Job(JobType._EXPLOIT, job.orig_state + f", prep_{i}")
        await do_job(f"prep_{i}")
        work_loop.create_task(do_exploit(work_loop, new_job))


async def do_exploit(work_loop: AbstractEventLoop, job: Job) -> None:
    for i in range(0, 4):
        new_job = Job(JobType._VERIFY, job.orig_state + f", exploit_{i}")
        await do_job(f"exploit_{i}")
        work_loop.create_task(do_verify(work_loop, new_job))


async def do_verify(work_loop: AbstractEventLoop, job: Job) -> None:
    await do_job(job.orig_state + ", verify")


async def main():
    loop = asyncio.get_event_loop()

    current_tasks = asyncio.Task.all_tasks()
    assert len(current_tasks) == 1
    main_task = list(current_tasks)[0]
    
    loop.create_task(do_prep(loop, Job(JobType._PREP, "start")))

    while True:
        pending = [task for task in asyncio.Task.all_tasks() if task != main_task and not task.done()]
        if not pending:
            break
        await asyncio.gather(*pending)


asyncio.run(main())
