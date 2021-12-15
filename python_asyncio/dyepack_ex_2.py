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


class BrowserView:
    def __init__(self, sempahore: asyncio.Semaphore, url: str) -> None:
        self.semaphore = sempahore
        self.url = url

    async def load_url(self) -> None:
        async with self.semaphore:
            print(f"Getting {self.url}")
            await asyncio.sleep(6)
            print(f"Done getting {self.url}")

    def html(self) -> str:
        return "html"

    async def close(self) -> None:
        pass

    async def __aenter__(self) -> "BrowserView":
        await self.load_url()
        return self

    async def __aexit__(self, type, value, traceback) -> bool:
        await self.close()
        return True if type is None else False


class PlaywrightBrowser:
    def __init__(self, semaphore: asyncio.Semaphore) -> None:
        self.semaphore = semaphore

    def open_new_view(self, url: str) -> BrowserView:
        ret = BrowserView(self.semaphore, url)
        return ret

    def quit(self) -> None:
        pass


class BrowserManager:
    def __init__(self, semaphore: asyncio.Semaphore) -> None:
        self._map = {"primary": PlaywrightBrowser(semaphore)}

    def get_browser(self, *, browser_type: str) -> PlaywrightBrowser:
        return self._map[browser_type]


async def do_job(dpbm: BrowserManager, url: str) -> None:
    dpb = dpbm.get_browser(browser_type="primary")
    async with dpb.open_new_view(url) as browser_view:
        print(browser_view.html())


async def do_prep(work_loop: AbstractEventLoop, dpbm: BrowserManager, job: Job) -> None:
    for i in range(0, 4):
        new_job = Job(JobType._EXPLOIT, job.orig_state + f", prep_{i}")
        await do_job(dpbm, f"prep_{i}")
        work_loop.create_task(do_exploit(work_loop, dpbm, new_job))


async def do_exploit(work_loop: AbstractEventLoop, dpbm: BrowserManager, job: Job) -> None:
    for i in range(0, 4):
        new_job = Job(JobType._VERIFY, job.orig_state + f", exploit_{i}")
        await do_job(dpbm, f"exploit_{i}")
        work_loop.create_task(do_verify(work_loop, dpbm, new_job))


async def do_verify(work_loop: AbstractEventLoop, dpbm: BrowserManager, job: Job) -> None:
    await do_job(dpbm, job.orig_state + ", verify")


async def main():
    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(600, loop=loop)
    dpbm = BrowserManager(semaphore)

    current_tasks = asyncio.Task.all_tasks()
    assert len(current_tasks) == 1
    main_task = list(current_tasks)[0]
    
    loop.create_task(do_prep(loop, dpbm, Job(JobType._PREP, "start")))

    while True:
        pending = [task for task in asyncio.Task.all_tasks() if task != main_task and not task.done()]
        if not pending:
            break
        await asyncio.gather(*pending)


asyncio.run(main())
