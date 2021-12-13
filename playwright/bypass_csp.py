import asyncio
import typing
from playwright.async_api import async_playwright
from playwright.async_api._generated import Route, Dialog


async def on_dialog(dialog: Dialog):
    print(dialog)
    print(dir(dialog))
    msg = dialog.message
    print(f"Got popup with message {msg}")
    await dialog.accept()


async def get_title(url: str) -> None:
    async with async_playwright() as p:
        print("hi")
        browser = await p.chromium.launch(headless=False, slow_mo=10000)
        page = await browser.new_page(bypass_csp=True)
        page.on("dialog", on_dialog)
        await page.goto(url)
        title = await page.title()
        await browser.close()
        print(title)


async def main():
    task = asyncio.create_task(get_title("http://127.0.0.1:60760/beta?foo=%3C/h1%3E%3Cscript%3Ealert(4)%3C/script%3E"))
    await task

asyncio.run(main())
