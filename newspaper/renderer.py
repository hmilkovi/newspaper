import asyncio
from pyppeteer import launch
import time

async def render_js(url, headless=False, proxy=None, sleep=0.1):
    args = []
    if proxy:
        args = ['--proxy-server=%s' % proxy]
    browser = await launch(headless=headless, ignoreHTTPSErrors=True, dumpio=True, autoClose=False, args=args)
    page = await browser.newPage()
    await page.goto(url)
    if sleep:
        time.sleep(sleep)
    html = await page.content()
    await page.close()
    await browser.close()
    browser = None
    return html

def rendered_page(url, headless=True, proxy=None, sleep=0.1):
    html = asyncio.run(render_js(url, headless=headless, proxy=proxy, sleep=sleep))
    return html