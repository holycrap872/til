import asyncio
from playwright.async_api import async_playwright
from playwright.async_api._generated import Request, Response



async def log_request_headers(request: Request) -> None:
    print("request", request.method, request.url)


async def log_response_headers(response: Response) -> None:
    text = await response.text()
    body = await response.body()
    response.url
    response.request
    response.headers
    response.status
    response.request
    response.request.method
    response.request.
    response.
    print("response", response.status, response.url, len(text), len(body))


async def get_title(url: str) -> None:
    async with async_playwright() as p:
        print("hi")
        browser = await p.chromium.launch(headless=False, slow_mo=5000)
        page = await browser.new_page()
        page.on("request", log_request_headers)
        page.on("response", log_response_headers)
        await page.goto(url)
        title = await page.title()
        await browser.close()
        print(title)


async def main():
    task = asyncio.create_task(get_title("https://www.google.com"))
    await task

asyncio.run(main())
