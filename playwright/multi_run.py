import asyncio
from playwright.async_api import async_playwright



async def get_title(url: str, semaphore) -> None:
    async with semaphore:
        async with async_playwright() as p:
            print("hi")
            browser = await p.chromium.launch(headless=False, slow_mo=2000)
            page = await browser.new_page(bypass_csp=True)
            await page.goto(url)
            title = await page.title()
            page = await browser.new_page()
            await page.goto(url)
            await page.close()
            # You should use page.wait_for_timeout(5000) instead of time.sleep(5) and
            # it is better to not wait for a timeout at all, but sometimes it is useful
            # for debugging. In these cases, use our wait method instead of the time
            # module. This is because we internally rely on asynchronous operations and
            # when using time.sleep(5) they can't get processed correctly.
            page.wait_for_timeout(5000)
            await browser.close()
            print(title)


async def main():
    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(1, loop=loop)

    task_set = set()
    task_set.add(loop.create_task(get_title("https://www.google.com", semaphore)))
    task_set.add(loop.create_task(get_title("https://www.yahoo.com", semaphore)))
    task_set.add(loop.create_task(get_title("https://www.duckduckgo.com", semaphore)))
    task_set.add(loop.create_task(get_title("https://www.amazon.com", semaphore)))

    await asyncio.gather(*task_set)

asyncio.run(main())
