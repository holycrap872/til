import asyncio
from playwright.async_api import async_playwright



async def get_title(url: str, semaphore) -> None:
    async with semaphore:
        async with async_playwright() as p:
            print("hi")
            browser = await p.chromium.launch(headless=False, slow_mo=5000)
            page = await browser.new_page()
            await page.goto(url)
            title = await page.title()
            await browser.close()
            print(title)


async def main():
    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(2, loop=loop)

    task_set = set()
    task_set.add(loop.create_task(get_title("https://www.google.com", semaphore)))
    task_set.add(loop.create_task(get_title("https://www.yahoo.com", semaphore)))
    task_set.add(loop.create_task(get_title("https://www.duckduckgo.com", semaphore)))
    task_set.add(loop.create_task(get_title("https://www.amazon.com", semaphore)))

    await asyncio.gather(*task_set)

asyncio.run(main())