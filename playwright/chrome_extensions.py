import asyncio
import typing
from playwright.async_api import async_playwright
from playwright.async_api._generated import Route

# mockapi_path = "/Users/erizzi/Documents/workspace/DyePackInfraDeploy/src/DyePackInfrastructure/configuration/dyepack_lambda_resources/mockapi.crx"
# mockapi_path = "/Users/erizzi/DyePackChromeExtension/dist.crx"
mockapi_path = "/Users/erizzi/Documents/workspace/til/DyePackChromeExtension/dist"

# To run:
# 1. make everything in the /dist folder of the extension readable
# 2. point the load at the /dist folder

# DEPRECATED- If need to pack the extension for the given version
# 0. In terminal, go to /Users/erizzi/Library/Caches/ms-playwright/chromium-857950/chrome-mac/Chromium.app/Contents/MacOS/Chromium
#    - got it via:
# ```
# print(p.chromium.executable_path)
# ```
# 1. Go to control bar (top right of mac screen) -> About Chromium
# 2. Click "Extensions"
# 3. Put into developer mode (top right of chrome screen)
# 4. Load unpacked
# 5. Select ~/DyePackChromeExtension/dist

# 


async def get_title(url: str) -> None:
    async with async_playwright() as p:
        print("hi")
        userDataDir = '/tmp/test-user-data-dir'
        print(p.chromium.executable_path)
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=userDataDir,
            headless=False,
            args=[
                "--enable-extension-activity-logging",
                f"--disable-extensions-except={mockapi_path}",
                f"--load-extension={mockapi_path}",
            ],
            bypass_csp=True,
        )
        page = await browser.new_page()
        await page.goto(url)
        # You should use page.wait_for_timeout(5000) instead of time.sleep(5) and
        # it is better to not wait for a timeout at all, but sometimes it is useful
        # for debugging. In these cases, use our wait method instead of the time
        # module. This is because we internally rely on asynchronous operations and
        # when using time.sleep(5) they can't get processed correctly.
        page.wait_for_timeout(5000)
        title = await page.title()
        await browser.close()
        print(title)


async def main():
    task = asyncio.create_task(get_title("http://www.amazon.com"))
    await task

asyncio.run(main())
