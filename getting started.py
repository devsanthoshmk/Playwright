from time import time
import asyncio
from playwright.async_api import async_playwright

async def pw(link):
    async with async_playwright() as p:
        st=time()
        browser=await p.chromium.launch(headless=False)
        
        page=await browser.new_page()
        
        await page.goto(link)
        print(await page.title())
        print(time()-st)
        await browser.close()
st=time()
async def main():
    await asyncio.gather(pw("http://playwright.dev"),pw("https://playwright.dev/python/docs/library"))
asyncio.run(main())
print(time()-st)