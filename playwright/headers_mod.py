import asyncio
import typing
from playwright.async_api import async_playwright
from playwright.async_api._generated import Route



async def mod_request_headers(route: Route) -> None:
    headers = route.request.headers

    new_headers = {k: "butt" for k in headers}
    await route.continue_(headers={**new_headers, "foo": "bar"})


async def get_title(url: str) -> None:
    async with async_playwright() as p:
        print("hi")
        browser = await p.chromium.launch(headless=False, slow_mo=10000)
        page = await browser.new_page()
        await page.route("**/*", mod_request_headers)
        await page.goto(url)
        title = await page.title()
        await browser.close()
        print(title)


async def main():
    task = asyncio.create_task(get_title("https://manytools.org/http-html-text/http-request-headers/"))
    await task

asyncio.run(main())
