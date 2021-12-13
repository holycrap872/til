import asyncio
from playwright.async_api import async_playwright


async def get_title(url: str) -> str:
    async with async_playwright() as p:
        print("hi")
        browser = await p.chromium.launch(headless=False, slow_mo=5000)
        page = await browser.new_page()
        await page.goto(url)
        print(f"sleeping in order to let {url} render")
        # You should use page.wait_for_timeout(5000) instead of time.sleep(5) and
        # it is better to not wait for a timeout at all, but sometimes it is useful
        # for debugging. In these cases, use our wait method instead of the time
        # module. This is because we internally rely on asynchronous operations and
        # when using time.sleep(5) they can't get processed correctly.
        page.wait_for_timeout(5000)
        print(f"done sleeping in order to let {url} to render")
        title = await page.title()
        await browser.close()
        return title


async def main():
    google_task = asyncio.create_task(get_title("https://www.google.com"))
    amazon_task = asyncio.create_task(get_title("https://www.amazon.com"))

    google_title = await google_task
    amazon_title = await amazon_task

    print(google_title)
    print(amazon_title)


asyncio.run(main())