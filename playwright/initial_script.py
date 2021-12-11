import asyncio
import time
from playwright.async_api import async_playwright


async def get_title(url: str) -> str:
    async with async_playwright() as p:
        print("hi")
        browser = await p.chromium.launch(headless=False, slow_mo=5000)
        page = await browser.new_page()
        await page.goto(url)
        print(f"sleeping in order to let {url} render")
        await asyncio.sleep(8)  # let render
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