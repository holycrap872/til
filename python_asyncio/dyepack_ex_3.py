import asyncio
import enum
import typing
from asyncio.events import AbstractEventLoop
from playwright.async_api import async_playwright


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
    def __init__(self, pw_browser, sempahore: asyncio.Semaphore, url: str) -> None:
        self.pw_browser = pw_browser
        self.semaphore = sempahore
        self.url = url

    async def load_url(self) -> None:
        async with self.semaphore:
            self.page = await self.pw_browser.new_page(bypass_csp=True)
            print(self.url)
            await self.page.goto(self.url)
            await asyncio.sleep(6)

    def html(self) -> str:
        return "html"

    async def close(self) -> None:
        await self.page.close()

    async def __aenter__(self) -> "BrowserView":
        await self.load_url()
        return self

    async def __aexit__(self, type, value, traceback) -> bool:
        await self.close()
        return True if type is None else False


class PlaywrightBrowser:
    def __init__(self, semaphore: asyncio.Semaphore) -> None:
        self.playwright = async_playwright()
        self.semaphore = semaphore

    async def prep(self) -> None:
        self.async_playwright = await self.playwright.__aenter__()
        self.pw_browser = await self.async_playwright.chromium.launch(headless=False, slow_mo=2000)

    def open_new_view(self, url: str) -> BrowserView:
        ret = BrowserView(self.pw_browser, self.semaphore, url)
        return ret

    async def quit(self) -> None:
        await self.playwright.__aexit__()


class BrowserManager:
    def __init__(self, semaphore: asyncio.Semaphore) -> None:
        self._map = {"primary": PlaywrightBrowser(semaphore)}

    async def prep(self) -> None:
        for b in self._map.values():
            await b.prep()


    def get_browser(self, *, browser_type: str) -> PlaywrightBrowser:
        return self._map[browser_type]


    async def teardown(self) -> None:
        for b in self._map.values():
            await b.quit()


async def do_job(dpbm: BrowserManager, url: str) -> None:
    dpb = dpbm.get_browser(browser_type="primary")
    async with dpb.open_new_view(url) as browser_view:
        print(browser_view.html())


async def do_prep(work_loop: AbstractEventLoop, dpbm: BrowserManager, job: Job) -> None:
    await do_job(dpbm, job.orig_state)
    for i in range(0, 4):
        new_job = Job(JobType._EXPLOIT, job.orig_state + f"/prep_{i}")
        work_loop.create_task(do_exploit(work_loop, dpbm, new_job))


async def do_exploit(work_loop: AbstractEventLoop, dpbm: BrowserManager, job: Job) -> None:
    await do_job(dpbm, job.orig_state)
    for i in range(0, 4):
        new_job = Job(JobType._VERIFY, job.orig_state + f"/exploit_{i}")
        work_loop.create_task(do_verify(work_loop, dpbm, new_job))


async def do_verify(work_loop: AbstractEventLoop, dpbm: BrowserManager, job: Job) -> None:
    await do_job(dpbm, job.orig_state + "/verify")


async def main():
    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(6, loop=loop)

    dpbm = BrowserManager(semaphore)
    await dpbm.prep()

    current_tasks = asyncio.Task.all_tasks()
    print(len(current_tasks))
    assert len(current_tasks) == 2

    loop.create_task(do_prep(loop, dpbm, Job(JobType._PREP, "https://www.example.com")))

    while True:
        pending = [task for task in asyncio.Task.all_tasks() if task not in current_tasks and not task.done()]
        print(pending)
        await asyncio.sleep(1)
        if not pending:
            break
        await asyncio.gather(*pending)

    await dpbm.teardown()

asyncio.run(main())
